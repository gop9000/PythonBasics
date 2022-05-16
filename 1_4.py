usr_in = int(input('Enter your number: '))

max = 0

if usr_in >= 0:
    while usr_in > 0:

        last = usr_in % 10

        usr_in = usr_in // 10

        if last > max:
    	    max = last
    print(max)
else:
	print('The numer is negative!')
