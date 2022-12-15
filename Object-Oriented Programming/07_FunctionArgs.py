'''
You may occasionally find it useful to make a keyword-only argument, that is, an argument
that must be supplied as a keyword argument. You can do that by placing a  *  before the
keyword-only arguments:
'''
def kw_only(x, y='defaultkw', *, a, b='only'):
    print(x, y, a, b)

try:
    kw_only('x')
except Exception as e:
    print(e)

try:
    kw_only('x', 'y', 'a')
except Exception as e:
    print(e)

try:
    kw_only('x', a='a', b='b')
except Exception as e:
    print(e)


'''
If we run this code, it outputs the number  8  first, but then it outputs the number  5  for the
call with no arguments. We had set the variable to the number  6 , as evidenced by the last
line of output, but when the function is called, the number  5  is printed; the default value
was calculated when the function was defined, not when it was called
'''
print('*'*20)

number = 5

def funky_function(number=number):
    print(number)

number=6
funky_function(8)
funky_function()
print(number)

'''
This is tricky with empty containers such as lists, sets, and dictionaries. For example, it is
common to ask calling code to supply a list that our function is going to manipulate, but the
list is optional. We'd like to make an empty list as a default argument. We can't do this; it
will create only one list, when the code is first constructed
'''
print('*'*20)

def hello(b=[]):
    b.append('a')
    print(b)

print(hello())
print(hello())

'''
Variable argument lists
'''
print('*'*20)

class Options:
    default_options = {
            'port': 21,
            'host': 'localhost',
            'username': None,
            'password': None,
            'debug': False,
            }
    def __init__(self, **kwargs):
        self.options = {**Options.default_options, **kwargs}
    def __getitem__(self, key):
        return self.options[key]

options = Options(username="dusty", password="drowssap", debug=True)
print(options['debug'])
print(options['port'])
print(options['username'])

'''
Unpacking arguments
'''
print('*'*20)

def show_args(arg1, arg2, arg3="THREE"):
    print(arg1, arg2, arg3)

some_args = range(3)
more_args = {
        "arg1": "ONE",
        "arg2": "TWO"}

print("Unpacking a sequence:", end=" ")
show_args(*some_args)
print("Unpacking a dict:", end=" ")
show_args(**more_args)
