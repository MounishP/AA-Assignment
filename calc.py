def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    choice = input("Enter choice(1 2 3 4): ")
    if choice in ('1', '2', '3', '4'):
        i = float(input("Enter first number: "))
        j = float(input("Enter second number: "))
        if choice == '1':
            print(add(i, j))
        elif choice == '2':
            print(subtract(i, j))
        elif choice == '3':
            print(multiply(i, j))
        elif choice == '4':
            print(divide(i, j))
        break
    else:
        print("Invalid Input")
