print("Hello! Welcome to the Conditional Calculator!")

print("\nThis conditional calculator is a calculator that'll help with 2 numbers on the 4 basic operations:")

print("1. Addition")

print("2. Subtraction")

print("3. Multiplication")

print("& 4. Division")

input("\nPress Enter to continue.")

a = int(input("\nPlease enter your first number (e.g., an integer or decimal, like 10 or 5.5):"))

b = input("\nPlease type in the operation you would like to do (like +,-,*,/):")

c = int(input("\nPlease enter your second number (e.g., an integer or decimal, like 10 or 5.5):"))

print("\nHere is your answer:")

if b == "+":
    print(f"{a} + {c} = {a+c}")
elif b == "-":
    print(f"{a} - {c} = {a-c}")
elif b == "*":
    print(f"{a} * {c} = {a*c}")
elif b == "/":
    print(f"{a} / {c} = {a/c}")


print("\nThank you for using the conditional calculator!")

print("\nHave a good day!")