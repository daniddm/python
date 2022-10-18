
from random import random


import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']




xS = random.choice(numbers)

letter = int(input(" how many letters ? "))
symbol = int(input("how many symbol ? "))
number = int(input("how many numbers ? "))

password_list = []

for i in range( 0, letter ):
    xl = random.choice(letters)
    print(xl)
    password_list += xl
for x in range (0, symbol):
    xN = random.choice(symbols)
    print(xN)
    password_list += xN
for y in range (0, number):
    xS = random.choice(numbers)
    print(xS)
    password_list += xS


print(f" the password is : {password_list}")