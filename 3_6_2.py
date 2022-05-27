print("Enter words in latin (lower).")
print()
usr = input("Your input: ").split()

def int_func():
    for i in usr:
        count = 0
        for symb in i:
            if ord(symb) >= 97 and ord(symb) <= 122:
                count += 1
        if count == len(i):
            print(i.title())
        else:
            print("Please use only latin letters in lower case!!!")
int_func()