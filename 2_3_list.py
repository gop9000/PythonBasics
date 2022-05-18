usr_in = input("Enter the number of the month (1-12): ")

### If user typed 01-09
if int(usr_in) == 0:
    print("Wrong input! The number should be 1-12!")

elif int(usr_in) > 12:
    print("Wrong input! The number should be 1-12!")

else:
    usr_in = int(usr_in)


### Lists with seasons
winter = ['Winter', 1, 11, 12]
spring = ['Spring', 3, 4, 5]
summer = ['Summer', 6, 7, 8]
autumn = ['Autumn', 9, 10, 11]

### Check season
if usr_in in winter:
    print(f"The season is: {winter[0]}!")
elif usr_in in spring:
    print(f"The season is: {spring[0]}!")
elif usr_in in summer:
    print(f"The season is: {summer[0]}!")
elif usr_in in autumn:
    print(f"The season is: {autumn[0]}!")
else:
    print("Something went wrong, please check your input!")
