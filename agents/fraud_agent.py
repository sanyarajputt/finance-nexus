import pandas as pd

df = pd.read_csv("data/transactions.csv")

def check_transaction(transaction):

    category = transaction["category"]
    amount = transaction["amount"]

    previous = df[
        (df["category"] == category) &
        (df["type"] == "debit")
    ]

    average = previous["amount"].mean()

    threshold = average * 3

    print(f"Category : {category}")
    print(f"Average  : ₹{average:.2f}")
    print(f"Threshold: ₹{threshold:.2f}")
    print(f"Current  : ₹{amount}")

    if amount > threshold:
        return True

    return False