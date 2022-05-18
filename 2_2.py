count = 1
my_list = []
while True:
    usr_in = input(f"Enter the {count} element in list. Type 'STOP' to abort: ")
    count += 1
    if usr_in == 'STOP':
        print("The list is generated! Moving on!")
        break
    else:
        my_list.append(usr_in)

print(f"Your list is {my_list}. Now we are changing its contents!")
i = 0
while i < len(my_list) - 1:
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 2
print(f"The final list is: {my_list}")