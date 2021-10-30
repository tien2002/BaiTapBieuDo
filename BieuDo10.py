import matplotlib.pyplot as plt
import numpy as np

height = np.array([167,170,150,175,176,174,153])

weight = np.array(([86, 87, 85, 84, 90, 73, 70]))

plt.xlim(140,200)
plt.ylim(60,100)
plt.scatter(height,weight)
plt.title("Scatter Plot")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()