spam = "That is Alice's cat."  #Strings can be declared using both single and double quotes, but keep in mind that if we try using the same quotation inside the string, python will think it is the end of the sting

#spamWithSingleQuotes = 'That is Alice's cat.' , this code will raise an error since python thinks the second single quote is the end of the string and the characters after it are junk

spamWithSingleQuotes = 'That is Alice\'s cat.' #However we can use the backslash(\) to escape it so python evaluates it as part of the string and not the syntax

'''
A few example of escape characters

    \'  Single quote

    \"  Double quote

    \t  Tab

    \n  Newline (line break)

    \\  Backslash
'''

print(r'That is Carol\'s cat.') #we can also prefix a string with 'r' to tell python that it's a raw string, raw strings ignores escape characters and takes the value inside the quotation as it is

print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''') # we can also use triple quotation (both single and double quotes) to create multiline strings which will not ignore the whitespace (specifically newlines) in the strings, escaping quotes isn't necessary in multiline string

helloString = 'Hello, world!'

print(helloString[0]) #We can access single characters from string using indexing
print(helloString[:5]) #We can also slice a string

print(('Hello' in helloString)) #We can also use the in and not in operator to check wether a string has a substring (exact string, case-sensitive)

name = 'Randy'
age = 18

#This method is called string interpolation
print('My name is %s, i am %s years old' % (name,age)) #We can also include variables in string declaration using %s and specifying the variables after the string (order of variables matter)

#This method is called f-strings
print(f'My name is {name}. Next year I will be {age + 1}.') #We can also prefix the string with f to tell python its a f-string, it can use the same way as string interpolation however we declare the variables inside curly braces (we can also do operations inside)

print(helloString.upper()) #the upper() method returns the string in all uppercase (without modifying the original string)

print(helloString.lower()) #the lower() method returns the string in all lowercase (without modifying the original string)

print(helloString)

print(helloString.upper().isupper()) #the isupper method returns True if the string has atleast one letter and all the letters are uppercase, otherwise False

print(helloString.lower().islower()) #the islower method returns True if the string has atleast one letter and all the letters are lowercase, otherwise False

print(helloString.isupper())

'''
Here are other isX methods we can use with strings
    isalpha() Returns True if the string consists only of letters and isn't blank

    isalnum() Returns True if the string consists only of letters and numbers and is not blank

    isdecimal() Returns True if the string consists only of numeric characters and is not blank

    isspace() Returns True if the string consists only of spaces, tabs, and newlines and is not blank

    istitle() Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters
'''

print(helloString.startswith('Hello')) #startswith() method checks wether a string starts with the string passed as argument, returns boolean values

print(helloString.endswith('world!')) #endswith() method checks wether a string ends with the string passed as argument, returns boolean values

print(helloString.startswith('Hello, world!')) #if we pass the whole string it will still evaluate True (both startswith() and endswith())

print(helloString.startswith('Hello, world!!')) #if we pass more than the string it will still evaluate False (both startswith() and endswith())

print(', '.join(['cats', 'rats', 'bats'])) #join() method returns a string from the list passed as argument, the string it is called on will be the separator of each element of the list

print('ABC'.join(['My', 'name', 'is', 'Simon']))

print('My name is Simon'.split()) #split() method returns a list of the string it is called on, by default it will seperate wherever a whitespace is found

print('MyABCnameABCisABCSimon'.split('ABC')) #we can pass an argument to the split() method to specify a different string to split on, note that the string it is split on will not be include in the list

print('My name is Simon'.split('m'))

print('Hello, world!'.partition('w')) #partition() method returns a tuple of 3 strings, the string before the partition string, the partition string itself, and the the string after the partition

print('Hello, world!'.partition('o')) #if there are multiple occurence of the partition string, it will only separate in the first occurence

print('Hello, world!'.partition('XYZ')) #if there partition string can't be found, it will return the whole string as the first string of the tuple, and will leave the second and third string empty

before, sep, after = 'Hello, world!'.partition(' ') #because the partition string always returns a tuple, we can use the multiple assignment method to get the before, partition, and after string and assign it to variables

print(before)

print(sep)

print(after)

print('Hello'.rjust(10)) #rjust() method returns the string padded towards the right (add spaces left of the original string), the argument will determine the length of the new string

print('Hello'.rjust(4)) #if we pass a number lower (or equal) than the original string length, it will modify the string

print('Hello'.ljust(10)) #ljust() method returns the string padded towards the left (add spaces right of the original string), the argument will determine the length of the new string
#although the spaces might be invisible if we execute print(len('Hello'.ljust(10))) it will print 10

print('Hello'.center(20)) #center() method centers the text (add spaces bat left and right of the string), the argument will determine the length of the new string

print('Hello'.center(20, '*')) #we can also pass a (must be) single character to change the fill character (works for ljust(), rjust(), and center())

print('     Hello       '.strip()) #strip() method lets you remove the whitespaces both left and right of a string

print('     Hello       '.lstrip()) #lstrip() method lets you remove whitespace from the left of the string

print('     Hello       '.rstrip()) #rstrip() method lets you remove whitespace from the right of the string

print('cdfdadfHellocdfda'.strip('cdfa')) #specifying a string as an argument, will remove all occurence of the character on the string passed until the first occurence of a letter that wasn't on the string (works on strip(), lstrip(), rstrip())

print(ord('B')) #ord() method returns an integer code point of a character (ASCII)

print(chr(65)) #chr() method returns a one-character string of an integer code point (ASCII)

import pyperclip #pyperclip is a third party module, it gives access to copy() method that allows us to pass a text to our clipboard and paste it elsewhere, and paste() method that allows us to have access to the clipboard and pass it to our program
import sys

#! python3
# mclip.py - A multi-clipboard program.

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]    # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)
