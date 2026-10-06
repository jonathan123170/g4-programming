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
q = 0
input("\nPress ENTER to start!")

q1 = input("\nQ1: What is the default format type for numbers in Python?")
if q1 == "int":
    print("\nCorrect! +2 points!")
    if s >= 0:
        s += 2
    if q >= 0:
        q += 1
else:
    print("\nIncorrect! -1 point!")
    if s > 0:
        s -= 1

q2 = input("\nQ2: What symbol is used to perform the modulo operation in Python?")
if q2 == "%":
    print("\nCorrect! +2 points!")
    if s >= 0:
        s += 2
    if q >= 0:
        q += 1
else:
    print("\nIncorrect! -1 point!")
    if s > 0:
        s -= 1

q3 = input("\nQ3: Strings are actually arrays of what data type?")
if q3 == "char":
    print("\nCorrect! +2 points!")
    if s >= 0:
        s += 2
    if q >= 0:
        q += 1
else:
    print("\nIncorrect! -1 point!")
    if s > 0:
        s -= 1

q4 = input("\nQ4: What keyword is used to define a function in Python?")
if q4 == "def":
    print("\nCorrect! +2 points!")
    if s >= 0:
        s += 2
    if q >= 0:
        q += 1
else:
    print("\nIncorrect! -1 point!")
    if s > 0:
        s -= 1

q5 = input("\nQ5: What is the term for combining multiple lists into one?")
if q5 == "concatenation":
    print("\nCorrect! +2 points!")
    if s >= 0:
        s += 2
    if q >= 0:
        q += 1
else:
    print("\nIncorrect! -1 point!")
    if s > 0:
        s -= 1

q6 = input("\nQ6: What function would you use to find how many items are in a list?")
if q6 == "len()":
    print("\nCorrect! +2 points!")
    if s >= 0:
        s += 2
    if q >= 0:
        q += 1
else:
    print("\nIncorrect! -1 point!")
    if s > 0:
        s -= 1

q7 = input("\nQ7: What function is used to get responses from the user in the console?")
if q7 == "input":
    print("\nCorrect! +2 points!")
    if s >= 0:
        s += 2
    if q >= 0:
        q += 1
else:
    print("\nIncorrect! -1 point!")
    if s > 0:
        s -= 1

q8 = input("\nQ8: What method is used to add an item to the end of a list?")
if q8 == "append":
    print("\nCorrect! +2 points!")
    if s >= 0:
        s += 2
    if q >= 0:
        q += 1
else:
    print("\nIncorrect! -1 point!")
    if s > 0:
        s -= 1

q9 = input("\nQ9: What symbol is used for exponents in Python?")
if q9 == "**":
    print("\nCorrect! +2 points!")
    if s >= 0:
        s += 2
    if q >= 0:
        q += 1
else:
    print("\nIncorrect! -1 point!")
    if s > 0:
        s -= 1

q10 = input("\nQ10: What method is used to convert a string to all lowercase characters?")
if q10 == "lower()":
    print("\nCorrect! +2 points!")
    if s >= 0:
        s += 2
    if q >= 0:
        q += 1
else:
    print("\nIncorrect! -1 point!")
    if s > 0:
        s -= 1

print("\nCongratulations! You have finished the Trivia Game!")
print(f"\nQUESTIONS ANSWERED CORRECTLY: {q}/10")
print(f"SCORE: {s}/20")
print("\nThank you for completing this Trivia Game! Goodbye!")