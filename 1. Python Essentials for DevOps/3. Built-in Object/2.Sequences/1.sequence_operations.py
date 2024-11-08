'''
There are many operations that work across all of the types of sequences. We cover some of the most commonly used operations here.
You can use the in and not in operators to test whether or not an item exists in a sequence:
'''

print(2 in [1,2,3])

print('a' not in 'cat')

print(10 in range(12))

print(10 not in range(2, 4))


'''
You can reference the contents of a sequence by using its index number. To access the item at some index, use square brackets with the 
index number as an argument. The first item indexed is at position 0, the second at 1, and so forth up to the number one less than the 
number of items:
'''

my_sequence = 'Bill Cheatham'
print(my_sequence[0])
print(my_sequence[2]) 
print(my_sequence[12]) 

'''
Indexing can appear from the end of a sequence rather than from the front using neg‐ ative numbers. The last item has the index of –1, 
the second to last has the index of – 2, and so forth:
'''

print(my_sequence[-1])
print(my_sequence[-2])
print(my_sequence[-13])

'''
The index of an item results from the index method. By default, it returns the index of the first occurrence of the item, but optional 
arguments can define a subrange in which to search:
'''

print(my_sequence.index('C'))
print(my_sequence.index('a'))
print(my_sequence.index('a',9,12))
print(my_sequence[11])

'''
You can produce a new sequence from a sequence using slicing. A slice appears by invoking a sequence with brackets containing optional 
start, stop, and step arguments:
                                my_sequence[start:stop:step]
'''

my_sequence = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(my_sequence[2:5])
print(my_sequence[:5])
print(my_sequence[3:])
print(my_sequence[-6:])
print(my_sequence[3:-1])