spam = True #There are two boolean values in python True and False (must start with uppercase)
spam = False
# spam = true  ;this will cause an error

#We can also use comparison operators that will resolve into boolean values depending on the expression
spam = 42 == 42 
print(spam)
spam = 42 == 92
print(spam)

spam = 42 == 42.0 #this will resolve to True because python will equal an integer and float as long as the values match
print(spam)
spam = 42 == '42' #however this will be False since (both 42 and 42.0) because python consider the number 42 and string '42' as different
print(spam)
'''
    Below are list of comparison operators that can be used 
    ==  Equal to

    !=  Not equal to

    <   Less than

    >   Greater than

    <=  Less than or equal to

    >=  Greater than or equal to
'''

'''
The and operators take 2 boolean values (we can chain multiple and clauses) and will resove to 
True and True           True

True and False          False

False and True          False

False and False         False
'''
spam = True and True
print(spam)

'''
The or operators take 2 boolean values (we can chain multiple and clauses) and will resove to 
True or True           True

True or False          True

False or True          True

False or False         False
'''
spam = True or False
print(spam)

'''
The not operators take 1 boolean values (we can chain multiple and clauses) and will resove to 
not True            False
not False           True
'''
spam = not True
print(spam)

name = 'Alice'
age = 8

if name == 'Alice': #If statements check wether the condition is True, and will execute the block of code under it
    print('Hi, Alice.')
elif age < 12: #Elif statements will be executed if the If(or other Elif) statement before it resolve to False and it's condition is True
    print('You are not Alice, kiddo.') 
else: #When an If(and all elif) condition resolves to False, the code under the else block will execute
    print('Hello, stranger.')
'''If, Elif, and Else statements will only execute the first block that resolves to True, following the example above 
even though age < 12 will resolve to True, the block of code will not be executed because the if statement was True'''

spam = 0

while spam < 5: #while statement will execute the block of code until the condition resolves to False
    print("Hello world")
    spam += 1

spam = 0

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue #continue statement will repeat the loop process when it is executed
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break #break statement will terminate the loop when it is executed
print('Access granted.')  

for i in range(5): #for in loop will execute a certain number of time depending on the range function
    print(i)

for i in range(1, 6): #we can also pass 2 argument to change the starting number of the range(1st argument)
    print(i)

for i in range(1, 6, 2): #we can also pass 4 argument to change the starting number of the range(1st argument) and the stepping (3rd argument)
    print(i)

