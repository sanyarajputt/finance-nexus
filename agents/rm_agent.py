import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API key
load_dotenv()

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def respond(transaction, fraud_detected):

    if fraud_detected:

        prompt = f"""
You are SBI Nexus, an AI Relationship Manager.

A customer has made this transaction:

Category: {transaction['category']}
Amount: ₹{transaction['amount']}

The Fraud Agent has flagged it as suspicious.

Respond politely in 2–3 sentences.

Ask whether the customer recognizes the transaction.
Offer to help secure the account if needed.
"""

    else:

        prompt = f"""
You are SBI Nexus, an AI Relationship Manager.

Transaction:

Category: {transaction['category']}
Amount: ₹{transaction['amount']}

Everything looks normal.

Respond in a friendly way.
"""

    response = llm.invoke(prompt)

    return response.content