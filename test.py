from graph.workflow import app

transaction = {
    "amount": 180000,
    "category": "shopping"
}

result = app.invoke(
    {
        "transaction": transaction
    }
)

print("\n--------------- FINAL RESPONSE ---------------\n")

print(result["response"])