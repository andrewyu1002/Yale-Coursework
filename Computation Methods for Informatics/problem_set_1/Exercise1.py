import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from tqdm import tqdm

#Q1a -------------------------------------------------------------------

tree = ET.parse("Computation Methods for Informatics/problem_set_1/hw1-patients.xml")
root = tree.getroot()

ages = []
for patient in root.findall("patients/patient"):
    ages.append(float(patient.get("age")))

# print(ages)

plt.hist(ages, bins = 100, color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Patient Age Distribution Histogram')
plt.show()

duplicates = {}
for age in tqdm(ages, desc="Checking for duplicates"):
    if age in duplicates:
        duplicates[age] += 1
    else:
        duplicates[age] = 1

duplicate_ages = {age: count for age, count in duplicates.items() if count > 1}

if duplicate_ages:
    print("The following ages belong to multiple patients")
    for age, count in duplicate_ages.items():
        print("Age:", age, ", Count:", count)
else:
    print("No ages appear more than once among the list of patients")

#Q1b --------------------------------------------------------------------
    
gender = {}
for patient in root.findall("patients/patient"):
    if patient.get("gender") not in gender:
        gender[patient.get("gender")] = 1
    else:
        gender[patient.get("gender")] += 1

plt.bar(gender.keys(), gender.values(), color='skyblue')
for i, gender_count in enumerate(gender.values()):
    plt.text(i, gender_count + 0.5, str(gender_count), ha='center', va='bottom')
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.title('Patient Gender Distribution Histogram')
plt.show()

#Q1c --------------------------------------------------------------------

sorted_patients = sorted(root.findall("patients/patient"), key = lambda patient: float(patient.get("age")))
print("The oldest patient is", sorted_patients[-1].get("name"), "at", sorted_patients[-1].get("age"), "years old")

#Q1d --------------------------------------------------------------------
#Answer in README

#Q1e --------------------------------------------------------------------

def binary_search(patients, target_age):
    low_bound = 0
    high_bound = len(patients) - 1
    while low_bound <= high_bound:
        mid = (low_bound + high_bound) // 2
        mid_age = float(patients[mid].get("age"))
        if mid_age < target_age:
            low_bound = mid + 1
        elif mid_age > target_age:
            high_bound = mid - 1
        else:
            return patients[mid]
    return None

specific_age_patient = binary_search(sorted_patients, 41.5)

print("The patient that is exactly 41.5 years old is", specific_age_patient.get("name"))

#Q1f --------------------------------------------------------------------

age_index = sorted_patients.index(specific_age_patient)
at_least_age = len(sorted_patients) - age_index
print("There are", at_least_age, "number of patients who are at least 41.5 years old")

#Q1g --------------------------------------------------------------------

def left_boundary(patients, target_age):
    low_bound = 0
    high_bound = len(patients) - 1
    while low_bound < high_bound:
        mid = (low_bound + high_bound) // 2
        mid_age = float(patients[mid].get("age"))
        if mid_age < target_age:
            low_bound = mid + 1
        else:
            high_bound = mid
    return low_bound

def age_range(patients, low_age, high_age):
    lower_age_bound = left_boundary(patients, low_age)
    upper_age_bound = left_boundary(patients, high_age)
    index_range = upper_age_bound - lower_age_bound
    print("There are", index_range, "patients between ages", low_age, "and", high_age)

# age_range(sorted_patients, 43, 44)
# age_range(sorted_patients, 56.5, 56.51)
# age_range(sorted_patients, 2, 2.5)
# age_range(sorted_patients, 3, 7)
age_range(sorted_patients, 79, 81)

#Q1h --------------------------------------------------------------------

# One-time setup
male_prefix = [0] * (len(sorted_patients) + 1)
for i, patient in enumerate(sorted_patients):
    male_prefix[i + 1] = male_prefix[i] + (1 if patient.get("gender") == "male" else 0)

def age_gender_range(patients, low_age, high_age, gender, prefix):
    left_bound = left_boundary(patients, low_age)
    right_bound = left_boundary(patients, high_age)
    count = prefix[right_bound] - prefix[left_bound]
    print("There are", count, gender, "patients between ages", low_age, "and", high_age)

# age_gender_range(sorted_patients, 43, 44, "male", male_prefix)
# age_gender_range(sorted_patients, 56.5, 56.51, "male", male_prefix)
# age_gender_range(sorted_patients, 2, 2.5, "male", male_prefix)
# age_gender_range(sorted_patients, 3, 7, "male", male_prefix)
age_gender_range(sorted_patients, 79, 81, "male", male_prefix)