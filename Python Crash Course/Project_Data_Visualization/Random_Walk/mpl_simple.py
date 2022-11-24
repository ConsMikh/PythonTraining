import matplotlib.pyplot as plt

input_values = range(1,1001)
squares = [i**2 for i in input_values ]
cubes = [i**3 for i in input_values ]


plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()
ax.plot(input_values, squares)
ax.scatter(input_values, squares, c=squares,  cmap=plt.cm.Blues, s=10)

# The axis() method requires four values: the minimum and maximum values for 
# the x-axis and the y-axis.
# ax.axis([0, 1100, 0, 1100000])

plt.show()