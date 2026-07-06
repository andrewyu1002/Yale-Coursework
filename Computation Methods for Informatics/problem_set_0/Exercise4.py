import random
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

def generate_population(n, d):
    pop_list = [True] * d + [False] * (n - d)
    random.shuffle(pop_list)
    return pop_list

def pop_sample(s, pop):
    random_sample = random.sample(pop, s)
    sample_response = []
    for sample in random_sample:
        flip = random.choice(["heads", "tails"])
        if(flip == "heads"):
            flip2 = random.choice(["heads", "tails"])
            if(flip2 == "heads"):
                sample_response.append(True)
            else:
                sample_response.append(False)
        else:
            sample_response.append(sample)
    return sample_response

def estimate(n, d, s):
    population = generate_population(n, d)
    sample = (pop_sample(s, population))
    sample_drug_users = sum(sample) / s
    #derived from f = 0.25 + 0.5r, where f is the fraction of reported drug users from the sample and r is the true 
    #(in this case, estimated) fraction of drug users
    estimate = 2 * (sample_drug_users - 0.25)
    if(estimate < 0):
        estimate = 0
    estimate_number = estimate * n
    return estimate_number

#This function will be used in 4f to calculate the mean estimate of number of users for a specific sample side
def estimate_with_neg(n, d, s):
    population = generate_population(n, d)
    sample = (pop_sample(s, population))
    sample_drug_users = sum(sample) / s
    estimate = 2 * (sample_drug_users - 0.25)
    estimate_number = estimate * n
    return estimate_number

def estimate_histogram(reps):
    estimate_list = []
    for i in range(reps):
        estimate_inst = estimate(1000, 100, 50)
        estimate_list.append(estimate_inst)
    plt.hist(estimate_list, bins=30, color='skyblue', edgecolor='black')
    plt.xlabel('Drug Users')
    plt.ylabel('Frequency')
    plt.title('Frequencies of Estimated Number of drug users')
    plt.show()
    return None

def sample_size_estimates(reps):
    sample_sizes = np.arange(10, 1010, 10)
    means_100 = []
    means_500 = []
    std_100 = []
    std_500 = []
    for sample_size in tqdm(sample_sizes, desc="Sample Sizes"):
        estimates_100 = []
        estimates_500 = []
        for i in range(reps):
            sample_size_100estimate = estimate_with_neg(1000, 100, sample_size)
            estimates_100.append(sample_size_100estimate)
            sample_size_500estimate = estimate_with_neg(1000, 500, sample_size)
            estimates_500.append(sample_size_500estimate)
        means_100.append(np.mean(estimates_100))
        std_100.append(np.std(estimates_100))
        means_500.append(np.mean(estimates_500))
        std_500.append(np.std(estimates_500))
    plt.plot(sample_sizes, means_100, label="100 Drug Users", color="blue")
    plt.fill_between(sample_sizes, np.array(means_100) - np.array(std_100), np.array(means_100) + np.array(std_100), 
                     color="blue", alpha=0.2)
    plt.plot(sample_sizes, means_500, label="500 Drug Users", color="red")
    plt.fill_between(sample_sizes, np.array(means_500) - np.array(std_500), np.array(means_500) + np.array(std_500), 
                     color="red", alpha=0.2)
    plt.xlabel("Sample Size")
    plt.ylabel("Mean Estimated Number of Drug Users")
    plt.title("Mean Estimated Number of Drug Users vs Sample Size")
    plt.legend()
    plt.grid(True)
    plt.show()
    return None

sample_size_estimates(250)