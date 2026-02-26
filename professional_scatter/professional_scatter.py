from matplotlib import pyplot as plt
import numpy as np
x = np.random.randint(100,size =(100))
y = np.random.randint(100,size =(100))
color = np.random.randint(100,size =(100))
size = 20 * np.random.randint(100,size =(100))
plt.scatter(x,y, cmap='nipy_spectral',alpha=1,s = size,c=color)
plt.title("Hu.w Siwa'Mahdi'")
plt.colorbar()
plt.legend()
plt.show()