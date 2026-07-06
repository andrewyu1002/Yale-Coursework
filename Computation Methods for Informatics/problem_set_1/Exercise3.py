def alg1(data):
    data = list(data)
    changes = True
    while changes:
        changes = False
        for i in range(len(data) - 1):
            if data[i + 1] < data[i]:
                data[i], data[i + 1] = data[i + 1], data[i]
                changes = True
    return data

def alg2(data):
    if len(data) <= 1:
        return data
    else:
        split = len(data) // 2
        left = iter(alg2(data[:split]))
        right = iter(alg2(data[split:]))
        result = []
        # note: this takes the top items off the left and right piles
        left_top = next(left)
        right_top = next(right)
        while True:
            if left_top < right_top:
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
                
def data1(n, sigma=10, rho=28, beta=8/3, dt=0.01, x=1, y=1, z=1):
    import numpy
    state = numpy.array([x, y, z], dtype=float)
    result = []
    for _ in range(n):
        x, y, z = state
        state += dt * numpy.array([
            sigma * (y - x),
            x * (rho - z) - y,
            x * y - beta * z
        ])
        result.append(float(state[0] + 30))
    return result

def data2(n):
    return list(range(n))

def data3(n):
    return list(range(n, 0, -1))

#Q3a -------------------------------------------------------------------

data1_10 = data1(10)
data2_10 = data2(10)
data3_10 = data3(10)

print("data1_10 is composed of", data1_10)
print("After alg 1, data1_10 becomes", alg1(data1_10))
print("After alg 2, data1_10 becomes", alg2(data1_10), end="\n\n")

print("data2_10 is composed of", data2_10)
print("After alg 1, data2_10 becomes", alg1(data2_10))
print("After alg 2, data2_10 becomes", alg2(data2_10), end="\n\n")

print("data3_10 is composed of", data3_10)
print("After alg 1, data3_10 becomes", alg1(data3_10))
print("After alg 2, data3_10 becomes", alg2(data3_10), end="\n\n")

# data1_100 = data1(100)
# data2_100 = data2(100)
# data3_100 = data3(100)

# print("data1_100 is composed of", data1_100)
# print("After alg 1, data1_100 becomes", alg1(data1_100))
# print("After alg 2, data1_100 becomes", alg2(data1_100), end="\n\n")

# print("data2_100 is composed of", data2_100)
# print("After alg 1, data2_100 becomes", alg1(data2_100))
# print("After alg 2, data2_100 becomes", alg2(data2_100), end="\n\n")

# print("data3_100 is composed of", data3_100)
# print("After alg 1, data3_100 becomes", alg1(data3_100))
# print("After alg 2, data3_100 becomes", alg2(data3_100), end="\n\n")

# data1_1000 = data1(1000)
# data2_1000 = data2(1000)
# data3_1000 = data3(1000)

# print("data1_1000 is composed of", data1_1000)
# print("After alg 1, data1_1000 becomes", alg1(data1_1000))
# print("After alg 2, data1_1000 becomes", alg2(data1_1000), end="\n\n")

# print("data2_1000 is composed of", data2_1000)
# print("After alg 1, data2_1000 becomes", alg1(data2_1000))
# print("After alg 2, data2_1000 becomes", alg2(data2_1000), end="\n\n")

# print("data3_1000 is composed of", data3_1000)
# print("After alg 1, data3_1000 becomes", alg1(data3_1000))
# print("After alg 2, data3_1000 becomes", alg2(data3_1000), end="\n\n")

#Q3b -------------------------------------------------------------------

#Answer in README

#Q3c -------------------------------------------------------------------

import numpy as np
import time
import matplotlib.pyplot as plt
from tqdm import tqdm

n_values = np.logspace(1, 4, num=15, dtype=int)

def time_alg(alg, data_function, n_values):
    alg_times = []
    for n in tqdm(n_values, desc="Timing Algorithm"):
        data = data_function(n)
        start = time.perf_counter()
        alg(data)
        alg_times.append(time.perf_counter() - start)
    return alg_times

def time_plot(alg1_times, alg2_times, n_values, title):
    plt.loglog(n_values, alg1_times, label="alg1", color = "red")
    plt.loglog(n_values, alg2_times, label="alg2", color = "blue")
    plt.xlabel('n')
    plt.ylabel('Time (seconds)')
    plt.title(title)
    plt.legend()
    plt.show()

data_1_alg_1 = time_alg(alg1, data1, n_values)
data_1_alg_2 = time_alg(alg2, data1, n_values)
print("The times to sort data 1 with algorithm 1 are:,", data_1_alg_1)
print("The times to sort data 1 with algorithm 2 are:,", data_1_alg_2)
time_plot(data_1_alg_1, data_1_alg_2, n_values, "Time Performance of alg1 and alg2 on data1")

data_2_alg_1 = time_alg(alg1, data2, n_values)
data_2_alg_2 = time_alg(alg2, data2, n_values)
print("The times to sort data 2 with algorithm 1 are:,", data_2_alg_1)
print("The times to sort data 2 with algorithm 2 are:,", data_2_alg_2)
time_plot(data_2_alg_1, data_2_alg_2, n_values, "Time Performance of alg1 and alg2 on data2")

data_3_alg_1 = time_alg(alg1, data3, n_values)
data_3_alg_2 = time_alg(alg2, data3, n_values)
print("The times to sort data 3 with algorithm 1 are:,", data_3_alg_1)
print("The times to sort data 3 with algorithm 2 are:,", data_3_alg_2)
time_plot(data_3_alg_1, data_3_alg_2, n_values, "Time Performance of alg1 and alg2 on data3")

#Q3d -------------------------------------------------------------------

#Answers in README