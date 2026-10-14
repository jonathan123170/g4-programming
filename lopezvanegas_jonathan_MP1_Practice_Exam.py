"""
Lopez Vanegas_Jonathan
Practice_MP1_Exam
"""

print("Welcome to the Temperature Converter and Threshold Alert tool!")

f = int(input("\nPlease enter a temperature in Fahrenheit to convert to Celsius: "))

c = (f-32)*5/9

if c <= 0:
    print(f"\nHere is your answer in Celsius: {c}°C - Freezing Alert!")
elif c > 32:
    print(f"\nHere is your answer in Celsius: {c}°C - Heat Warning!")
else:
    print(f"\nHere is your answer in Celsius: {c}°C - Normal Temperature!")

print("\nThank you for using the Temperature Converter and Threshold Alert tool!")
print("\nHave a good day!")