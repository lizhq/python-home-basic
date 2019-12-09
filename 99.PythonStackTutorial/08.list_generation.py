#__author:jack
#date 2019-12-09 17:55

#列表生成式

result = [i for i in range(10)]
print(result)

result = [i*i for i in range(10)]
print(result)

def f(i):
    return 4*i

result = [f(i) for i in range(10)]
print(result)
print(type(result))

# ValueError: too many values to unpack (expected 2)
#a,b = [1,2,3]
#ValueError: not enough values to unpack (expected 3, got 2)
#a,b,c = [1,2]
a,b = ['111',12]
print(a,b)