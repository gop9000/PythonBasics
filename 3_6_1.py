print("Enter words in latin (lower).")
print()
usr = input("Your input: ")

def int_func(usr):
    for i in usr:
        en = 0
        if ord(i) >= 97 and ord(i) <= 122:
            en += 1
            return usr.capitalize()

        else:
            return "Please use only latin letters in lower case!!!"

print(int_func(usr))