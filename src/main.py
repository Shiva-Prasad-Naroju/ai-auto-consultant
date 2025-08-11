import logging

logging.basicConfig(
    level=logging.DEBUG,  # overall minimum level
    format='[%(asctime)s][%(levelname)s][%(name)s] %(message)s',
    datefmt='%H:%M:%S'
)

# Fine-tune noisy libraries to higher log level
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("groq._base_client").setLevel(logging.WARNING)

# Keep useful libraries verbose
logging.getLogger("langgraph").setLevel(logging.DEBUG)
logging.getLogger("langchain").setLevel(logging.DEBUG)


from graph.car_advisor_graph import build_graph

if __name__ == "__main__":
    # After building we need to compile it together.
    graph = build_graph().compile() 

    user_input = input("Enter car name: ")
    
    # invoke the graph using .invoke method (This is a runnable)
    result = graph.invoke({"car_name": user_input})
    
    print("\n--- Car Evaluation ---")
    print(result["evaluation"])
