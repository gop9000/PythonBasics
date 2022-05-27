def my_func():
    count = 0
    while True:
        usr = input("Enter your number. Enter 'q' to stop: ").split()

        for i in usr:
            if i == "q":
                return count
            else:
                try:
                    count = count + int(i)
                except ValueError:
                    return "Wrong input!"
print(my_func())