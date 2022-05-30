# I like importing module random (:
from random import randint

old_list = [randint(100, 500) for i in range(randint(1, 10))]
print(f"Old list is: {old_list}")

new_list = [old_list[el] for el in range(1, len(old_list)) if old_list[el] > old_list[el - 1]]
if not new_list:
    print("Sorry, random is not on your side. Please try again!")
else:
    print(new_list)
