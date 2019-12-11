#__author:jack
#date 2019-11-28 17:55

# filter
def fun(s):
    if s != 'a':
        return s

result = filter(fun,['a','b','c','d',1])
print(result) #<filter object at 0x10f373410>
print(list(result)) #['b', 'c', 'd', 1]

# map
result = map(fun,['a','b','c','d',1])
print(result) #<filter object at 0x10f373410>
print(list(result)) #['b', 'c', 'd', 1]

from functools import reduce
# redure
def add(x,y):
    return x+y

print(reduce(add,[1,2,3,4,5]))
print(reduce(add,range(1,100)))

# lambda
print(reduce(lambda x,y: x+y,range(1,100)))

print(dir(__builtins__))