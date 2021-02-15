# columns
import csv
import random

#Słowniki

D1 = {'A': str(random.randint(0,2)),
      'B': str(random.randint(1,3)),
      'C': str(random.randint(2,4)),
      'D': str(random.randint(3,5))}


lista = [D1]

with open('kolumny.csv','w') as csvfile:
    nazwy = ['A','B','C','D']
    csvwriter = csv.DictWriter(csvfile, fieldnames=nazwy)
    csvwriter.writeheader()
    for n in lista:
        csvwriter.writerow(n)

with open('kolumny.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row[0])
