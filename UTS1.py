a = int(input("Enter minimum: " ))
b = int(input("Enter maximum: "))
c = 0

while a <= b:
    if a % 3 == 0:
        print(a)
        c = c + a
    a = a + 1

print("-------------- +")
print("Sum: ", c)
