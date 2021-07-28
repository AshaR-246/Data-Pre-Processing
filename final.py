import csv
from typing import final

data1=[]
data2=[]
with open("data1.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data1.append(row)
with open("data2.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data2.append(row)
headers_1=data1[0]
planet_data_1=data1[1:]
headers_2=data2[0]
planet_data_2=data2[1:]
headers=headers_1+headers_2
planet_data=[]
for index, data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index]+planet_data_2[index])

with open ("final.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerows(headers)
    csvwriter.writerows(planet_data)
