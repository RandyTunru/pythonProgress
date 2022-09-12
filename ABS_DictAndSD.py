myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'} #Dictionary are a set list of key value pairs, they're unordered and the values can be accessed like lists by putting the key inside square brackets []

print(myCat['size'])

spam = {12345: 'Luggage Combination', 42: 'The Answer'} #Dictionary can also use numbers as their key, and they do not need to start at 0 since Dictionaries are not ordered

spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon) #The order in a list matters, hence the expression returns False

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham) #Unlike lists, the order in a dictionary doesnt matter and the expression returns True as long as both dictionaries have the same key-value pair

identity = {'name': 'Zophie', 'age': 7}

try: 
    print(identity['hair color'])
except KeyError: #accessing a dictionary using a key that doesn't exist will raise a KeyError
    print("Key doesn't exist in the dictionary")

identity['hair color'] = 'blonde' #however if we declare a value to a key that doesn't exist in the dictionary will create a new item(key-value pair) in the dictionary
print(identity['hair color'])


'''
an example program using dictionaries and creating new items when it doesn't exist in the dictionary

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
'''

print(eggs.keys()) #the keys() method of a dictionary returns an iterable (type dict_keys), with all the keys from the dictionary as values

print(eggs.values()) #the values() method of a dictionary returns an iterable (type dict_values), with all the values from the dictionary as values

print(eggs.items()) #the items() method of a dictionary returns an iterable (type dict_items), the value of an index in the iterable are tuples of the key-value pair from the dictionary

#we can use the iterables returned from the methods in for loops
for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for v in eggs.items():
    print(v)

for k, v in eggs.items(): #we can also use the multiple assignment method to assign the tuple values from items() method into 2 variables (key, value in that order)
    print(k, end=' : ')
    print(v)

#we can pass the values returned from those methods to the list() function to make an actual list of the values
listOfEggsKeys = list(eggs.keys())
print(listOfEggsKeys, 'is of type', type(listOfEggsKeys))

#we can use the in keyword to check wether a key or value exist in a dictionary using the keys() and values() method
print('name' in identity.keys())
print('Zophie' in identity.values())

#the get() method will return the value of the key (first argument), however if they key doesn't exist in the dictionary, it will return a fallback value (second argument)
picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

'''
Sometimes we only want to assign a value to a key only when the key doesn't exist yet on the dictionary
using the identity['hair color'] = 'black', if 'hair color' already exist as a key in the identity dictionary
will overwrite it's previous value to 'black'
'''
#we can use setdefault() method to pass a key (first argument) to find in the dictionary, if the key exists it will return its current value, otherwise it will create a new key-value pair with the value passed (second argument) and return it
print(identity.setdefault('skin color', 'white'))
print(identity.setdefault('skin color', 'black'))
print(identity['skin color'])

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count) #pprint gives us a method called pprint() that can print dictionary in a much cleaner way

countPretified = pprint.pformat(count) #pprint also gives us a method called pformat() that can return the prettified string

print(countPretified)

allGuests = {'Alice': {'apples': 5, 'pretzels': 12}, #value in a dictionary can also be a dictonary or even list
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))
