"""
Filename: <lopezvanegas_jonathan_number_guessing_game.py>
Author: <Lopez Vanegas, Jonathan>
Created: <11/05/26>
Instructor: Mr. Burgess
"""

import random
#prints a random integer between 1 & 100
x = random.randint(1,100)
print(x)
n = 0
print("Welcome to the Number Guessing Game!")

while True:
    g = int(input("Please enter a number: "))
    if n >= 0:
        n += 1
    if g > x:
        print("Uh oh! Too high, try again!")
        continue
    elif g < x:
        print("Uh oh! Too low, try again!")
        continue
    elif g == x:
        break
print("Congratulations! You guessed the number!")
print(f"\nYou guessed the number in {n} tries!")