# utils/csv_utils.py

import csv

def read_csv(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        return list(reader)

def write_csv(filepath, data, mode='w'):
    with open(filepath, mode, newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
