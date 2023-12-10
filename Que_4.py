import pandas as pd

def filter_routes(df):
    
    average_truck_values = df.groupby('route')['truck'].mean()
    selected_routes = average_truck_values[average_truck_values > 7].index.tolist()
    selected_routes.sort()

    return selected_routes

df = pd.read_csv('dataset-1.csv')
result_routes = filter_routes(df)
print(result_routes)
