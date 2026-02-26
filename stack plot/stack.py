from matplotlib import pyplot as plt 
plt.style.use('fivethirtyeight')

minutes = [1,2,3,4,5,6,7,8,9]
player1 = [8,6,5,5,4,2,1,1,0]
player2 = [0,1,2,2,2,4,4,4,4]
player3 = [0,1,1,1,2,2,3,3,4]
labels=['player1','player2','player3']
colors = ['green','red','blue']
plt.stackplot(minutes,player1,player2,player3,colors=colors, labels=labels )
plt.title('My Awesome Stack Plot')
plt.xlabel('minutes')
plt.ylabel('players')
plt.tight_layout()
plt.legend(loc = (0.01,0.0000))
plt.show()