print("Name: Kushagra Patidar\nScholar Number: 30665")
import csv
import numpy as np 
fi=open("yellow_trip_data.csv","r",encoding="utf8")
taxi_list=list(csv.reader(fi))

fo=open("taxi_modified.csv","w",encoding="utf8")
writer=csv.writer(fo)

taxi_list[0].append("dropped_airport")

writer.writerow(taxi_list[0])

for row in taxi_list[1:]:
    converted_row=[]
    for item in row:
        if item=='':                         #Cleaning the data
            converted_row.append(0.00)   #Otherwise there will be an index error
        else:
            converted_row.append(float(item))
    if converted_row[5]==2 or converted_row[5]==3 or converted_row[5]==5:
        converted_row.append(1)
    else:
        converted_row.append(0)
    writer.writerow(converted_row)

