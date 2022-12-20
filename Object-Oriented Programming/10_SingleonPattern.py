'''
The basic idea behind the singleton pattern is to allow exactly one instance of a certain
object to exist.
'''

class OneOnly:
    _singleton = None
    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(OneOnly, cls).__new__(cls, *args, **kwargs)
        return cls._singleton

o1 = OneOnly()
o2 = OneOnly()
print(o1 == o2)
print(o1)
print(o2)

