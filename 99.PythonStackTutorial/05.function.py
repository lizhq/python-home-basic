#__author:jack
#date 2019-11-26 17:55

## 一个 *  可变参数
def render(first,second = 1,*others):
    print(first,second,others)
    print("=====")
    return [1,2,3]

## 两个 * 收集 关键字参数字典
def renderEx(first,second = 1,**others):
    print(first,second,others)
    print("=====")

ret = render([1,2,3])
render([1,2,3],"133","ww","11",[1,2,3])

renderEx([1,2,3],"133",name = "ww", sex = "11",list = [1,2,3])

# 逆向参数
render(*[1,2,3,4,5])
render(**{"first":"wwww"})

print("ret")

 
count = 10
def outer():
    global count
    print(count)
    count = 11
    print(count)
    sum = 11
    def inner():
        nonlocal sum
        sum = 12
        print("inner",count)
        print("sum",sum)
    
    inner()
    print("outer",count)

print(outer())
print(count)