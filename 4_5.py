from functools import reduce


# Needed for reduce
def func(f_el, s_el):
    return f_el * s_el


lst = [i for i in range(100, 1001, 2)]

print(f"The answer is {reduce(func, lst)}")
