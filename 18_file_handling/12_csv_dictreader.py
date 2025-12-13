"""
reading csv file using csv module - DIctReader
"""
import csv
with open('./files/csv_example.csv') as f:
    csv_dict_reader = csv.DictReader(f)
    line_count = 0
    for row in csv_dict_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        print(
            f'\t{row["Name"]} is a teachers. He lives in {row["City"]}, {row["Country"]}.')
        line_count += 1
    print(f'Number of lines:  {line_count}')