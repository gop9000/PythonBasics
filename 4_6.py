from itertools import count
from itertools import cycle

print("Counter:")
counter = count(9)
for i in range(9):
    print(f"{next(counter)}")
print()

print("Cycler: ")
cycler = cycle("foo")
for i in range(9):
    print(f"{next(cycler)}")
