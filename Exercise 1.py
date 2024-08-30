'''
from math import *
from math import floor
#Exercise1
wii = 100

userIn = int(input("How much money do you have? "))
print("You have", userIn, "pesos")
afford = floor(userIn/wii)
print("You can buy", afford, "Nintendo Wiis!")

additional = wii - (userIn - (wii*afford))
print("You still need", additional, "pesos to buy 1 more Nintendo Wiis!")

#Exercise2
from math import factorial

userIn = int(input("Enter a number: "))
factorial=1
for x in range(1, (userIn+1)):
    factorial = factorial * x
print("The factorial of the entered number is: ", factorial)
'''
from math import factorial

#Exercise3
factorList = []
userIn = int(input("Enter a number: "))
for x in range(1, (userIn+1)):
    if userIn%x == 0:
        factorList.append(x)
print("The factors of", userIn, "are:", factorList)



