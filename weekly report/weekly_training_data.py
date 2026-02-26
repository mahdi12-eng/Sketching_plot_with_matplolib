from matplotlib import pyplot as plt
x = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
y = [5500,8200,6800,10500,9200,14000,15500]
plt.grid(c = "#39fc6a",ls = ":")
plt.plot(x,y,marker = 'o', ls = '--',c ="#fc3232" )
plt.title('Fitness Progress',loc ='center')
plt.xlabel('Day')
plt.ylabel('Steps')
plt.legend()
plt.show()
