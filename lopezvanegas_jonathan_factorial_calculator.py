"""
Filename: factorial_calculator.py
Author: <Lopez Vanegas, Jonathan>
Created: <11/9/26>
Instructor: Mr. Burgess
"""
def factorial():
    n = int(input("Please enter a absolute whole number:"))
    a = 1
    print(f"{n}! = ", end='')
    for i in range(n,0,-1):
        if i > 1:
            print(f"{i} * ", end='')
        else:
            print(f"{i} ", end='')
        #print (i)
        a *= i
    print(f"= {a}")



# You should not need to change any code below this point
def main():
    print("This program computes factorials and displays their intermediate calculations.")
    running = "y"
    while running == "y":
        factorial()
        running = input("Do another calculation? (y/n)\n").lower()
    print("Thank you for using this factorial calculator!")

if __name__ == "__main__":
    main()