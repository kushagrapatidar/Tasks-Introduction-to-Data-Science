import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

happiness_ds = pd.read_csv('2015.csv')
happiness_ds = pd.DataFrame(happiness_ds)

mean_happiness = {}
regions = happiness_ds['Region'].unique()
# print(regions)

for r in regions:
    region_group = happiness_ds[happiness_ds['Region']==r] 
    region_group_mean = region_group['Happiness Score'].mean()
    mean_happiness[r] = region_group_mean

print(mean_happiness)