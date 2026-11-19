# My baseise sakrekenaar
# This program can plus, minus, maal  en deel .
# Dit gee ook die gebruiker die opsie om die berekeninge te verwyder.

# Funksie om 2 nommers te plus
def plus(num1, num2):
    return num1 + num2

# Funksie om twee nommers met mekaar te minus
def minus(num1, num2):
    return num1 - num2

# Funksie om twee nommers met mekaar te maal
def maal(num1, num2):
    return num1 * num2

# Funksie om twee nommers met mekaar te deel
def deel(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero!"
    else:
        return num1 / num2


# Hierdie variable beheer die while loop
running = True

while running:

    print("\n--- MY CALCULATOR ---")
    print("1. Plus")
    print("2. Minus")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear screen")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1" or choice == "2" or choice == "3" or choice == "4":

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            print("Answer:", plus(num1, num2))

        elif choice == "2":
            print("Answer:", minus(num1, num2))

        elif choice == "3":
            print("Answer:", maal(num1, num2))

        elif choice == "4":
            print("Answer:", deel(num1, num2))

    elif choice == "5":
        import os
        os.system("cls")
        print("Screen cleared.")

    elif choice == "6":
        print("Calculator closed. Goodbye!")
        running = False

    else:
        print("Invalid option. Please try again.")