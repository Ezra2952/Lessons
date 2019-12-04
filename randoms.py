import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

'''The smallest number line 1 can generate is 5 and 20 is the largest number'''
'''The smallest number line 2 can generate is 3 and 9 is the largest number.
line 2 can not produced a 4 because it can only produce odd-unmbers'''
'''The smallest number line 3 can generate is 2.500000 and 5.500000 is the largest number '''

print(random.randint(1, 100))
