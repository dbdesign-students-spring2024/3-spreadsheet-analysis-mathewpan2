# place your code to clean up the data file below.
import csv
import os

read_path = os.path.join('data', 'data.csv')
write_path = os.path.join('data', 'cleaned_data.csv')

columns_to_delete = []
first_row = True
with open(write_path, 'w') as write:
    writer = csv.writer(write)
    with open(read_path, 'r') as read:
        reader = csv.reader(read)
        for row in reader:
            if first_row:
                for index, category in enumerate(row):
                    if category.strip() == 'School DBN' or category.strip() == 'Number Scoring CR' or category.strip() == 'Demographic Variable' or category.strip() == 'Percent Scoring CR':
                        columns_to_delete.append(index)
            row  = [col for index, col in enumerate(row) if index not in columns_to_delete]
            if row[5] != 'All Students' and not first_row:
                continue
            if first_row:
                first_row = False
            for item in row:
                if item == 's':
                    row[row.index(item)] = ''
            writer.writerow(row)