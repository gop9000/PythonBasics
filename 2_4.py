usr_in = input("Please enter your words: ")

### Deleting possible symbols . , ? ! :
last = usr_in[-1]
stop = [".", ",", "!", "?", ":", " "]
if last in stop:
    usr_in = usr_in[:-1]

my_list = usr_in.split(" ")

### Removing after 10th symbol
for s in my_list:
    if len(s) > 10:
        position = my_list.index(s)
        my_list.remove(s)
        s = s[:10]
        my_list.insert(position, s)

### Making the enumerated list
print("Your final strings are: ")
for i, el in enumerate(my_list, 1):
     print(i, el)