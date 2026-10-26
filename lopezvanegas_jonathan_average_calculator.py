"""
Filename: <lopezvanegas_jonathan_average_calculator.py>
Author: <Lopez Vanegas, Jonathan>
Created: <10/22/26>
Instructor: Mr. Burgess
"""

x = 0
b = 0
s = 1

print("Hello! Welcome to the Average Calculator!")

print("\nThis average calculator is a calculator that'll help you find the average of numbers.")

while True:
    a = int(input("\nPlease enter a number:"))
    f = s/b
    s += x

    print(f"\nCurrent sum of numbers: {s}")
    if x >= 0:
        x += 1

    print(f"\nCurrent amount of numbers entered: {b}")
    c = (a+b)/2
    print(f"\nCurrent average of numbers: {a}")

    t = input("\nWould you like to enter another number? (y/n)")
    if t == "y":
        continue
    else:
        break

print("\nThank you for using the Average Calculator!")

print("\nHave a good day!")