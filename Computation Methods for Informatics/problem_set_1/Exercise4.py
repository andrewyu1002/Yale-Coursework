import numpy as np
import time
import matplotlib.pyplot as plt
from tqdm import tqdm
import random
import string

class Tree:
    def __init__(self):
        self._value = None
        self._data = None
        self.left = None
        self.right = None

    #Q4a -------------------------------------------------------------------

    def add(self, value, data):
        if self._value is None:
            self._value = value
            self._data = data
        elif value < self._value:
            if self.left is None:
                self.left = Tree()
            self.left.add(value, data)
        elif value > self._value:
            if self.right is None:
                self.right = Tree()
            self.right.add(value, data)
        else:
            self._data = data

    #Added this section to see if values were properly added to the tree for Q4a
    def tree_in_order(self):
        tree_result = []
        if self.left:
            tree_result += self.left.tree_in_order()
        tree_result.append((self._value, self._data))
        if self.right:
            tree_result += self.right.tree_in_order()
        return tree_result
    
    #Q4b -------------------------------------------------------------------
    def __contains__(self, patient_id):
        if self._value == patient_id:
            return True
        elif self.left and patient_id < self._value:
            return patient_id in self.left
        elif self.right and patient_id > self._value:
            return patient_id in self.right
        else:
            return False
        
    #Q4c -------------------------------------------------------------------
    def has_data(self, patient_data):
        if self._data == patient_data:
            return True
        elif self.left and self.left.has_data(patient_data):
            return True
        elif self.right and self.right.has_data(patient_data):
            return True
        return False
        
#Q4a Testing -------------------------------------------------------------------
my_tree = Tree()
for patient_id, initials in [(24601, "JV"), (42, "DA"), (7, "JB"), (143, "FR"), (8675309, "JNY")]:
    my_tree.add(patient_id, initials)
print(my_tree.tree_in_order())

#Q4b Testing -------------------------------------------------------------------
print("24601 in my_tree:", 24601 in my_tree)
print("42 in my_tree:", 42 in my_tree)
print("7 in my_tree:", 7 in my_tree)
print("143 in my_tree:", 143 in my_tree)
print("8675309 in my_tree:", 8675309 in my_tree)
print("5 in my_tree:", 5 in my_tree)
print("1286 in my_tree:", 1286 in my_tree)
print("9989989 in my_tree:", 9989989 in my_tree)
print("-7 in my_tree:", -7 in my_tree)
print("4.2 in my_tree:", 4.2 in my_tree)

#Q4c Testing -------------------------------------------------------------------
print("Data = JV in my_tree:", my_tree.has_data('JV'))
print("Data = DA in my_tree:", my_tree.has_data('DA'))
print("Data = JB in my_tree:", my_tree.has_data('JB'))
print("Data = FR in my_tree:", my_tree.has_data('FR'))
print("Data = JNY in my_tree:", my_tree.has_data('JNY'))
print("Data = 42 in my_tree:", my_tree.has_data(42))
print("Data = 5 in my_tree:", my_tree.has_data(5))
print("Data = 182 in my_tree:", my_tree.has_data(182))
print("Data = HIJ in my_tree:", my_tree.has_data('HIJ'))
print("Data =  in my_tree:", my_tree.has_data(''))

#Q4d -------------------------------------------------------------------
def random_uppercase_string():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(3))

def time_plot(times, n_values, title, data_label):
    min_time = min(times)

    O_n = n_values
    O_n_squared = n_values ** 2
    O_log_n = np.log(n_values)
    O_n_log_n = n_values * np.log(n_values)

    O_n_scaled = O_n * (min_time / O_n[0])
    O_n_squared_scaled = O_n_squared * (min_time / O_n_squared[0])
    O_log_n_scaled = O_log_n * (min_time / O_log_n[0])
    O_n_log_n_scaled = O_n_log_n * (min_time / O_n_log_n[0])

    plt.loglog(n_values, times, label = data_label, color = "red")
    plt.loglog(n_values, O_n_scaled, label = 'Scaled O(n)', color='green', linestyle='--')
    plt.loglog(n_values, O_n_squared_scaled, label = 'Scaled O(n^2)', color='blue', linestyle='--')
    plt.loglog(n_values, O_log_n_scaled, label = 'Scaled O(logn)', color='purple', linestyle='--')
    plt.loglog(n_values, O_n_log_n_scaled, label = 'Scaled O(nlogn)', color='orange', linestyle='--')

    plt.xlabel('n')
    plt.ylabel('Time (seconds)')
    plt.title(title)
    plt.legend()
    plt.grid(True)

def setup_time(n_values):
    list_of_trees = []
    setup_time_list = []
    for n in tqdm(n_values, desc="Timing Setup"):
        random_value_list = random.sample(range(1, 2 * n + 1), n)
        random_string_list = [random_uppercase_string() for _ in range(n)]
        start = time.perf_counter()
        n_tree = Tree()
        for patient_id, initials in zip(random_value_list, random_string_list):
            n_tree.add(patient_id, initials)
        setup_time_list.append(time.perf_counter() - start)
        list_of_trees.append(n_tree)
        # print(n_tree.tree_in_order())
    time_plot(setup_time_list, n_values, "Time to Set Up Tree for Various Sizes n", "Time to Set Up Tree")
    plt.show()
    return list_of_trees

def contains_time(n_values, tree_list, searches):
    contains_time_list = []
    tree_index = 0
    for n in tqdm(n_values, desc="Timing __contains__"):
        start = time.perf_counter()
        for _ in range(searches):
            random_value = random.randint(1, 2 * n)
            random_value in tree_list[tree_index]
        contains_time_list.append(time.perf_counter() - start)
        tree_index += 1
    contains_graph_title = "Time to Perform " + str(searches) + " __contains__ Operations for Various Sizes n"
    time_plot(contains_time_list, n_values, contains_graph_title, "Time to Perform Value Searches")
    plt.show()
    return contains_time_list

def has_data(n_values, tree_list, searches, contains_time_list):
    has_data_time_list = []
    tree_index = 0
    for n in tqdm(n_values, desc="Timing has_data"):
        start = time.perf_counter()
        for _ in range(searches):
            random_data = random_uppercase_string()
            tree_list[tree_index].has_data(random_data)
        has_data_time_list.append(time.perf_counter() - start)
        tree_index += 1
    has_data_graph_title = "Time to Perform " + str(searches) + " has_data Operations for Various Sizes n"
    time_plot(has_data_time_list, n_values, has_data_graph_title, "Time to Perform Data Searches")
    #Adding __contains__ times to the graph
    plt.loglog(n_values, contains_time_list, label = "Time to Perform Value Searches", color = "pink")
    plt.legend()
    plt.show()
    
n_values = np.logspace(1, 6, num=20, dtype=int)

tree_list = setup_time(n_values)
contains_time_list = contains_time(n_values, tree_list, 10)
has_data(n_values, tree_list, 10, contains_time_list)

#Q4e -------------------------------------------------------------------
#Answer in README