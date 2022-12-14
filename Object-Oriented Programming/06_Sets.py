'''
Sets are much more efficient than lists when checking for membership using the  in  keyword. 
A set will find the value in the same amount of time no matter how big the container is,
but a list will take longer and longer to search for a value as the list contains more and more
values.
'''

first_artists = {
    "Sarah Brightman",
    "Guns N' Roses",
    "Opeth",
    "Vixy and Tony",
    }
second_artists = {
    "Nickelback", 
    "Guns N' Roses", 
    "Savage Garden"
    }
print("All: {}".format(first_artists.union(second_artists)))
print("Both: {}".format(second_artists.intersection(first_artists)))
print("Either but not both: {}".format(first_artists.symmetric_difference(second_artists)))

print("*"*20)
first_artists = {"Sarah Brightman", "Guns N' Roses",
        "Opeth", "Vixy and Tony"}
bands = {"Guns N' Roses", "Opeth"}
print("first_artists is to bands:")
print("issuperset: {}".format(first_artists.issuperset(bands)))
print("issubset: {}".format(first_artists.issubset(bands)))
print("difference: {}".format(first_artists.difference(bands)))
print("*"*20)
print("bands is to first_artists:")
print("issuperset: {}".format(bands.issuperset(first_artists)))
print("issubset: {}".format(bands.issubset(first_artists)))
print("difference: {}".format(bands.difference(first_artists)))