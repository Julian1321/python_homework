import csv

def read_employees():
    employees_dict = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)

            for index, row in enumerate(reader):
                if index == 0:
                    employees_dict["fields"] = row
                else:
                    rows.append(row)
            
            employees_dict["rows"] = rows
    
    except Exception as e:
        print(f"An exception occurred: {type(e).__name__}: {e}")
        raise

    return employees_dict

employees = read_employees()
print(employees)


def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]

def employee_find(employee_id):

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))

    return matches

def employee_find_2(employee_id):
    matches = list(filter(
        lambda row: int(row[employee_id_column]) == employee_id,
        employees["rows"]
    ))
    return matches

def sort_by_last_name():
    last_name_column = column_index("last_name")

    employees["rows"].sort(
        key=lambda row: row[last_name_column]
    )

    return employees["rows"]

sort_by_last_name()
print(employees)

def employee_dict(row):
    result = {}

    for index, field in enumerate(employees["fields"]):
        if field != "employee_id":
            result[field] = row[index]
    
    return result

print(employee_dict(employees["rows"][0]))

def all_employees_dict():
    result = {}

    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        result[employee_id] = employee_dict(row)

    return result

print(all_employees_dict())

import os

def get_this_value():
    return os.environ.get("THISVALUE")

import custom_module

def set_that_secret(value):
    custom_module.secret = value

def read_minutes():

    def read_file(filename):
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            all_rows = list(reader)

        return {
            "fields": all_rows[0],
            "rows": [tuple(row) for row in all_rows[1:]]
        }

    minutes1 = read_file("../csv/minutes1.csv")
    minutes2 = read_file("../csv/minutes2.csv")

    return minutes1, minutes2


minutes1, minutes2 = read_minutes()

print(minutes1)
print(minutes2)

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

    return set1.union(set2)

minutes_set = create_minutes_set()

from datetime import datetime

def create_minutes_list():
    records = list(minutes_set)

    converted = list(map(
        lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
        records
    ))

    return converted

minutes_list = create_minutes_list()
print(minutes_list)

def write_sorted_list():
    minutes_list.sort(key=lambda row: row[1])

    sorted_list = list(map(
        lambda x: (
            x[0],
            datetime.strftime(x[1], "%B %d, %Y")

        ),
        minutes_list
    ))

    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(sorted_list)
    
    return sorted_list

write_sorted_list()