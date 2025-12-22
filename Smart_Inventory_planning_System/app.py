from flask import Flask, render_template, request, jsonify
import sqlite3
from agents.planner_agent import planner_agent
from agents.llm_agent import llm_explain
from agents.executor_agent import executor_agent

app = Flask(__name__)

# -----------------------------
# Initialize database
# -----------------------------
def init_db():
    conn = sqlite3.connect("inventory.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product TEXT PRIMARY KEY,
        min_stock INTEGER NOT NULL,
        unit TEXT NOT NULL
    )
    """)
    default_products = [
        ('Rice', 40, 'kg'),
        ('Sugar', 25, 'kg'),
        ('Oil', 30, 'liters'),
        ('Tea Powder', 15, 'packets'),
        ('Coffee Powder', 18, 'packets'),
        ('Wheat', 35, 'kg'),
        ('Salt', 20, 'kg'),
        ('Soap', 50, 'pieces'),
        ('Shampoo', 30, 'bottles'),
        ('Biscuits', 60, 'packets'),
        ('Milk Packets', 70, 'packets'),
        ('Detergent', 40, 'kg')
    ]
    cur.executemany(
        "INSERT OR IGNORE INTO products (product, min_stock, unit) VALUES (?, ?, ?)",
        default_products
    )
    conn.commit()
    conn.close()

init_db()  # Initialize DB at app start

# -----------------------------
# Helper to get product info
# -----------------------------
def get_product_info(product):
    conn = sqlite3.connect("inventory.db")
    cur = conn.cursor()
    cur.execute("SELECT min_stock, unit FROM products WHERE product=?", (product,))
    row = cur.fetchone()
    conn.close()
    if row:
        return row[0], row[1]
    return 20, "units"

# -----------------------------
# Helper to parse stock/unit input
# -----------------------------
def parse_value(value):
    if not value:
        return 0, "units"
    parts = value.strip().split()
    try:
        number = int(parts[0])
    except:
        number = 0
    unit = parts[1] if len(parts) > 1 else "units"
    return number, unit

# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_min_stock", methods=["POST"])
def min_stock_route():
    data = request.json
    min_stock, unit = get_product_info(data["product"])
    return jsonify({"min_stock": min_stock, "unit": unit})

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    product = data["product"]
    llm_mode = data.get("llm_mode", "offline")

    stock_value, stock_unit = parse_value(data["stock"])
    sales_value, _ = parse_value(data["sales"])
    min_stock, unit = get_product_info(product)

    decision, qty, _ = planner_agent(stock_value, min_stock, sales_value)

    reason_html = llm_explain(
        product=product,
        decision=decision,
        stock=stock_value,
        min_stock=min_stock,
        sales=sales_value,
        unit=unit,
        llm_mode=llm_mode
    )

    return jsonify({
        "decision": decision,
        "quantity": qty,
        "unit": unit,
        "reason": reason_html
    })

@app.route("/action_result", methods=["POST"])
def action_result():
    action = request.form["action"]
    qty = request.form.get("quantity", "")
    if action == "Accept":
        bg_color = "linear-gradient(to right, #11998e, #38ef7d)"
        text_color = "#11998e"
        title = "Action Accepted"
        message = "You accepted the recommendation. Stock will be maintained properly."
    elif action == "Modify":
        bg_color = "linear-gradient(to right, #f7971e, #ffd200)"
        text_color = "#f39c12"
        title = "Quantity Modified"
        message = "You modified the quantity. Make sure stock is sufficient for upcoming sales."
    else:
        bg_color = "linear-gradient(to right, #cb2d3e, #ef473a)"
        text_color = "#c0392b"
        title = "Action Ignored"
        message = "You ignored the recommendation. Monitor stock levels carefully."

    return render_template(
        "action_result.html",
        bg_color=bg_color,
        title=title,
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)
