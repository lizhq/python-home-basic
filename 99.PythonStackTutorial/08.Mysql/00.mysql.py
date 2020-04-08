#__author:jack
#date 2020-03-02 13:55

# pip3 install pymysql
# python3 -m pip install --upgrade pip
import pymysql
# ORM sqlalchemy
def test():
    # 创建连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='mysql123', db='home')
    # 创建游标
    cursor = conn.cursor()
    
    # 执行SQL，并返回收影响行数
    effectRow = cursor.execute("update test set txt = '123'")
    print(effectRow)
    # 执行SQL，并返回受影响行数
    #effectRow = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,))
    
    # 执行SQL，并返回受影响行数
    #effectRow = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])
    
    cursor.execute("select * from test")
    row = cursor.fetchone()
    print(row)
    
    # 提交，不然无法保存新建或者修改的数据
    conn.commit()
    
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()


if __name__ == '__main__':
    test()
    print("===")