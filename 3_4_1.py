a = int(input("Ener the first number: "))
b = int(input("Ener the second number: "))

def my_func(a, b):
    try:
        result = a ** b
    except TypeError:
        return "Enter a number and a negative number!"
    return result
print(my_func(a, b))