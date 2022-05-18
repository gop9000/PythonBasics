usr_in = input("Enter the number of the month (1-12): ")

### If user typed something wrong:
if int(usr_in) == 0:
    print("Wrong input! The number should be 1-12!")

elif int(usr_in) > 12:
    print("Wrong input! The number should be 1-12!")

else:
    usr_in = int(usr_in)

### Dict with seasons
seasons = {12: 'Winter', 1: 'Winter', 2: 'Winter',
           3: 'Spring', 4: 'Spring', 5: 'Spring',
           6: 'Summer', 7: 'Summer', 8: 'Summer',
           9: 'Autumn', 10: 'Autumn', 11: 'Autumn'}

### Check season
if usr_in in seasons:
    print(f"The season is {seasons.get(usr_in)}!")
else:
    print("Something went wrong, please check your input!")