import csv

with open("../csv/employees.csv", "r", newline="") as file:
    reader = csv.reader(file)
    employees = list(reader)

headers = employees[0]
first_name_index = headers.index("first_name")
last_name_index = headers.index("last_name")

full_names = [
    employee[first_name_index] + " " + employee[last_name_index]
    for employee in employees[1:]
]

print(full_names)

names_with_e = [
    name for name in full_names
    if "e" in name
]

print(names_with_e)