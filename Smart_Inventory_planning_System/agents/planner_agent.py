def planner_agent(stock, min_stock, sales):
    if stock <= 0 or sales <= 0:
        return "Insufficient Data", 0, "Not enough data for planning"

    if stock < min_stock:
        qty = (min_stock - stock) + sales
        return "Reorder", qty, "Stock below minimum and demand is high"

    return "No Action", 0, "Stock level is sufficient"
