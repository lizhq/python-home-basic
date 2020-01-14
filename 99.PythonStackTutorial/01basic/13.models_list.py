#__author:jack
#date 2019-12-16 09:45

import os

#print(help(os))
# https://docs.python.org/3.7/library/os.html

#print(os.getcwd())


# os
# sys
# shutil
# json & picle
# shelve
# xml处理
# yaml处理
# configparser
# hashlib

import hashlib
m = hashlib.md5()
print(m)
m.update("admin".encode("utf8"))
print(m.hexdigest())

# subprocess
# logging模块
# re正则表达式
# paramiko (pycrypto)