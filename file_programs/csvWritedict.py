import csv
dict1={"Name":"Subi","age":21,"branch":"MCA"
}
fieldnames=dict1.keys()
with open("file_programs/csv2.csv","a") as csv2:
    writer=csv.DictWriter(csv2,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(dict1)