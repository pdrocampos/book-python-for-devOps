'''
The function list() can be used to create an empty list or a list based on 
another finite iterable object (such as another sequence):
'''

print(list())

print(list(range(10)))

print(list("Henry Miller"))

'''
Lists created by using square brackets directly are the most common form. 
Items in the list need to be enumerated explicitly in this case. Remember 
that the items in a list can be of different types:
'''

empty = []
print(empty)

nine = [0,1,2,3,4,5,6,7,8,9]
print(nine)

mixed = [0, 'a', empty, 'WheelHoss']
print(mixed)

'''
The most efficient way to add a single item to a list is to append the item to 
the end of the list. A less efficient method, insert, allows you to insert an item 
at the index posi‐ tion of your choice:
'''

pies = ['cherry', 'apple']
print(pies)

pies.append('rhubard')
print(pies)

pies.insert(1, 'cream')
print(pies)

'''
The contents of one list can be added to another using the extend method:
'''

desserts = ['cookies', 'paste']
print(desserts)
desserts.extend(pies)
print(desserts)

'''
The most efficient and common way of removing the last item from a list and return‐ 
ing its value is to pop it. An index argument can be supplied to this method, removing 
and returning the item at that index. This technique is less efficient, as the list 
needs to be re-indexed:
'''

print(pies)
pies.pop()
print(pies)
pies.pop(1)
print(pies)

'''
There is also a remove method, which removes the first occurrence of an item.
'''

pies.remove('apple')
print(pies)

'''
One of the most potent and idiomatic Python features, list comprehensions, allows you to use 
the functionality of a for loop in a single line. Let’s look at a simple exam‐ ple, starting
 with a for loop squaring all of the numbers from 0–9 and appending them to a list:
'''

squares = []
for i in range(10):
    squared = i*i
    squares.append(squared)
print(squares)

'''
In order to replace this with a list comprehension, we do the following:
'''

squares = [i*i for i in range(10)]
print(squares)

'''
Note that the functionality of the inner block is put first, followed by the for state‐ ment. 
You can also add conditionals to list comprehensions, filtering the results:
'''

squares = [i*i for i in range(10) if i%2==0]
print(squares)
