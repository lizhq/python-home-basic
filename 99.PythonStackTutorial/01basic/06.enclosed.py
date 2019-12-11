#__author:jack
#date 2019-12-08 12:20

# 闭包

def enclosed():
    x = 10

    def inner():
        print(x)
    return inner

f = enclosed()
# f()

#decorate
import time

def showTime(func,flag):
    def warpper(v):
        v()
        if flag:
            print("this is a true flag doing")
            return func()
        print("this is a false or others flags doing")
        startTime = time.time()
        result = func()
        endTime = time.time()
        print('doing times:%s' % (endTime-startTime))
        return result
    return warpper

def logger(flag):
    def showTime(func):
        def warpper():
            if flag != True:
                print("this is a false flag doing")
                return func()
            print("this is a true or others flags doing")
            startTime = time.time()
            result = func()
            endTime = time.time()
            print('doing times:%s' % (endTime-startTime))
            return result
        return warpper
    return showTime


@logger(True)
def test():
    time.sleep(2)
    print("test...")
    return True
#test = showTime(test,False)
#print(test())


def func(f):
    print("this is a function")

@func
def home():
    print("this is a home page")


