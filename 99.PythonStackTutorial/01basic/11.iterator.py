#__author:jack
#date 2019-12-09 17:55

from collections import Iterator,Iterable

# 迭代器
# 迭代器不一定是生成器 生成器都是迭代器
l=[1,2,3,4]
d = iter(l)
#print(d) #<list_iterator object at 0x10e137290>

print(next(d)) #StopIteration

print(isinstance(l,Iterable))
print(isinstance(l,Iterator))
print(isinstance([1,2,3],list))

f=open("README.md","r")
for x in f:
    print(x)