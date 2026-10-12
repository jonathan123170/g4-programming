"""
Lopez Vanegas_Jonathan
MP1_Exam
"""

print("Welcome to the Temperature Converter and Threshold Alert thingamajig!")

f = int(input("\nPlease enter a temperature in Fahrenheit to convert to Celsius: "))

c = (f-32)*5/9

if c <= 0:
    print(f"\nHere is your answer in Celsius: {c} - Freezing Alert!")
elif c > 32:
    print(f"\nHere is your answer in Celsius: {c} - Heat Warning!")
else:
    print(f"\nHere is your answer in Celsius: {c} - Normal Temperature!")

print("\nThank you for using the Temperature Converter and Threshold Alert thingamajig!")
print("\nHave a good day!")