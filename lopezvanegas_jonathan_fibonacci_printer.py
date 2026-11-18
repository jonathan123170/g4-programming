"""
Filename: fibonacci_printer.py
Author: <Lopez Vanegas, Jonathan>
Created: <11/18/26>
Instructor: <Mr. Burgess>
"""

def n_fibonacci():
    n = int(input("Please enter a absolute whole number:"))
    t = 1
    p = 1
    for i in range(0,n,p+t):
        p = i
        t =+ t
        i = n
        i += n
        print(i)



# You should not need to change any code below this point
def main():
    print("This program displays the standard Fibonacci sequence that is n elements long.")
    running = "y"
    while running == "y":
        n_fibonacci()
        running = input("Print another sequence? (y/N)\n").lower()
    print("Thank you for using this standard Fibonacci sequence printer!")

if __name__ == "__main__":
    main()