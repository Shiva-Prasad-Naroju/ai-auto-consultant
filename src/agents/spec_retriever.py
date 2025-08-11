from langchain_core.tools import tool
from tools.car_db import CarDatabase

db = CarDatabase()

@tool
def retrieve_car_specs(car_name: str):
    """Retrieve car specifications from the database."""
    results = db.search_car(car_name)
    if isinstance(results, list) and results:
        return results[0]
    return results
