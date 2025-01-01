import csv
with open('file_programs/csv1.csv','r') as csv1:
    reader=csv.reader(csv1)
    header=next(reader)
    rowslist=list(reader)
    for i in range (0,len(header)):
        print(header[i])
        for row in rowslist:
            print(row[i])
            