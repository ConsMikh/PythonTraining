from collections import namedtuple
Book = namedtuple("Book", "author title genre")

b1 = Book("Pratchett", "Nightwatch", "fantasy")
b2 = Book("Pratchett", "Thief Of Time", "fantasy")
b3 = Book("Le Guin", "The Dispossessed", "scifi")

print(b1.author)
print(b2.title)
print(b3.genre)
