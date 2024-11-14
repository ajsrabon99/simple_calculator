def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    
    while True:
        try:
            choice = int(input("Enter choice (1, 2, 3, 4, 5): "))
            if choice not in [1, 2, 3, 4, 5]:
                raise ValueError("Invalid choice.")
            
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            
            if choice == 1:
                result = add(num1, num2)
                operation = "Addition"
            elif choice == 2:
                result = subtract(num1, num2)
                operation = "Subtraction"
            elif choice == 3:
                result = multiply(num1, num2)
                operation = "Multiplication"
            elif choice == 4:
                result = divide(num1, num2)
                operation = "Division"
            elif choice == 5:
                result = modulus(num1, num2)
                operation = "Modulus"
            
            print(f"{operation}: {num1} {get_operator(choice)} {num2} = {result:.2f}")
        
        except ValueError as e:
            print(f"Error: {e}")
        
        again = input("Do you want to more calculations? (yes/no): ").lower()
        if again != 'yes':
            break



def get_operator(choice):
    if choice == 1:
        return "+"
    elif choice == 2:
        return "-"
    elif choice == 3:
        return "*"
    elif choice == 4:
        return "/"
    elif choice == 5:
        return "%"

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def modulus(x, y):
    if y == 0:
        raise ValueError("Cannot take modulus by zero.")
    return x % y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter your number.")


if __name__ == "__main__":
    main()
