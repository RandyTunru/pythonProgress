def isPhoneNumber(text): #This is a function that can check wether the input is a phone number or not
    if len(text) != 12:
        return False
    for i in range(0, 3):
       if not text[i].isdecimal():
             return False
    if text[3] != '-':
         return False
    for i in range(4, 7):
       if not text[i].isdecimal():
             return False
    if text[7] != '-':
         return False
    for i in range(8, 12):
       if not text[i].isdecimal():
             return False
    return True

print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))

#If we want to check wether a phone number is in a larger string we need to add more code
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
   chunk = message[i:i+12]
   if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

import re #re is a module for using RegEx

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #Passing a string value representing your regular expression to re.compile() returns a Regex pattern object
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242. Her\'s are 415-653-2222') #the search() method returns a Match object, which have a group() method that will return the actual matched text from the searched string. It will return None when the pattern isnt found in the string
print('Phone number found: ' + mo.group()) 

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #Adding parentheses will create groups in the regex
mo = phoneNumRegex.search('My number is 415-555-4242.') #Then you can use the group() match object method to grab the matching text from just one group
print(mo.group(1)) #This will print the first parentheses
print(mo.group(2)) #This will print the second parentheses
print(mo.groups()) #If you would like to retrieve all the groups at once, use the groups() method (It returns a tuple of the groups)

'''

In regular expressions, the following characters have special meanings:

.  ^  $  *  +  ?  {  }  [  ]  \  |  (  )

If you want to detect these characters as part of your text pattern, you need to escape them with a backslash:

\.  \^  \$  \*  \+  \?  \{  \}  \[  \]  \\  \|  \(  \)

'''

heroRegex = re.compile (r'Batman|Tina Fey') #The | character is called a pipe. You can use it anywhere you want to match one of many expressions.
mo1 = heroRegex.search('Batman and Tina Fey') #the first occurrence of matching text will be returned as the Match object.
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)') #You can also use the pipe to match one of several patterns as part of your regex. For example, say you wanted to match any of the strings
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())

batRegex = re.compile(r'Bat(wo)?man') #The ? character flags the group that precedes it as an optional part of the pattern
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())


mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

batRegex = re.compile(r'Bat(wo)*man') #The * (called the star or asterisk) means “match zero or more”—the group that precedes the star can occur any number of times in the text
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

batRegex = re.compile(r'Bat(wo)+man') #The + (or plus) means “match one or more.”
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())


mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)

haRegex = re.compile(r'(Ha){3}') #We can use the curly braces to specify how many time will the group will specificly repeat
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo1 = haRegex.search('HaHa')
print(mo1)

haRegex = re.compile(r'(Ha){3,5}') #Specifying another number will make it a range starting from the first number up to the second number
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo1 = haRegex.search('HaHaHaHa')
print(mo1.group())
mo1 = haRegex.search('HaHaHaHaHa')
print(mo1.group())
mo1 = haRegex.search('HaHaHaHaHaHa') #Even though there are 6 repetitions of the pattern, it will only take up to 5 
print(mo1.group())

#We can add a comma but leave the second number blank to make it only match with atleast a certain repetition up to as many possible
haRegex = re.compile(r'(Ha){3,}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo1 = haRegex.search('HaHaHaHa')
print(mo1.group())
mo1 = haRegex.search('HaHaHaHaHa')
print(mo1.group())
mo1 = haRegex.search('HaHaHaHaHaHa') 
print(mo1.group())

#We can leave the first number empty to make it match starting from none up to the second number of repetitions
haRegex = re.compile(r'(Ha){,5}') 
mo1 = haRegex.search('')
print(mo1.group())
mo1 = haRegex.search('HaHa')
print(mo1.group())
mo1 = haRegex.search('HaHaHaHa')
print(mo1.group())
mo1 = haRegex.search('HaHaHaHaHa') 
print(mo1.group())

#Regular Expressions are greedy by default, meaning if we use a range of repetition it will always match the string with the most repetition
#To make a non-greedy(lazy) version we can put a ? after the braces 

haRegex = re.compile(r'(Ha){3,5}?')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo1 = haRegex.search('HaHaHaHa')
print(mo1.group())
mo1 = haRegex.search('HaHaHaHaHa')
print(mo1.group())

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
mo1 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000') #findall() will return a list of strings that matches with the pattern
print(mo1)

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
mo1 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000') #findall() will return a list of tuples of the groups that matches the pattern
print(mo1)

'''
A few shorthands that can be used to match with Regular Expressions
     \d        Any numeric digit from 0 to 9.

     \D        Any character that is not a numeric digit from 0 to 9.

     \w        Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)

     \W        Any character that is not a letter, numeric digit, or the underscore character.

     \s        Any space, tab, or newline character. (Think of this as matching “space” characters.)

     \S        Any character that is not a space, tab, or newline.
'''

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo1 = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo1)

'''
     You can also include ranges of letters or numbers by using a hyphen. For example, the character class [a-zA-Z0-9] 
     will match all lowercase letters, uppercase letters, and numbers. Note that inside the square brackets, 
     the normal regular expression symbols are not interpreted as such. This means you do not need to escape the ., *, ?, or () 
     characters with a preceding backslash. For example, the character class [0-5.] will match digits 0 to 5 and a period.
'''
'''
     placing a caret character (^) just after the character class' opening bracket, you can make a negative character class. 
     A negative character class will match all the characters that are not in the character class.
'''
consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')

beginsWithHello = re.compile(r'^Hello') #the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning of the searched text
mo1 = beginsWithHello.search('Hello, world!')
print(mo1.group())

#The dollar sign ($) at the end of the regex to indicate the string must end with this regex pattern.
endsWithNumber = re.compile(r'\d$')
mo1 = endsWithNumber.search('Your number is 42')
print(mo1.group())

endsWithNumber = re.compile(r'\d+$')
mo1 = endsWithNumber.search('Your number is 42')
print(mo1.group())

wholeStringIsNum = re.compile(r'^\d+$') #When both of the care and dollar symbol is present then the whole string must match the regex
mo1 = wholeStringIsNum.search('1234567890')
print(mo1 == None)
mo1 = wholeStringIsNum.search('12345xyz67890') 
print(mo1 == None)
mo1 = wholeStringIsNum.search('12  34567890')
print(mo1 == None)

atRegex = re.compile(r'.at') #The . (or dot) character in a regular expression is called a wildcard and will match any character except for a newline
mo1 = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo1) 

'''
     the re.compile can take a second argument after it to...

     re.DOTALL                     make the dot character match all characters, including the newline character.
     re.IGNORECASE or re.I         make your regex case-insensitive
     re.VERBOSE                    make it ignore whitespace and comments inside the regular expression string
'''

'''
     The sub() method for Regex objects is passed two arguments. The first argument is a string to replace any matches. 
     The second is the string for the regular expression. The sub() method returns a string with the substitutions applied.
'''
namesRegex = re.compile(r'Agent \w+')
mo1 = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo1)

agentNamesRegex = re.compile(r'Agent (\w)\w*')
mo1 = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(mo1)
#you can type \1, \2, \3, and so on, to mean “Enter the text of group 1, 2, 3, and so on, in the substitution
