from sys import argv
from random import randint

sname, work_hours, wage_hour = argv

# Some acute and poignant humour (:
bonus = randint(10, 20)
# End of the humour
try:
    salary = (int(work_hours) * int(wage_hour)) + bonus
    print(f"Your salary is: {salary} tougrics.")
except:
    print("Enter numbers!!!")
