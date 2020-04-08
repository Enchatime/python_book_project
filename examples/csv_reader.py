import csv

with open('E:\csv_files\test.csv', newline='') as csvfile:
     numbers = csv.reader(csvfile, delimiter=';', quotechar='|')
     for row in numbers:
         print(', '.join(row))
