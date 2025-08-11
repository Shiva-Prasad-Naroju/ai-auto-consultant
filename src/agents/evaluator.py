from langchain_groq import ChatGroq

import os
from dotenv import load_dotenv

# Load the environement variables from .env
load_dotenv()

# Set the groq api key
groq_api_key=os.getenv("GROQ_API_KEY")

# Initialize Groq LLM
llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0.3,
    groq_api_key=groq_api_key
)

def evaluate_specs(specs: dict) -> str:
    """
    Given car specs, return an evaluation for a buyer.
    Specs should be a dictionary with keys like 'car_name', 'price_lakh', etc.
    """
    if isinstance(specs, list):
        if specs:
            specs = specs[0]
        else:
            return "No specs found for evaluation."

    specs_str = "\n".join([f"{k}: {v}" for k, v in specs.items()])
    prompt = f"Evaluate the following car specs for a potential buyer:\n{specs_str}\n" \
             f"Give your analysis in 3-4 bullet points."

    response = llm.invoke(prompt)
    return response.content
