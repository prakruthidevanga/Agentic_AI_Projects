import subprocess
import openai
import os

USE_ONLINE_LLM = True
openai.api_key = os.getenv("OPENAI_API_KEY")

def llm_explain(product, decision, stock, min_stock, sales, unit, llm_mode="offline"):
    prompt = f"""
Generates a human-friendly explanation of the inventory decision in bullet points.
    Online LLM (OpenAI) is used if enabled and key is present.
    Offline fallback uses Ollama. If both fail, rule-based explanation is used.
    """

    prompt = f"""
You are an inventory planning assistant.

Product: {product}
Current stock: {stock} {unit}
Minimum stock: {min_stock} {unit}
Weekly sales: {sales} {unit}
Decision: {decision}

Give 3-5 short bullet points to explain this decision clearly in simple language for a shop owner.
"""
    
    explanation = ""

    html = "<ol>"

    if llm_mode == "online" and openai.api_key:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role":"system","content":"Explain clearly to shop owners."},{"role":"user","content":prompt}],
                temperature=0.4
            )
            text = response.choices[0].message.content.strip()
        except:
            text = ""

    else:  # offline fallback
        try:
            result = subprocess.run(["ollama","run","mistral"], input=prompt, capture_output=True, encoding="utf-8")
            text = result.stdout.strip()
        except:
            text = ""

    if not text:
        if decision == "Reorder":
            text = f"1. Your stock of {product} is below minimum.\n2. Sales are high.\n3. Reorder to avoid shortages.\n4. Keep customers happy."
        else:
            text = f"1. Stock level for {product} is sufficient.\n2. Sales are under control.\n3. Monitor regularly."

    for line in text.splitlines():
        line = line.strip("0123456789.- ")
        if line:
            html += f"<li>{line}</li>"

    html += "</ol>"
    return html
