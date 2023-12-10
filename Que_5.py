import pandas as pd
import datetime

def calculate_time_based_toll_rates(df):
    
    weekday_time_ranges = [
        {'start': datetime.time(0, 0, 0), 'end': datetime.time(10, 0, 0), 'factor': 0.8},
        {'start': datetime.time(10, 0, 0), 'end': datetime.time(18, 0, 0), 'factor': 1.2},
        {'start': datetime.time(18, 0, 0), 'end': datetime.time(23, 59, 59), 'factor': 0.8}
    ]
    weekend_time_ranges = [
        {'start': datetime.time(0, 0, 0), 'end': datetime.time(23, 59, 59), 'factor': 0.7}
    ]
    for time_range in weekday_time_ranges:
        mask = (df['start_time'].dt.time >= time_range['start']) & (df['start_time'].dt.time <= time_range['end'])
        df.loc[mask, ['moto', 'car', 'rv', 'bus', 'truck']] *= time_range['factor']
    for time_range in weekend_time_ranges:
        mask = (df['start_time'].dt.time >= time_range['start']) & (df['start_time'].dt.time <= time_range['end'])
        df.loc[mask, ['moto', 'car', 'rv', 'bus', 'truck']] *= time_range['factor']

    df['start_day'] = df['start_time'].dt.day_name().str.capitalize()
    df['end_day'] = df['end_time'].dt.day_name().str.capitalize()
    df['start_time'] = df['start_time'].dt.time
    df['end_time'] = df['end_time'].dt.time

    return df

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

df_with_time_based_toll_rates = calculate_time_based_toll_rates(df_with_toll_rates)


print(df_with_time_based_toll_rates)
