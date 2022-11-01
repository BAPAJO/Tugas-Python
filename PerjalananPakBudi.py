l = 2200
gas = l / 12
gasTank = 50
refill = 1
while (gasTank < gas):
    refill = refill + 1
    gasTank = gasTank + 50

print("Sir Budi uses ", gas, "liters amount of gas to travel ", l, "km")
print("Sir Budi also needs to refill his gas ", refill, " times")
