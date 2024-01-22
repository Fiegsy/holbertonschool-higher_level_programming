#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ldig = number % -10
else:
    ldig = number % 10
if ldig > 5:
    print("Last digit of", number, "is", ldig, "and is greater than 5")
elif ldig == 0:
    print("Last digit of", number, "is", ldig, "and is 0")
else:
    print("Last digit of", number, "is", ldig, "and is less than 6 and not 0")
