from math import *

def square(number):
    if (isinstance(number, int)):
        return sqrt(number)
    else:
        return "Le paramètre doit être un nombre !"


print(square(6))
print(square('t'))