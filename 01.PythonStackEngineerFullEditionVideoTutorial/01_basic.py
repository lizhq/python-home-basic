#!/usr/bin/env python
#_*_coding:utf-8_*_

# 001 变量，输出
'''name = "Jack"
print("hello word!","您好：",name,sep="")

# 002 输入
import getpass
# 将用户输入的内容赋值给 name 变量
pwd = getpass.getpass("请输入密码：")
  
# 打印输入的内容
print(pwd)


del pwd
age = int(input("输入int："))
print("age：",age)
'''

# step 003 集合
# 元组(不可变列表)
name_list = ['alex', 'seven', 'eric']
name_list = list(['alex', 'seven', 'eric'])
#字典（无序）
person = {"name": "mr.wu", 'age': 18}
person = dict({"name": "mr.wu", 'age': 18})

for i in person:
	print(i,person[i]);

# step 004 if
'''
age = 20
if age > 20 :
	print("大于20")
elif age > 30 :
	print("大于30")
else:
	print("其他")
'''	

# step 004 for while break continue
'''
for i in name_list:
	if i == 'seven':
		print("找到seven")
		break;
	print(i)
	
count = 1
while True:
	count+=1
	if count==10:
		continue;
	elif count==20:
		break;
	else:
		print("");
	print("循环次数",count)
'''

# step 005 三元运算
choice = True==False
result = "ok" if choice else "No"
print(result)

# step 006 模块
import os,sys
#print(os.environ)
#print(sys.path)
