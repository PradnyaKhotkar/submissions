import pandas as pd

def get_bus_indexes(df):
    # Calculate the mean value of the 'bus' column
    bus_mean = df['bus'].mean()

    # Identify indices where the 'bus' values are greater than twice the mean value
    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()

    # Sort the indices in ascending order
    bus_indexes.sort()

    return bus_indexes

# Example usage:
# Assuming dataset-1.csv is in the same directory as your Python script or notebook
df = pd.read_csv('dataset-1.csv')
result_bus_indexes = get_bus_indexes(df)
print(result_bus_indexes)
