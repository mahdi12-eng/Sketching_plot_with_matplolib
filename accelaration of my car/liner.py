from matplotlib import pyplot as plt

# time of travel
time = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

# speed during travel
speed_1 = [0, 20, 45, 60, 80, 90, 100, 110, 120, 115, 100, 80, 0]

# Graph of accelaration
plt.plot(time,speed_1)

# sistance my car traveled
distance= [0, 100, 200, 300, 400, 500]

#fuel burned during dravel
fuel_2 = [50, 42, 35, 28, 20, 12]

# graph of fuel consuming rate
plt.plot(distance,fuel_2)

# title of the graph
plt.title('Accelaration of my Car')

# name of horizantal axis
plt.xlabel('Time(Hr) & Distance')

# name of vertical axis
plt.ylabel('Speed(Km) & Fuel')

# Differentiation of graphs
plt.legend(['Accelaration','Fuel During Accelaration'])

# see accelaration file for graph
plt.show()