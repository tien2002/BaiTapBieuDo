import matplotlib.pyplot as plt
import numpy as np

plt.subplot(1,2,1)
plt.plot([1,2,3,4],[1,4,9,16],"go")
plt.title("Bieu Do 1")

plt.subplot(1,2,2)
plt.plot([1,2,3,4],[1,4,9,16],"go")
plt.title("Bieu Do 2")

plt.suptitle("Bieu Do")
plt.show()