# pylint: disable = pointless-string-statement

subtotal = 12.32
tax = subtotal * 0.07
total = subtotal + tax
print(
    "Sub: ${0} Tax: ${1} Total: ${total}".format(
        subtotal, tax, total=total
    )
)

print('*'*20)
'''
The  0.2f  format specifier after the colons basically says the following, from left to right:
0 : for values lower than one, make sure a zero is displayed on the left-hand of the
decimal point
. : show a decimal point
2 : show two places after the decimal
f : format the input value as a float
'''
print(
    "Sub: ${0:0.2f} Tax: ${1:0.2f} "
    "Total: ${total:0.2f}".format(subtotal, tax, total=total)
)
print('*'*20)

'''
The first variable is a string that is formatted with
{product:10s} . This one is easier to read from right to left:
    s  means it is a string variable.
    10  means it should take up 10 characters. By default, with strings, if the string is
shorter than the specified number of characters, it appends spaces to the right-
hand side of the string to make it long enough (beware, however: if the original
string is too long, it won't be truncated!).
    product: , of course, is the name of the variable or Python expression being
formatted.

The formatter for the  quantity  value is {quantity: ^9d} . You can interpret this format
from right to left as follows:
    d  represents an integer value.
    9  tells us the value should take up nine characters on the screen.
    ^  tells us that the number should be aligned in the center of this available
padding; this makes the column look a bit more professional.
    * tells the formatter to use a * as the padding character. With integers,
instead of *, the extra characters are zeros, by default.
    quantity:  is the variable being formatted.

We do similar things with the specifiers for  price  and  subtotal . For  price , we use
{2:<8.2f} ; and for  subtotal ,  {3:>7.2f} . In both cases, we're specifying a space as the
fill character, but we use the  <  and  >  symbols, respectively, to represent that the numbers
should be aligned to the left or right within a minimum space of eight or seven characters.
Further, each float should be formatted to two decimal places.
'''
orders = [("burger", 2, 5), ("fries", 3.5, 1), ("cola", 1.75, 3)]
print("PRODUCT QUANTITY PRICE SUBTOTAL")
for product, price, quantity in orders:
    subtotal = price * quantity
    print(
        f"{product:10s}{quantity:*^9d} "
        f"${price: <8.2f}${subtotal: >7.2f}"
    )
print('*'*20)

import datetime
print("{the_date:%Y-%m-%d %I:%M%p }".format(
    datetime.datetime.now()))