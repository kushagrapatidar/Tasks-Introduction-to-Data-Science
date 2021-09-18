print("Name: Kushagra Patidar\nScholar Number: 30665")
import csv
import numpy as np 
# import nyc_taxi.csv as a list of lists
f=open("yellow_trip_data.csv","r",encoding="utf8")
taxi_list=list(csv.reader(f))
# remove the header row
taxi_list=taxi_list[1:]
# convert all values to floats
converted_taxi_list=[]
for row in taxi_list:
    converted_row=[]
    for item in row:
        if item=='':                         #Cleaning the data
            converted_row.append(0.00)   #Otherwise there will be an index error
        else:
            converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

data_ndarray=np.array(converted_taxi_list)
taxi = data_ndarray