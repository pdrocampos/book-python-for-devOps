'''
Exceptions are a type of error causing your program to crash if not handled (caught). Catching them with a try-except block allows the program to continue.
 These blocks are created by indenting the block in which the exception might be raised, putting a try statement before it and an except statement after it, 
 followed by a code block that should run when the error occurs:
'''

thinkers = ['Plato', 'PlayDo', 'Gumby']
while True:
    try:
        thinker = thinkers.pop()
        print(thinker)
    except IndexError as e:
        print("We tried to pop too many thnkers")
        print(e)
        break

