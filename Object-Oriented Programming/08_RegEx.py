import sys
import re

def research(pattern, search_string = 'hello world'):
    match = re.match(pattern, search_string)

    if match:
        template = "'{}' matches pattern '{}'"
    else:
        template = "'{}' does not match pattern '{}'"

    print(template.format(search_string, pattern))

pattern = "ello world"
research(pattern)
print('*'*20)

'''
If you need control over whether items happen at the beginning or end of a line (or if there
are no newlines in the string, or at the beginning and end of the string), you can use the  ^
and  $  characters to represent the start and end of the string respectively. If you want a
pattern to match an entire string, it's a good idea to include both of these
'''
pattern = "^hello world$"
research(pattern)
print('*'*20)

pattern = "^hello world$"
research(pattern, 'hello worl')
print('*'*20)

