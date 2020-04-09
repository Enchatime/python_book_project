import csv
import re

regex1 = '"8.'
regex2 = '"Y'
regex3 = '"P'

with open('E:\test_csv\test_csv.csv', newline='') as csvfile:
     numbers = csv.reader(csvfile, delimiter=';', quotechar='|')
     for row in numbers:
        if re.match(regex1, str(row[2])):
            if re.match(regex2, str(row[3])):
                if re.match(regex3, str(row[4])):
                    print(row)
