import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

with sqlite3.connect("problem_set_0/hw0-population.db") as db:
    data = pd.read_sql_query("SELECT * FROM population", db)

print(data)

def age_distribution():
    age_mean = data['age'].mean()
    age_std = data['age'].std()
    age_min = data['age'].min()
    age_max = data['age'].max()
    print("The mean age is", age_mean)
    print("The standard deviation for age is", age_std)
    print("The minimum age is", age_min)
    print("The maximum age is", age_max)
    #calculations for number of bins
    q1 = data['age'].quantile(0.25)
    q3 = data['age'].quantile(0.75)
    iqr = q3 - q1
    num_bins = (age_max - age_min) / (2 * iqr / (data.shape[0] ** (1/3)))
    # print("The number of bins should be", num_bins)
    plt.hist(data['age'], bins=70, color='skyblue', edgecolor='black')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Age Distribution Histogram')
    plt.show()
    return None

def weight_distribution():
    weight_mean = data['weight'].mean()
    weight_std = data['weight'].std()
    weight_min = data['weight'].min()
    weight_max = data['weight'].max()
    print("The mean weight is", weight_mean)
    print("The standard deviation for weight is", weight_std)
    print("The minimum weight is", weight_min)
    print("The maximum weight is", weight_max)
    q1 = data['weight'].quantile(0.25)
    q3 = data['weight'].quantile(0.75)
    iqr = q3 - q1
    num_bins = (weight_max - weight_min) / (2 * iqr / (data.shape[0] ** (1/3)))
    # print("The number of bins should be", num_bins)
    plt.hist(data['weight'], bins=196, color='skyblue', edgecolor='black')
    plt.xlabel('Weight')
    plt.ylabel('Frequency')
    plt.title('Weight Distribution Histogram')
    plt.show()
    return None

def scatterplot():
    plt.scatter(data['weight'], data['age'], s=5)
    plt.xlabel('Weight')
    plt.ylabel('Age')
    plt.title('Weights vs. Ages Scatterplot')
    plt.show()
    return None

age_distribution()
weight_distribution()
scatterplot()

#To determine an individual outlier based on information on the scatterplot
result = data[(np.floor(data['weight']) == 21) & (np.floor(data['age']) == 41)]
print(result)