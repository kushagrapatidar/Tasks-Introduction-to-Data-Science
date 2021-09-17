#Task_3.e
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

taxi=np.array(converted_taxi_list)
row_0=taxi[0]
row_391_to_500=taxi[391:501]
row_21_column_5=taxi[21,5]