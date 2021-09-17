print("Name: Kushagra Patidar\nScholar Number: 30665")
import csv
import numpy as np 
f=open("nyc_taxi.csv","r",encoding="utf8")
taxi_list=list(csv.reader(f))

taxi_list=taxi_list[1:]

converted_taxi_list=[]
for row in taxi_list:
    converted_row=[]
    for item in row:
        if item=='':                         #Cleaning the data
            converted_row.append(0.00)   #Otherwise there will be an index error
        else:
            converted_row.append(format(float(item),".2f"))
    converted_taxi_list.append(converted_row)

taxi=np.array(converted_taxi_list)
taxi_modified=taxi.copy()
#taxi_modified[1066,5]=1
taxi_modified[:,0]=16
print(taxi_modified)
#taxi_modified[551,7]=taxi_modified[550,7]=(taxi[:,7].sum()-taxi_modified[550,7]-taxi_modified[551,7])/(len(taxi_modified)-1)