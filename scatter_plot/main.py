from matplotlib import pyplot as plt 
plt.figure(figsize=(18,12))
x = [1,2,3,4]
y = [1,4,9,16]

x2 = [1,2,3,4]
y2= [1,2,3,4]

plt.scatter(x , y, label='y = x^2', color = 'g')
plt.plot(x,y)
plt.scatter(x2 , y2, label='y=x', color = 'r')
plt.plot(x2,y2)
x3 = [4,4,4,4,4,4,4,4,4,4,4,4,4]
y3 =[4,5,6,7,8,9,10,11,12,13,14,15,16]
plt.plot(x3,y3, label = 'x= 4', color = 'b')
x4 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
y4= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
plt.scatter(x4,y4, label='x=1', color = 'y')
plt.plot(x4,y4)
plt.yticks(range(1,17,1))
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()
