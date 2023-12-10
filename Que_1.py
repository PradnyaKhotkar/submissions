import pandas as pd

def generate_car_matrix():
    # Assuming dataset-1.csv is in the same directory as your Python script or notebook
    df = pd.read_csv('dataset-1.csv')

    # Pivot the DataFrame to create the desired matrix
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car')

    # Replace NaN values with 0
    car_matrix = car_matrix.fillna(0)

    # Set diagonal values to 0
    car_matrix.values[[range(len(car_matrix))]*2] = 0

    return car_matrix

# Example usage:
result_matrix = generate_car_matrix()
print(result_matrix)
