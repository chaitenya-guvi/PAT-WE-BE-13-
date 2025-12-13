"""
Program to write contenat to csv file

"""
import csv
with open('./files/csv_write_example.csv', mode='w', newline='') as f:
    csv_writer = csv.writer(f, delimiter=',')
    # writing the header
    csv_writer.writerow(['Name', 'Profession', 'City'])
    # writing multiple rows
    csv_writer.writerows([
        ['Alice', 'Engineer', 'New York'],
        ['Bob', 'Doctor', 'Los Angeles'],
        ['Charlie', 'Artist', 'Chicago']
    ])