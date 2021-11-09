import pandas as pd
import matplotlib.pyplot as plt

happiness_ds = pd.read_csv('worldhappiness2015.csv')
happiness_ds = pd.DataFrame(happiness_ds)

# print(happiness_ds['Country'])

# happiness_ds = happiness_ds[:5]

happiness_ds['Happiness Score'].plot(kind='bar', title='Happiness Scores', ylim=(0,10))
plt.show()