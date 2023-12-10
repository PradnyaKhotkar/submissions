import pandas as pd
import numpy as np

# Function to generate car matrix
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

# Function to multiply matrix
def multiply_matrix(input_matrix):
    # Create a copy of the input matrix to avoid modifying the original DataFrame
    modified_matrix = input_matrix.copy()

    # Use NumPy to perform element-wise operations
    modified_matrix = np.where(modified_matrix > 20, modified_matrix * 0.75, modified_matrix * 1.25)

    # Round the values to 1 decimal place
    modified_matrix = np.round(modified_matrix, 1)

    # Convert the NumPy array back to a DataFrame
    modified_matrix = pd.DataFrame(modified_matrix, index=input_matrix.index, columns=input_matrix.columns)

    return modified_matrix

# Example usage:
# Generate the car matrix
result_matrix = generate_car_matrix()

# Multiply and modify the matrix
modified_result_matrix = multiply_matrix(result_matrix)

# Print the modified matrix
print(modified_result_matrix)
