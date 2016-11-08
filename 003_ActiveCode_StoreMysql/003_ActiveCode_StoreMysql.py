#coding=utf-8
__author__ = 'zyx'

#第 003 题：把生成的 200 个激活码存入mysql数据

import MySQLdb,re

# 打开数据库连接
db=MySQLdb.connect("localhost","root","root","test")
# 使用cursor()方法获取操作游标
cursor=db.cursor()

#创建数据库表
Creat_table="""CREATE TABLE ActiveCode(
                id   INT(20) not null AUTO_INCREMENT,
                activecode char(20),
                primary key (id))"""
#表已存在返回错误并清空表数据
try:
    cursor.execute(Creat_table)
except MySQLdb.Error as e:
    print('connect fails!{}'.format(e))
    cursor.execute("Truncate Table ActiveCode")


#打开并读取激活码文件
ActiveCode_file=open('activecode.txt','r')
file_contain= ActiveCode_file.read()
#将文件内容分割成list
#code_list=file_contain.split('\n')#字符串分割
code_list=re.findall(r'[a-zA-Z0-9]+',file_contain)#正则表达式匹配，并生成list
#执行插入语句
try:
    for i in code_list:
        cursor.execute("insert into ActiveCode (activecode) values(%s)",i)
        db.commit()
except:
    db.rollback()#发生错误时回滚

#执行查询语句
sql_select=cursor.execute("select * from ActiveCode")
results_select=cursor.fetchall()
#读取查询结果并打印结果
for row in results_select:
    id=row[0]
    activecode=row[1]
    print "id=%s,activecode=%s" % (id,activecode)
db.close()



