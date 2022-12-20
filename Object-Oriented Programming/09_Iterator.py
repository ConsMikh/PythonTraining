'''
The iterable is an object with elements that can be looped over.
Normally, these elements can be looped over multiple times, maybe even at the same time
or in overlapping code. The iterator, on the other hand, represents a specific location in that
iterable; some of the items have been consumed and some have not. Two different iterators
might be at different places in the list of words, but any one iterator can mark only one
place. Each time  next()  is called on the iterator, it returns another token from the iterable, in
order.
'''

class CapitalIterable:
    def __init__(self, string):
        self.string = string
    def __iter__(self):
        return CapitalIterator(self.string)


class CapitalIterator:
    def __init__(self, string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0
    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()
        word = self.words[self.index]
        self.index += 1
        return word
    def __iter__(self):
        return self

iterable = CapitalIterable('the quick brown fox jumps over the lazy dog')
iterator = iter(iterable)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
print('*'*20)

for i in iterable:
    print(i)