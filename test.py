def collatz(number):
    if number == 1:
        return 1
    elif number % 2 == 0:
        number //= 2
        print(number)
    elif number % 2 == 1:
        number = 3 * number + 1
        print(number)
    return collatz(number)
    

while True :
    try :
        var1 = int(input())
        break
    except ValueError :
        print("Must input a number")
        continue

collatz(var1)
