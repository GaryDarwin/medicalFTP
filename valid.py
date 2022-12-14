
import numpy as np
import csv
bad_data = {} #dictionary containing all issues of the file

#Check for empty values; if true, then find position of None values and record them
def empty_values_check(csv_matrix):
    if any(None in data for data in csv_matrix):
        missing_values = np.where(csv_matrix is None).tolist()
        bad_data['Missing Values'] = missing_values
        return print(f"Missing values:\n", missing_values)
    print("No missing values")

#Checking batch ids are all unique; if not, find position and record them

def batch_id_check(csv_matrix):
    batch_ids = csv_matrix[1:, 0]
    repeat_ids = []
    if len(set(batch_ids)) != len(batch_ids):
        for i in range(len(batch_ids)):
            for j in range(i + 1, len(batch_ids)):
                if batch_ids[i] == batch_ids[j]:
                    repeat_ids.append((batch_ids[i], i, j))
        bad_data['Repeat IDs'] = repeat_ids #Coordinates" of repeat batch id: (ID, column position1, column position2)
    return print(f"Repeat batch IDs:\n", repeat_ids)

#Check data is in range 0.000 - 9.900; if not, note value and location
def check_range(csv_matrix):
    for i in range(len(csv_matrix[1:, 0])):
        data_readings = csv_matrix[1:, -10:]
        out_of_range = []
        too_many_decimal = []

        for j in range(10):
            if data_readings[i, j] < 0.0 or data_readings[i, j] > 9.9:
                out_of_range.append((data_readings[i, j], i, j))
            if str(data_readings[i, j])[::-1].find('.') > 3:
                too_many_decimal.append((data_readings[i, j], i, j))
        if out_of_range != []:
            bad_data['Out of range'] = out_of_range
        if too_many_decimal != []:
            bad_data['Decimal Place Errors'] = too_many_decimal
        return print(f"Out of range:\n", out_of_range, f"\nDecimal Place Errors:\n", too_many_decimal)

def data_validation(fileName):
    file = open(fileName, 'r')
    csv_data = list(csv.reader(file))
    csv_matrix = np.array([np.array(row) for row in csv_data])
    empty_values_check(csv_matrix)
    batch_id_check(csv_matrix)
    check_range(csv_matrix)
    return print(bad_data)
