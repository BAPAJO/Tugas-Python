x = 200000
y = 10000
rentalTimeStart = 0
rentalTimeEnd = 0
totalPrice = 0

rentalTimeStart = float(input("Rental Time Start: " ))
rentalTimeEnd = float(input("Rental Time End: " ))
rentalTime = rentalTimeEnd - rentalTimeStart
if(rentalTime <= 12):
    print("Rental Price: ", x)
elif(rentalTime > 12):
    print("Rental Price: ", x + (y * (rentalTime - 12)))
    