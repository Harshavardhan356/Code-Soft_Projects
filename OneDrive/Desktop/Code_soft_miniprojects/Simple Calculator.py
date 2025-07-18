
#Simple calculater 

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Can't divide by zero."
    return x / y

print("Simple Calculator")
print("------------------")
print("Choose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1/2/3/4): ")

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(a, b))
    elif choice == '2':
        print("Result:", sub(a, b))
    elif choice == '3':
        print("Result:", mul(a, b))
    elif choice == '4':
        print("Result:", div(a, b))
    else:
        print("Invalid option.")
except:
    print("Something went wrong. Please enter valid numbers.")

