a = int(input("Enter minimum: " ))
b = int(input("Enter maximum: "))

while a <= b:
    if a % 3 == 0:
        print(a)
    a = a + 1

# alternate solution
# for i in range (a, b+1):
#   if a % 3 == 0:
#       print("a")