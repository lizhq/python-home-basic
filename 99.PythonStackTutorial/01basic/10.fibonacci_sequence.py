#__author:jack
#date 2019-12-09 17:55

#斐波那契数列

def fib(max):
    n,before,after = 0,0,1
    
    while n < max:
        print('inner:',after)

        message = yield after

        print("message:",message)
        before,after = after,before+after # ==> before,after = 1,0 + 1
        n = n + 1

b = fib(10)
#(fib(10))
#print(next(fib(10)))

# TypeError: can't send non-None value to a just-started generator
b.send(None)
b.send("hello")
b.send("hello1")

b.__next__()
print("===")
b.__next__()

