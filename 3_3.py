a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))


def my_f(a, b, c):
    lister = [a, b, c]
    lister.remove(min(lister))
    return lister[0] + lister[1]


print(f"The sum is: {my_f(a, b, c)}")
