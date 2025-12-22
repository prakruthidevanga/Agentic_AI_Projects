def feedback_agent(stock, sales):
    if sales > stock:
        return "High demand detected. Consider increasing minimum stock."
    return "Inventory levels are balanced."

