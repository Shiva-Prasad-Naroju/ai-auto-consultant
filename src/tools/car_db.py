import pandas as pd

class CarDatabase:
    def __init__(self, file_path="data/cars.csv"):
        self.df = pd.read_csv(file_path)
    
    def search_car(self, query: str):
        results = self.df[self.df['car_name'].str.contains(query, case=False)]
        if results.empty:
            return f"No data found for {query}"
        return results.to_dict(orient='records')
