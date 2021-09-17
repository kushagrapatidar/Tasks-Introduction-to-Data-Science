#Task_3.g
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
trip_mph=3600*taxi[:,7]/taxi[:,8]
print(trip_mph)
mph_min=trip_mph.min()
print(mph_min)