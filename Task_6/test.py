import csv
import numpy as np 
fi=open("yellow_trip_data.csv","r",encoding="utf8")
taxi_list=list(csv.reader(fi))

dic=dict()

for row in taxi_list[1:]:
    key=row[5]
    if row[5] not in dic.keys():
        dic[key]=1
    else:
        dic[key]+=1

key1,large1=0,0
key2,large2=0,0
key3,large3=0,0
for key,value in dic.items():
    if value>large1:
        key1,large1=key,value
    elif value>large2:
        key2,large2=key,value
    elif value>large3:
        key3,large3=key,value
print(key1,large1)
print(key2,large2)
print(key3,large3)







































