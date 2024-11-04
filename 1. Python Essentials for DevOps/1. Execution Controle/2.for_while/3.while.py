'''
while loops repeat a block as long as a condition evaluates to True:
'''

count = 0
while count < 3:
    print(f"The count is {count}")
    count += 1


'''
It is essential to define a way for your loop to end. Otherwise, 
you will be stuck in the loop until your program crashes. 
One way to handle this is to define your conditional statement such that it eventually evaluates to False. 
An alternative pattern uses the break statement to exit a loop using a nested conditional:
'''
count = 0
while True:
    print(f"The count is {count}")
    if count > 5:
        break
    count += 1