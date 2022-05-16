in_secs = int(input('Enter the amount of seconds: '))

hours = int(in_secs / 3600)

remains_min = int(in_secs - hours * 3600)

minutes = int(remains_min / 60)

seconds = int(remains_min - minutes * 60)

print(f'The time is {hours}:{minutes}:{seconds} ')
