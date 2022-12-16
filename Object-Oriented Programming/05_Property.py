class Color:
    '''Явное применение property'''
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name

    def _get_name(self):
        return self._name

    name = property(_get_name, _set_name)

c = Color("#0000ff", "bright red")
print(c.name)

c.name = "red"
print(c.name)


class Silly:
    '''Применение property через декораторы'''
    @property
    def silly(self):
        "This is a silly property"
        print("You are getting silly")
        return self._silly

    @silly.setter
    def silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value

    @silly.deleter
    def silly(self):
        print("Whoah, you killed silly!")
        del self._silly

s = Silly()
s.silly = "funny"
s.silly
del s.silly

# Применение декоратора для кеширования запроса, чтобы сократить время загрузки страницы
from urllib.request import urlopen
class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None
    
    @property
    def content(self):
        if not self._content:
            print("Retrieving New Page...")
        self._content = urlopen(self.url).read()
        return self._content

import time
webpage = WebPage("http://ccphillips.net/")
now = time.time()
content1 = webpage.content
time.time() - now
now = time.time()
content2 = webpage.content
time.time() - now
content2 == content1