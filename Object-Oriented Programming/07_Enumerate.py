'''
The  enumerate  function creates a sequence of tuples, 
where the first object in each tuple is the index 
and the second is the original item.
'''

import sys
filename = sys.argv[1]
with open(filename) as file:
    for index, line in enumerate(file):
        print(f"{index+1}: {line}", end="")