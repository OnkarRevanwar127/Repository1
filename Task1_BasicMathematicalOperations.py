def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

try:
    # Take inputs
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform all operations
    print("\nAddition:", add(num1, num2))
    print("Subtraction:", subtract(num1, num2))
    print("Multiplication:", multiply(num1, num2))
    print("Division:", divide(num1, num2))

except ValueError:
    print("Error: Invalid input. Please enter numbers.")