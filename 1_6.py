inc = int(input('Enter your income: '))

print('')

exp = int(input('Enter your expenses: '))

print('')

res = inc - exp

if res > 0:

    rent = inc / res * 10
    
    print('Company works with profit!')

    print(f'Profitability is: {rent: .2f}%')

    print('')

    employees = int(input('Enter the number of your employees: '))

    print('')

    print(f'Profitability per employee is: {rent / employees : .2f}%')

else:

    print('Company works with losses!')

