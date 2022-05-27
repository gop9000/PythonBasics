a = input("Enter the first number: ")
b = input("Enter the second number: ")

def fun(a, b):
    a = float(a)
    b = int(b)

    if a <= 0 or b >= 0:
        return "Please check the input! First number should be > 0 and the second should be < 0!"
    else:
        res = 1
        for n in range(abs(b)):
            res = res / a
        return f"Your result is {res}."
print(fun(a, b))

