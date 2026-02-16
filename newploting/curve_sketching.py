from matplotlib import pyplot as plt

x = [0,1,2,3,4,5,6,7,8]
y= [0,1,4,9,16,25,36,49,64]
plt.plot(x,y, 'k--' ,label='All Devs')
y1= [0,1,2,3,4,5,6,7,8]
plt.plot(x,y1,'k--', label='python')
plt.xlabel('variable')
plt.ylabel('function')
plt.title('Quaderatic function')
plt.show()