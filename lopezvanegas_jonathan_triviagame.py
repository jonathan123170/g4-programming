"""
Filename: trivia_game.py
Author: <Lopez Vanegas, Jonathan>
Created: <9/29/26>
Instructor: Mr. Burgess
"""

print("Hello! Welcome to the Trivia Game!")

print("\nThis trivia game will have 10 questions.")
print("You will get points for each question answered correctly!")
print("\nLet's get started!")
s = 0

input("Press ENTER to start!")

a = input("What is the default format type for numbers in Python?")
if a == "int":
    a1 = print("\nCorrect! +2 points!")
    if s >= 0:
        s += 2
else:
    a2 = print("\nIncorrect! -1 point!")
    if s > 0:
        s -= 1
print(f"\nSCORE: {s}")
input("\nPress ENTER to continue!")
