import pandas as pd

def find_ids_within_ten_percentage_threshold(df, reference_value):
    
    reference_df = df[df['id_start'] == reference_value]
    average_distance = reference_df['distance'].mean()
    threshold_range = 0.1 * average_distance
    within_threshold_df = df[
        (df['id_start'] != reference_value) &  # Exclude the reference value itself
        (df['distance'] >= average_distance - threshold_range) &
        (df['distance'] <= average_distance + threshold_range)
    ]
    sorted_ids_within_threshold = sorted(within_threshold_df['id_start'].unique())

    return sorted_ids_within_threshold


def generate_car_matrix():
   
    df = pd.read_csv('dataset-1.csv')
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car')
    car_matrix = car_matrix.fillna(0)
    car_matrix.values[[range(len(car_matrix))]*2] = 0

    return car_matrix

def unroll_distance_matrix(distance_matrix):

    distance_matrix_reset = distance_matrix.reset_index()
    unrolled_distances = pd.DataFrame(columns=['id_start', 'id_end', 'distance'])
    for _, row in distance_matrix_reset.iterrows():
        id_start = row['id_1']
        
        for id_end, distance in row.items():
            if id_start != id_end:  
                unrolled_distances = pd.concat({
                    'id_start': id_start,
                    'id_end': id_end,
                    'distance': distance
                }, ignore_index=True)

    return unrolled_distances

result_matrix = generate_car_matrix()

unrolled_distances = unroll_distance_matrix(result_matrix)



reference_value = 123  
result_within_threshold = find_ids_within_ten_percentage_threshold(unrolled_distances, reference_value)


print(result_within_threshold)
