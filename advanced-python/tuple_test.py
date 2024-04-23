# test.py

myString = "Hello World"
my_tuple = tuple(myString)
print(my_tuple.index('l'))
try:
    print(my_tuple.index('p'))
except:
    print("Value not found")
print(my_tuple.index('l'))
print(my_tuple.index('H'))
print(my_tuple[::2])

my_tuple = (0, 1, 2, 3, 4, 5)
item_first, *items_between, item_last = my_tuple
print(f"First item: {item_first}")
print(f"Items between: {items_between}")
print(f"Last item: {item_last}")