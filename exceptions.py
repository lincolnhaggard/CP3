#Exceptions from things our users do errors
#0/0, File not found, Value error, type errorm, and index error
class NegativeNumberError(Exception):
    pass
while True:
    try:
        num = int(input("Tell me a number: "))
    except ValueError:
        print("Wrong type!")
        continue
    else:
        break

while True:
    try:
        numTwo = int(input("Tell me another number: "))
        if numTwo<=0:
            raise NegativeNumberError("Cannot be a negative")
    except ValueError:
        print("Wrong type!")
        continue
    except NegativeNumberError as e:
        print(e)
    else:
        try:
            print(f"{str(num)} divided by {str(numTwo)} equls {num/numTwo}")
            break
        except ZeroDivisionError:
            print("You cannot divide by 0, try again")
            continue
    #runs no matter what
    
