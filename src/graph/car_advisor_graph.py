from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from agents.spec_retriever import retrieve_car_specs
from agents.evaluator import evaluate_specs

class CarAdvisorState(TypedDict):
    car_name: str
    specs: dict
    evaluation: str

def build_graph():
    workflow = StateGraph(CarAdvisorState)  # pass schema here

    # Step 1: Retrieve specs
    workflow.add_node("spec_retriever", lambda state: {
        "specs": retrieve_car_specs.invoke(state["car_name"])
    })

    # Step 2: Evaluate specs
    workflow.add_node("evaluator", lambda state: {
        "evaluation": evaluate_specs(state["specs"])
    })

    # Edges
    workflow.add_edge(START, "spec_retriever")
    workflow.add_edge("spec_retriever", "evaluator")
    workflow.add_edge("evaluator", END)

    return workflow
