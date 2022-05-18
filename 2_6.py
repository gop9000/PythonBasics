print("Please fill the data.")

### First dict
print("THE FIRST PRODUCT")

dict_1 = {}
dict_1['name'] = input("Please enter the first product: ")
dict_1['price'] = input("Please enter the price: ")
dict_1['quantity'] = input("Please enter the quantity: ")

print(dict_1)

### The second product
print("THE SECOND PRODUCT")

dict_2 = {}
dict_2['name'] = input("Please enter the second product: ")
dict_2['price'] = input("Please enter the price: ")
dict_2['quantity'] = input("Please enter the quantity: ")

### The third product
print("THE THIRD PRODUCT")

dict_3 = {}
dict_3['name'] = input("Please enter the third product: ")
dict_3['price'] = input("Please enter the price: ")
dict_3['quantity'] = input("Please enter the quantity: ")

### List of tuples
my_list = [(1, dict_1), (2, dict_2), (3, dict_3)]

print("The list of products is: ")
print(my_list[0])
print(my_list[1])
print(my_list[2])

### Analytics
c = 0
my_dic = {}
list_of_names = []
list_of_prices = []
list_of_qua = []

# Making up the list
while c <= 2:
    b = my_list[c]
    list_of_names.append(b[1].get('name'))
    list_of_prices.append(b[1].get('price'))
    list_of_qua.append(b[1].get('quantity'))
    c += 1

# Making up the dictionary

my_dic['name'] = list_of_names
my_dic['price'] = list_of_prices
my_dic['quantity'] = list_of_qua

### Final output
print("The final output is: ")
for k, v in my_dic.items():
    print(f"{k}: {v}")
