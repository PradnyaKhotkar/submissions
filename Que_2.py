import pandas as pd

def get_type_count(df):
    # Add a new categorical column 'car_type' based on values of the 'car' column
    df['car_type'] = pd.cut(df['car'],
                            bins=[float('-inf'), 15, 25, float('inf')],
                            labels=['low', 'medium', 'high'],
                            right=False)

    # Calculate the count of occurrences for each 'car_type' category
    type_count = df['car_type'].value_counts().to_dict()

    # Sort the dictionary alphabetically based on keys
    sorted_type_count = dict(sorted(type_count.items()))

    return sorted_type_count

# Example usage:
# Assuming dataset-1.csv is in the same directory as your Python script or notebook
df = pd.read_csv('dataset-1.csv')
result_type_count = get_type_count(df)
print(result_type_count)
