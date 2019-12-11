#__author:jack
#date 2019-12-11 13:55

import random

print(random.random())
print(random.randint(1,8))
print(random.choice('abcdefg'))
print(random.choices('abc',[1,9,1],k=2))

l = [2,3,4,5,6]
random.shuffle(l)
print(l)

def random_code():
    code = ''
    for i in range(5):
        c = random.choice([random.randrange(10),chr(random.randrange(65,91))])
        code += str(c)
        
    return code

print(random_code()) 
print(random.choices([random.randrange(10),chr(random.randrange(65,91))],k=4))