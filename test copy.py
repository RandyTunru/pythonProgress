def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1
    

while True :
    try :
        var1 = int(input())
        break
    except ValueError :
        print("Must input a number")
        continue

while var1 != 1:
    var1 = collatz(var1)
