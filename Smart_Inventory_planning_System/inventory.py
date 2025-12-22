import sqlite3

conn = sqlite3.connect("inventory.db")
cur = conn.cursor()

# Create products table
cur.execute("DROP TABLE IF EXISTS products")
cur.execute("""
CREATE TABLE products (
    product TEXT PRIMARY KEY,
    min_stock INTEGER NOT NULL,
    unit TEXT NOT NULL
)
""")

# Default products
products = [
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

cur.executemany("INSERT INTO products VALUES (?, ?, ?)", products)
conn.commit()
conn.close()
print("✅ inventory.db created successfully")
