"""Отработка главы 4 курса Python Crash Course"""

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
     print(f"{magician.title()}, that was a great trick!")

# Using range() function
for value in range(2, 5):
    print(value)

numbers = list(range(1, 10))
print(numbers)

numbers = list(range(1, 10, 3))
print(numbers)

# Simple statistic with a list of numbers
numbers = list(range(1, 10))
print(f'\nList: {numbers}')
print(f'min: {min(numbers)}')
print(f'max: {max(numbers)}')
print(f'sum: {sum(numbers)}')

# Generate list with loop
squares = [value**2 for value in range(1, 11)]
print(squares)

# Slices
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[-3:]) # last 3 elements

# Copy list
my_foods = ['pizza', 'falafel', 'carrot cake']
print(f'\nStart list: {my_foods}')
friend_foods1 = my_foods[:]
friend_foods2 = my_foods
my_foods[0] = 'ice_cream'
print(f'copy of list using [:]: {friend_foods1}')
print(f'copy of list : {friend_foods2}')

# Tuples
my_t = (3,) # tuple with one element
dimensions = (200, 50)
dimensions = (400, 100) # to change tuple we should redifine it