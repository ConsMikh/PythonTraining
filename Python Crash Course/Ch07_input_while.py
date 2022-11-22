'''Отработка 7 главы Python Crash Course'''

# Input string. It's always string. To input number use int()
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

age = input("How old are you? ")
age = int(age)
if age >= 18:
    print(f'{age} >= 18')
else:
    print(f'{age} < 18')

# Using break to exit a while loop. Break make exit  loop immediately without running any remaining code
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# Using continue in a loop.  Use the continue statement to return to the beginning of the 
# loop based on the result of a conditional test
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)