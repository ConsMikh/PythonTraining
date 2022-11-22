'''Отработка 8 главы Python Crash Course'''

# Default values and Keyword Arguments
def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
describe_pet(animal_type = 'hamster', pet_name='billie')
describe_pet('dillie', 'duck')

# Send copy of list in function to keep original list
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print (f'1. Original list: {unprinted_designs}')
print (f'\n')

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models) # Use slice
show_completed_models(completed_models)
print (f'2. Original list: {unprinted_designs}')

# Passing an Arbitrary Number of Arguments
# The asterisk (*) in the parameter name *toppings tells Python to make an 
# empty tuple called toppings and pack whatever values it receives into this 
# tuple
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:") 
    for topping in toppings: 
        print(f"- {topping}") 
        
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print (f'\n')

# Using Arbitrary Keyword Arguments
# The double asterisks (**) before the parameter **user_info cause Python to create 
# an empty dictionary called user_info and pack whatever name-value pairs 
# it receives into this dictionary
#  **kwargs used to collect non-specific keyword arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
print (f'\n')

# Importing an Entire Module with alias
print (f'\nImport module Ch08_module')

import Ch08_module as mod  # Or from Ch08_module import make_pizza_2 as mp for specific function with alias

mod.make_pizza_2(16, 'pepperoni')
mod.make_pizza_2(12, 'mushrooms', 'green peppers', 'extra cheese')

print (f'\nImport all function in the module Ch08_module')

from Ch08_module import * # Now we can use function without prefix
make_pizza_2(16, 'pepperoni')
make_pizza_2(12, 'mushrooms', 'green peppers', 'extra cheese')

# Python Docstrings
def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2
print(square.__doc__)
