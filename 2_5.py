my_list = [7, 5, 3, 3, 2]
usr_in = int(input("Please enter your number: "))
print(f"The original list is: {my_list}")

### Checking if the number is in list
if usr_in not in my_list:
    my_list.append(usr_in)
else:
    a = len(my_list) - 1 - my_list[::-1].index(usr_in)  # Find the last occurrence
    my_list.insert(a + 1, usr_in)   # Insert after the last occurrence

print(f"The new list is: {my_list}")