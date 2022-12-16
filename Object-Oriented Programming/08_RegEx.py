# pylint: disable = pointless-string-statement

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

'''
The period character, when used in a
regular expression pattern, can match any single character. Using a period in the string
means you don't care what the character is, just that there is a character there
'''
pattern = "hel.o world"
research(pattern)
research(pattern, 'helpo world')

pattern = "helo world"
research(pattern, 'hello worl')
print('*'*20)

'''
We can put a set of characters inside square brackets to match any one of those characters. 
So, if we encounter the string  [abc] in a regular expression pattern, we know that those five
(including the two square brackets) characters will only match one character in the string
being searched, and further, that this one character will be either an  a , a  b , or a  c .
'''
pattern = "hel[lp]o world"
research(pattern)
research(pattern, 'helpo world')
research(pattern, 'helPo world')

pattern = "hello [a-z] world"
research(pattern, 'hello   world')

pattern = "hello [a-z] world"
research(pattern, 'hello b world')

pattern = "hello [a-zA-Z] world"
research(pattern, 'hello B world')

pattern = "hello [a-zA-Z0-9] world"
research(pattern,'hello 2 world')

print('*'*20)

'''
Backslash escape sequence is used for a variety of special characters in regular
expressions. You can use  \[  to insert a square bracket without starting a character class,
and  \(  to insert a parenthesis, which we'll later see is also a special character.
More interestingly, we can also use the escape symbol followed by a character to represent
special characters such as newlines ( \n ) and tabs ( \t ). Further, some character classes can
be represented more succinctly using escape strings:  \s  represents whitespace
characters;  \w  represents letters, numbers, and underscore; and  \d  represents a digit
'''

pattern = "0\.[0-9][0-9]"
research(pattern, '0.05')
research(pattern, '005')
research(pattern, '0,05')

pattern = "\(abc\]"
research(pattern, '(abc]')
pattern = "\s\d\w"
research(pattern, ' 1a')
research(pattern, '\t5n')
research(pattern, '5n')

print('*'*20)

'''
The  *  character in the pattern says that the previous pattern (the  l  character) is optional,
and if present, can be repeated as many times as possible to match the pattern. The rest of
the characters ( h ,  e , and  o ) have to appear exactly once

If we combine the asterisk with patterns that match multiple characters. So,  .* , for example,
will match any string, whereas  [a-z]*  matches any collection of lowercase words,
including the empty string
'''
pattern = "hel*o"
research(pattern, 'hello')
research(pattern, 'heo')
research(pattern, 'helllllo')

pattern = "[A-Z][a-z]* [a-z]*\."
research(pattern, 'A string.')
research(pattern, 'No .')

pattern = "[a-z]*.*"
research(pattern, '')

print('*'*20)
'''
The plus ( + ) sign in a pattern behaves similarly to an asterisk; it states that the previous
pattern can be repeated one or more times, but, unlike the asterisk, is not optional. The
question mark ( ? ) ensures a pattern shows up exactly zero or one times, but not more. Let's
explore some of these by playing with numbers (remember that  \d  matches the same
character class as  [0-9]
'''
pattern = "\d+\.\d+"
research(pattern, '0.4')
research(pattern, '1.002')
research(pattern, '1.')

pattern = "\d?\d%"
research(pattern, '1%')
research(pattern, '99%')
research(pattern, '999%')

print('*'*20)

'''
Enclosing any set of patterns in parentheses
allows them to be treated as a single pattern when applying repetition operations.
'''
pattern = "abc{3}"
research(pattern, 'abccc')
pattern = "(abc){3}"
research(pattern, 'abccc')
research(pattern, 'abcabcabc')

pattern = "[A-Z][a-z]*( [a-z]+)*\.$"
research(pattern, 'Eat.')
research(pattern, 'Eat more good food.')
research(pattern, 'VERY good meal.')
research(pattern, 'Very Good meal.')
print('*'*20)

'''
We want to access the domain name (after the  @  sign) so we can connect to that
address. This is done easily by wrapping that part of the pattern in parentheses and calling
the  groups()  method on the object returned by match
'''

pattern = "^[a-zA-Z.]+@([a-z.]*\.[a-z]+)$"
research(pattern, "some.user@example.com")
research(pattern, "some.user@example..com")

search_string = "some.user@example.com"
match = re.match(pattern, search_string)
if match:
    domain = match.groups()[0]
    print(domain)
print('*'*20)

'''
If there are no groups in the pattern,  re.findall  will return a list of strings,
where each value is a complete substring from the source string that matches the
pattern

If there is exactly one group in the pattern,  re.findall  will return a list of
strings where each value is the contents of that group

If there are multiple groups in the pattern,  re.findall  will return a list of tuples
where each tuple contains a value from a matching group, in order
'''
print(re.findall('a.', 'abacadefagah'))
print(re.findall('a(.)', 'abacadefagah'))
print(re.findall('(a)(.)', 'abacadefagah'))
print(re.findall('((a)(.))', 'abacadefagah'))

print('*'*20)

DIRECTIVE_RE = re.compile(
    r'/\*\*\s*(include|variable|loopover|endloop|loopvar)\s*([^ *]*)\s*\*\*/')

search = """
/** include header.html **/
<h1>This is the title of the front page</h1>
/** include menu.html **/
<p>My name is /** variable name **/.
This is the content of my front page. It goes below the menu.</p>
<table>
<tr><th>Favourite Books</th></tr>
/** loopover book_list **/
<tr><td>/** loopvar **/</td></tr>
/** endloop **/
</table>
/** include footer.html **/
Copyright &copy; Today
"""
match = DIRECTIVE_RE.findall(search)
print(match)


