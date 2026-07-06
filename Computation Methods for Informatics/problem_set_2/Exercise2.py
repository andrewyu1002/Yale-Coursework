from multiprocessing import Pool, cpu_count
import time
import random
import matplotlib.pyplot as plt
import numpy as np

def alg2(data, key_index = 0):
    if len(data) <= 1:
        return data
    else:
        split = len(data) // 2
        left = iter(alg2(data[:split], key_index))
        right = iter(alg2(data[split:], key_index))
        result = []
        # note: this takes the top items off the left and right piles
        left_top = next(left)
        right_top = next(right)
        while True:
            left_key = left_top[key_index]
            right_key = right_top[key_index]

            if left_key < right_key:
                result.append(left_top)
                try:
                    left_top = next(left)
                except StopIteration:
                    # nothing remains on the left; add the right + return
                    return result + [right_top] + list(right)
            else:
                result.append(right_top)
                try:
                    right_top = next(right)
                except StopIteration:
                    # nothing remains on the right; add the left + return
                    return result + [left_top] + list(left)

def merge_sorted(left, right, key_index):
    left = iter(left)
    right = iter(right)
    result = []
    left_top = next(left)
    right_top = next(right)
    while True:
        left_key = left_top[key_index]
        right_key = right_top[key_index]

        if left_key < right_key:
            result.append(left_top)
            try:
                left_top = next(left)
            except StopIteration:
                # nothing remains on the left; add the right + return
                return result + [right_top] + list(right)
        else:
            result.append(right_top)
            try:
                right_top = next(right)
            except StopIteration:
                # nothing remains on the right; add the left + return
                return result + [left_top] + list(left)

def alg2_parallel(data, key_index):
    if len(data) <= 1:
        return data
    elif len(data) < 1000:
        return alg2(data, key_index)

    chunk_size = len(data) // cpu_count()
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    with Pool(processes=cpu_count()) as pool:
        sorted_chunks = pool.map(alg2, chunks)

    sorted_data = sorted_chunks[0]
    for chunk in sorted_chunks[1:]:
        sorted_data = merge_sorted(sorted_data, chunk, key_index)

    return sorted_data
    
def generate_data(num_entries):
    return [(i, f"Patient {i}") for i in random.sample(range(num_entries), num_entries)]

def measure_performance(data_size):
    data = generate_data(data_size)

    start_time = time.perf_counter()
    alg2(data, key_index = 0)
    serial_duration = time.perf_counter() - start_time

    start_time = time.perf_counter()
    alg2_parallel(data, key_index = 0)
    parallel_duration = time.perf_counter() - start_time

    return serial_duration, parallel_duration
    
if __name__ == '__main__':
    patient_data_tuple_1 = [
        (5, "John Doe"),
        (7, "Jane Doe"),
        (24, "Andrew Yu"),
        (1, "Adam Smith"),
        (18, "Emily So")
    ]
    sorted_patient_tuple_1 = alg2(patient_data_tuple_1, key_index = 0)
    print(f'{sorted_patient_tuple_1 = }')

    patient_data_tuple_2 = [
        (5, "John Doe"),
        (7, "John Doe"),
        (24, "Andrew Yu"),
        (1, "Andrew Yu"),
        (18, "Emily So")
    ]
    sorted_patient_tuple_2 = alg2(patient_data_tuple_2, key_index = 0)
    print(f'{sorted_patient_tuple_2 = }')

    patient_data_tuple_3 = [
        ("Sebastian Lee", 3),
        ("Luke Rowan", 15),
        ("Andrew Yu", 4),
        ("Rachel Wei", 14),
        ("Jane Zhang", 23)
    ]
    sorted_patient_tuple_3_name = alg2(patient_data_tuple_3, key_index = 0)
    print(f'{sorted_patient_tuple_3_name = }')

    sorted_patient_tuple_3_number = alg2(patient_data_tuple_3, key_index = 1)
    print(f'{sorted_patient_tuple_3_number = }')

    patient_data_tuple_1 = [
        (5, "John Doe"),
        (7, "Jane Doe"),
        (24, "Andrew Yu"),
        (1, "Adam Smith"),
        (18, "Emily So")
    ]

    sorted_patient_tuple_1_parallel = alg2_parallel(patient_data_tuple_1, key_index=0)
    print(f'{sorted_patient_tuple_1_parallel = }')

    sizes = [1000, 10000, 100000, 1000000, 10000000]
    serial_times = []
    parallel_times = []

    for size in sizes:
        serial_time, parallel_time = measure_performance(size)
        serial_times.append(serial_time)
        parallel_times.append(parallel_time)
        print(f"Data Size: {size}, Serial Time: {serial_time}s, Parallel Time: {parallel_time}s")

    plt.figure(figsize=(12, 6))
    plt.loglog(sizes, serial_times, color='blue', label='Serial Time')
    plt.loglog(sizes, parallel_times, color='red', label='Parallel Time')

    plt.xlabel('Size of Dataset')
    plt.ylabel('Time to Sort')
    plt.title('Serial vs Parallel Ordering of Large Datasets')
    plt.legend()
    plt.grid(True)
    plt.show()