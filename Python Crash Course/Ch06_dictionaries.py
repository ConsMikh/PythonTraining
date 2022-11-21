''' Отработка 6 главы курса Python Crash Course'''

# Remove key-value
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# Return default value if requested key doesn't exist
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# Looping Through All Key-Value Pairs
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# Looping Through All the Keys in a Dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in favorite_languages.keys():
    print(name.title())

# Looping Through sorted key list
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Looping Through All Values in a Dictionary
print("The following languages have been mentioned:")
# Create set of unique elements
for language in set(favorite_languages.values()): 
    print(language.title())