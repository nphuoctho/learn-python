"""
Lists
"""

my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

"""
Enumerate
"""
for index, item in enumerate(my_list):
    print(f"Index: {index}, Item: {item}")


"""
Slicing
: is called slice operator
has format [start:stop:step]
"""
new_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(new_list[:1])

'''
List Comprehensions
list[<expression> for <item> in <iterable> if <condition>]
'''
word = 'Hello World'
print([char for char in word])
