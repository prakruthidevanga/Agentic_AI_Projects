import sqlite3

def executor_agent(product, quantity, action):
    conn = sqlite3.connect("inventory.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS actions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        quantity INTEGER,
        action TEXT
    )""")

    cur.execute(
        "INSERT INTO actions (product, quantity, action) VALUES (?, ?, ?)",
        (product, quantity, action)
    )

    conn.commit()
    conn.close()

