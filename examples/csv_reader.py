import csv
import re

regex1 = '"8.+"Y.+"F.'

with open('E:\\test_csv\\test_csv.csv', newline='') as csvfile:
     numbers = csv.reader(csvfile, delimiter=';', quotechar='|')
     for row in numbers:
        if re.findall(regex1, str(row)):
            print(row[2])
