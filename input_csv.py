import csv
import os
import numpy as np

def input_csv(file_name: csv):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        data = []
        for idx, row in enumerate(reader):
            processed_row = []
            for value in row:
                processed_row.append(value)
            data.append(processed_row)
    total_data = np.array(data)

current_directory = os.path.dirname(os.path.abspath(__file__))

foo=current_directory + "/"  + str(input("Enter the name of the community graph csv file:\n"))

print(input_csv(foo))
