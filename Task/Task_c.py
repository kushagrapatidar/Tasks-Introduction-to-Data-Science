#Task_3.c
import csv
import numpy as np 
f=open("nyc_taxi.csv","r",encoding="utf8")
taxi_list=list(csv.reader(f))

taxi_list=taxi_list[1:]

converted_taxi_list=[]
for row in taxi_list:
    converted_row=[]
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

data_ndarray=np.array(converted_taxi_list)
print(data_ndarray)