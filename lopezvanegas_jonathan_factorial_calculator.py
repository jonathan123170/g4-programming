"""
Filename: factorial_calculator.py
Author: <Lopez Vanegas, Jonathan>
Created: <11/9/26>
Instructor: Mr. Burgess
"""

def factorial():
    n = int(input("Please enter a absolute whole number:"))
    a = for number in n:
        print(number)


# You should not need to change any code below this point
def main():
    print("This program computes factorials and displays their intermediate calculations.")
    running = "y"
    while running == "y":
        factorial()
        running = input("Do another calculation? (y/N)\n").lower()
    print("Thank you for using this factorial calculator!")

if __name__ == "__main__":
    main()