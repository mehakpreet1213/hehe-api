import csv
import pandas as pd

file1 = "dwarf_stars.csv"
file2 = "unit_converted_stars.csv"
d1=[]
d2=[]

with open(file1, 'r', encoding='utf8') as f:
    csv_reader=csv.reader(f)
    for i in csv_reader:
        d1.appned(i)

with open (file2,'r', encoding='utf8') as f:
    csv_reader=csv.reader(f)    
    for i in csv_reader:
        d2.append(i)

h1= d1[0]
h2= d2=[0]

data_d1= d1[1:]
data_d2= d2[1:]

h=h1+h2

data=[]
for i in data_d1:
    data.append(i)
    
for j in data_d2:
    data.append(j)

with open("total_stars.csv",'w',encoding='utf8') as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(h)
    csv_writer.writerows(data)


