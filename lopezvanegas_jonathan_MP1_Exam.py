"""
Lopez Vanegas_Jonathan
MP1_Exam
"""

print("Hello! Welcome to the 'Grade Predictor & Encourager' tool!")

print("\nThis tool will take your percentage score on a test and will show what letter grade (such as A,B,C,D,& F) belongs to it! ")

g = int(input("\nWhat is your test grade? "))

if g >= 90 and g <= 100:
    print("\nYou have a A! Congratulations!")

elif g >= 80 and g <= 89:
    print("\nYou have a B! Nice Work!")

elif g >= 70 and g <= 79:
    print("\nYou have a C! Nice! Make sure to keep on practicing!")

elif g >= 60 and g <= 69:
    print("\nYou have a D! Make sure to keep on practicing.")

elif g <= 59:
    print("\nYou have a F! Lock in buddy. Keep on practicing!")

print("\nThank you for using this tool!")

print("Goodbye!")
