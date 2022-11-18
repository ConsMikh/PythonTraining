"""Отработка 3 главы Python Crash Course"""

# it’s a good idea to make the name of your list plural
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# append element to list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

# insert element into list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# removing element from list
print('\nRemoving element usind del')
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

print('\nRemoving element usind value of item')
motorcycles = ['honda', 'yamaha', 'suzuki', 'yamaha']
motorcycles.remove('yamaha')
print(motorcycles)

# removing  element using pop() method
print('\nRemoving element using pop() method')
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop() # remove last element
print(motorcycles)
print(popped_motorcycle)
first_owned = motorcycles.pop(0) # remove element with index 0
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Sort list
print('\nSort list')
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # sort() changes the order of the list permanently
print(cars)
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the sorted list with sorted()")
print(sorted(cars))
print("Print list in reverse order")
cars.reverse()
print(cars)

# Finding lenght of list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f'\nLenght of list: {cars} is {len(cars)}')