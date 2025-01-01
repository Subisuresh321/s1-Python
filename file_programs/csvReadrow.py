import csv
with open('file_programs/csv1.csv','r') as csv1:
    reader=csv.reader(csv1)
    for row in reader:
        print(row)
    