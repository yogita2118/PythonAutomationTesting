import csv

with open('TestData.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for col in reader:
        print(col[0],col[1],sep="|")
