import pandas as pd

def calculate_toll_rate(df):
    
    rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}

    
    for vehicle_type, rate_coefficient in rate_coefficients.items():
        df[vehicle_type] = df['distance'] * rate_coefficient

    return df

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
                unrolled_distances = unrolled_distances.append({
                    'id_start': id_start,
                    'id_end': id_end,
                    'distance': distance
                }, ignore_index=True)

    return unrolled_distances

result_matrix = generate_car_matrix()

unrolled_distances = unroll_distance_matrix(result_matrix)

df_with_toll_rates = calculate_toll_rate(unrolled_distances)

print(df_with_toll_rates)
