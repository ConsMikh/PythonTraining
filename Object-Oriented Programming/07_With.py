'''
This code constructs a string of 15 random characters. It appends these to a  StringJoiner
using the  append  method it inherited from  list . When the  with  statement goes out of
scope (back to the outer indentation level), the  __exit__  method is called, and the  result
attribute becomes available on the joiner object. We then print this value to see a random
string.
'''

class StringJoiner(list):
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, tb):
        self.result = "".join(self)

import random, string
with StringJoiner() as joiner:
    for i in range(15):
        joiner.append(random.choice(string.ascii_letters))
print(joiner.result)