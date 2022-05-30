from random import randint

lst = [randint(1, 15) for i in range(randint(8, 10))]
new_lst =[i for i in lst if lst.count(i) == 1]
print(f"The pseudorandomly generated list is {lst}")

if not new_lst:
    print("Oops, the previous list contains only duplicates")
else:
    print(f"The new list is {new_lst}")