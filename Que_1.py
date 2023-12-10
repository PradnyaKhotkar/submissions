import pandas as pd
import networkx as nx

def calculate_distance_matrix(df):
    # Create a directed graph
    G = nx.DiGraph()

    # Add edges and their distances to the graph
    for _, row in df.iterrows():
        G.add_edge(row['id_start'], row['id_end'], distance=row['distance'])
        G.add_edge(row['id_end'], row['id_start'], distance=row['distance'])  # Bidirectional

    # Calculate shortest path distances between all pairs of nodes
    all_nodes = list(G.nodes)
    distance_matrix = pd.DataFrame(index=all_nodes, columns=all_nodes)

    for start_node in all_nodes:
        for end_node in all_nodes:
            if start_node == end_node:
                distance_matrix.loc[start_node, end_node] = 0
            else:
                try:
                    distance = nx.shortest_path_length(G, start_node, end_node, weight='distance')
                    distance_matrix.loc[start_node, end_node] = distance
                except nx.NetworkXNoPath:
                    # If no path exists, set the distance to NaN
                    distance_matrix.loc[start_node, end_node] = float('nan')

    return distance_matrix

# Example usage:
# Assuming dataset-3.csv is in the same directory as your Python script or notebook
df = pd.read_csv('dataset-3.csv')

# Apply the function to calculate the distance matrix
distance_matrix = calculate_distance_matrix(df)

# Print the resulting distance matrix
print(distance_matrix)
