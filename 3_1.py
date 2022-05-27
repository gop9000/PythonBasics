a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def my_f(a, b):
    try:
        return int(a / b)
    except ZeroDivisionError:
        print("Don't divide by zero!!!")

print(my_f(a, b))
