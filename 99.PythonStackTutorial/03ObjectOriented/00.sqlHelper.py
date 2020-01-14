#__author:jack
#date 2020-01-03 13:55

class MyType(type):
    def __init__(self,**argc):
        print("MyType...")

class SqlBase(object):
    __metaclass__  = MyType
    def __init__(self):
        print("this is a base __init__ !")

    def toString(self):
        print("this is a base!")

class SqlHelper(SqlBase):
    version = "1.0"

    def __init__(self, host, user, pwd):
        SqlBase.__init__(self)
        self.host = host
        self.user = user
        self.pwd = pwd

    @staticmethod
    def static(info):
        print(info)

    def add(self):
        print("add")
        # 使用主机名、用户名、密码（self.host 、self.user 、self.pwd）打开数据库连接
        # do something
        # 关闭数据库连接

    def delete(self):
        print("delete")
        # 使用主机名、用户名、密码（self.host 、self.user 、self.pwd）打开数据库连接
        # do something
        # 关闭数据库连接

    def update(self):
        print("update")
        # 使用主机名、用户名、密码（self.host 、self.user 、self.pwd）打开数据库连接
        # do something
        # 关闭数据库连接

    def query(self):
        print("query")
    # 使用主机名、用户名、密码（self.host 、self.user 、self.pwd）打开数据库连接
        # do something
        # 关闭数据库连接# do something
    
    def toString(self):
        pass
        SqlBase.toString(self)
        super().toString()
        print("Host:%s User:%s password:%s " %(self.host, self.user, self.pwd))
    
    @property
    def name(self):
        print("name")
        return "test property"

import socketserver

if __name__=='__main__':
    sqlHelper = SqlHelper('127.0.0.1','admin','123456')
    print(SqlHelper.version)
    print(sqlHelper.version)
    SqlHelper.static("====info")
    sqlHelper.add()
    sqlHelper.delete()
    sqlHelper.toString()

    print(sqlHelper.name)


    #server = socketserver.ThreadingTCPServer(1,2)
    #server.serve_forever()