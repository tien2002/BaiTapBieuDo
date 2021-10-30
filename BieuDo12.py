import matplotlib.pyplot as plt
import numpy as np

height = np.array([167,170,150,175,176,174,153])

weight = np.array(([86, 87, 85, 84, 90, 73, 70]))

ax = plt.axes(projection='3d')
ax.plot3D(height, weight)
ax.set_xlabel("Height")
ax.set_ylabel("Weight")
plt.show()
