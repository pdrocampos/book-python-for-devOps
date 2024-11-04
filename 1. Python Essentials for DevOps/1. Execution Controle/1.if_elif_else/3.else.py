'''
Multiple elif loops can append together. If you are familiar with switch statements in other languages, 
this simulates that same behavior of choosing from multiple choices. Adding an else statement at the end 
runs a block if none of the other condi‐ tions evaluate as True:
'''

i = 0
if i == 45:
     print('i is 45')
elif i == 35:
    print('i is 35')
elif i > 10:
    print('i is greater than 10')
elif i%3 == 0:
    print('i is a multiple of 3')
else:
    print("I don't know much about i...")

'''
You can nest if statements, creating blocks containing if statements that only exe‐ cute if an outer if statement is True:
'''

cat = 'spot'
if 's' in cat:
    print("Found an 's' in a cat")
    if cat == 'sheba':
        print('I found sheba')
    else:
        print("Some other cat")
else:
    print(" a cat without 's'")

