import numpy as np
import csv
import os

def csv_to_matrix(file_path):
    m = np.loadtxt(file_path, delimiter= ',')
    matrix = []
    i = j = 0
    while (i< len(m)):
        while (j<len(m[i])):
            matrix.append(float(m[i][j]))
            j+=1
        i+=1
    return matrix

current_directory = os.path.dirname(os.path.abspath(__file__))
file  = str(input("Enter the name of the community graph csv file:\n"))
path = current_directory + "/" + file

print(csv_to_matrix(path))
