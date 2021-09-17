print("Name: Kushagra Patidar\nScholar Number: 30665")
import numpy as np
taxi=np.genfromtxt("nyc_taxi.csv",delimiter=',')
(r,c)=taxi.shape
print("Taxi shape: ",(r,c))
print(type(taxi))
print(type(taxi.shape))