'''
Adapters are used to allow two preexisting objects to
work together, even if their interfaces are not compatible. Like the display adapters that
allow you to plug your Micro USB charging cable into a USB-C phone, an adapter object
sits between two different interfaces, translating between them on the fly. The adapter
object's sole purpose is to perform this translation. Adapting may entail a variety of tasks,
such as converting arguments to a different format, rearranging the order of arguments,
calling a differently named method, or supplying default arguments.
'''

# We have the following preexisting class, which takes a string date in
# the format  YYYY-MM-DD  and calculates a person's age on that date

class AgeCalculator:
    
    def __init__(self, birthday):
        self.year, self.month, self.day = (int(x) for x in birthday.split("-"))
    
    def calculate_age(self, date):
        year, month, day = (int(x) for x in date.split("-"))
        age = year - self.year
        if (month, day) < (self.month, self.day):
            age -= 1
        return age

# We can write an adapter that allows a normal date to be plugged into a normal
# AgeCalculator class

import datetime
class DateAgeAdapter:

    def _str_date(self, date):
        return date.strftime("%Y-%m-%d")

    def __init__(self, birthday):
        birthday = self._str_date(birthday)
        self.calculator = AgeCalculator(birthday)

    def get_age(self, date):
        date = self._str_date(date)
        return self.calculator.calculate_age(date)

'''
Creating a class as an adapter is the usual way to implement this pattern, but, as usual,
there are other ways to do it in Python. Inheritance and multiple inheritance can be used to
add functionality to a class. For example, we could add an adapter on the  date  class so that
it works with the original  AgeCalculator  class
'''
import datetime
class AgeableDate(datetime.date):
    def split(self, char):
        return self.year, self.month, self.day