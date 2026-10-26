"""
Filename: <lopezvanegas_jonathan_average_calculator.py>
Author: <Lopez Vanegas, Jonathan>
Created: <10/22/26>
Instructor: Mr. Burgess
"""

a = 0
x = 0
n = 0
s = 0
print("Hello! Welcome to the Average Calculator!")

print("\nThis average calculator is a calculator that'll help you find the average of numbers.")

while True:
    n = int(input("\nPlease enter a number:"))
    s = s + n

    print(f"\nCurrent sum of numbers: {s}")
    if x >= 0:
        x += 1

    print(f"\nCurrent amount of numbers entered: {x}")
    a = (s/x)

    print(f"\nCurrent average of numbers: {a}")

    t = input("\nWould you like to enter another number? (y/n)")
    if t == "y":
        continue
    else:
        break

print("\nThank you for using the Average Calculator!")

print("\nHave a good day!")