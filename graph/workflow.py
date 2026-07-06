from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.fraud_agent import check_transaction
from agents.rm_agent import respond


class AgentState(TypedDict):
    transaction: dict
    fraud: bool
    response: str


def fraud_node(state):

    transaction = state["transaction"]

    state["fraud"] = check_transaction(transaction)

    return state


def rm_node(state):

    transaction = state["transaction"]

    fraud = state["fraud"]

    state["response"] = respond(transaction, fraud)

    return state


graph = StateGraph(AgentState)

graph.add_node("Fraud Agent", fraud_node)

graph.add_node("RM Agent", rm_node)

graph.set_entry_point("Fraud Agent")

graph.add_edge("Fraud Agent", "RM Agent")

graph.add_edge("RM Agent", END)

app = graph.compile()