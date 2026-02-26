from matplotlib import pyplot as plt
import numpy as np
y_axis = np.array([1,2,3,4,5,6,7,4])
plt.plot(y_axis,'o',c="#fc04b2",mfc ='none',mec ='yellow',ms = 20,mew = 2,linewidth =5,marker ='*' )
plt.show()