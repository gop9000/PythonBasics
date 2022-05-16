km = int(input('Enter the number of kilometers: '))

print('')

km_res = int(input('Enter the number of needed kilometers: '))

print('')

days = 1


while km <= int(km_res):

	km = km + (km * 10 / 100)
	
	days = days + 1

print(f'The number of days is {days}.')
