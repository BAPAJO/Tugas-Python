from sys import _enablelegacywindowsfsencoding


num = 0
while True: 
        num = int(input("Enter Year (type -1 to to exit): "))
        if num == -1:
            break
        if num % 4 != 0:
            print(num , "is not a leap year")
        elif num % 100 != 0:
            print(num, "is a leap year")
        elif num % 400 != 0:
            print(num, "is not a leap year")
        else:
            print(num, "is a leap year")