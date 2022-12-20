
input_strings = ["1", "5", "28", "131", "3"]

output_integers = []
for num in input_strings:
    output_integers.append(int(num))

# List comprehensions
output_integers = [int(num) for num in input_strings]
print(output_integers)

output_integers = [int(num) for num in input_strings if len(num) < 3]
print(output_integers)

print('*'*20)

'''
Any iterable can be the input to a list comprehension. In other words, anything we can
wrap in a  for  loop can also be placed inside a comprehension. For example, text files are
iterable; each call to  __next__  on the file's iterator will return one line of the file. We could 
load a tab-delimited file where the first line is a header row into a dictionary using the  zip
function
'''
import sys
filename = sys.argv[1]
with open(filename) as file:
    header = file.readline().strip().split("\t")
    contacts = [
        dict(zip(header, line.strip().split("\t")))
        for line in file
        ]
for contact in contacts:
    print("email: {email} -- {last}, {first}".format(**contact))