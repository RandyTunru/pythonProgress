var1 = [2, 3, 'ThisString', 5]
print(var1)

for el in var1:
    print(el)

print('This string uses ' + str(var1[0]) + ' from the list var1')

try: 
    print(var1[20])
except IndexError: 
    print("Out of range")

var2 = [[20, 30], 21, 20]
print(var2)
print(var2[0][1])

print(var1[-1])

var1FirstHalf = var1[:2]
var1SecHalf = var1[2:]
print(var1FirstHalf)
print(var1SecHalf)

print(len(var1))

var1[1] = 6
print(var1)

print(var1 + var2)
print(var1 * 3)

del var1[3]
print(var1)

print(2 in var1)
print('ThisString' in var1)
print(30 in var2)
print(30 in var2[0])
print([20, 30] in var2)

firstIndexofVar2, secondIndexofVar2, thirdIndexofVar2 = var2 #number of variables must be equal the length of array

print(firstIndexofVar2)
print(secondIndexofVar2)
print(thirdIndexofVar2)

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies): #enumerate returns the index and the value from the list
   print('Index ' + str(index) + ' in supplies is: ' + item)


import random

print(random.choice(supplies))

suppliesRandomized = ['pens', 'staplers', 'flamethrowers', 'binders']
print(supplies)
random.shuffle(suppliesRandomized)
print(suppliesRandomized)

print(supplies.index('pens'))  #index method returns the index of the value passed as argument
try:   
    print(supplies.index('notInSupplies'))
except ValueError: #index method will raise ValueError when the argument passed isnt found in the list
    print('The value input is notInSupplies')

supplies.append('sticky notes') #append method adds an element at the end of the list
print(supplies)
supplies.insert(1, 'pencils') #insert adds an element at the given index (first argument) with the given value (second argument)
print(supplies) #if a value is already placed at the given index, it will pushed that value up 1 index

supplies.remove('flamethrowers') #remove method removes the given value from the list
print(supplies)
try:    
    print(supplies.remove('erasers'))
except ValueError: #remove method will raise ValueError when the argument passed isnt found in the list
    print('The value input is not found in the list')

supplies.sort() #sort method sorts the list in an ASCIIbetical way
print(supplies)

supplies.sort(reverse= True) #passing the keyword argument reverse to sort with value True will sort the list in reversed
print(supplies)

alphabetsList = ['a', 'A', 'z', 'Z']
alphabetsList.sort() #since it is sort by ASCII, uppercase letters comes first and will be sorted as lower than lowercases (even tho alphabetically incorrect)
print(alphabetsList)
alphabetsList.sort(key= str.lower) #we can pass the keyword argument key with value str.lower to fix the problem (will still prioritize uppercases)
print(alphabetsList)

try : 
    var1.sort()
except TypeError : #the sort method will raise a TypeError when the list contains a string and number(integer and float) type values
    print("Can't sort lists with numbers and strings inside them")

var1.reverse() #reverse method reverse the list
print(var1)
