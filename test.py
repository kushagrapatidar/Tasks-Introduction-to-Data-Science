import matplotlib.pyplot as plt
import numpy as np
month_number=[1,2,3,4,5,6,7]
new_deaths=[213,2729,37718,184064,143119,136073,165003]
plt.title('New Reported Deaths By Month(Globally)')
plt.xlabel('Month Number')
plt.ylabel('Number of Deaths')
plt.plot(month_number,new_deaths)
new_deaths=np.array(new_deaths)
new_deaths=new_deaths.sum()-new_deaths
plt.plot(month_number,new_deaths)
plt.show()