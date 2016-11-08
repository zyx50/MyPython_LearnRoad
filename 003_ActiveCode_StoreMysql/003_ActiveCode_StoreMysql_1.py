#coding=utf-8
__author__ = 'zyx'

#第 003 题：把生成的 200 个激活码存入mysql数据
import MySQLdb,re

class ActiveCode_StoreMysql1(object):
    def __init__(self,filepath,num):
        self.filepath=filepath
        self.num=num

    def sql_insert(self):
    # 打开数据库连接
        db=MySQLdb.connect("localhost","root","root","test")
    # 使用cursor()方法获取操作游标
        cursor=db.cursor()

    #创建数据库表
        Creat_table="""CREATE TABLE ActiveCode(
                    id   INT(20) not null AUTO_INCREMENT,
                    activecode char(20),
                    primary key (id))"""
    #表已存在返回错误
        try:
            cursor.execute(Creat_table)
        except MySQLdb.Error as e:
            #print('connect fails!{}'.format(e))
            pass
    #根据参数选择是否追加数据
        if self.num==1:
            cursor.execute("Truncate Table ActiveCode")
        else:
            if self.num==0:
                pass

    #打开并读取激活码文件
        ActiveCode_file=open(self.filepath,'r')
        file_contain= ActiveCode_file.read()
    #将文件内容分割成list（下面为两种方式）
        #字符串分割成list
        #code_list=file_contain.split('\n')
        #正则表达式匹配，并生成list
        code_list=re.findall(r'[a-zA-Z0-9]+',file_contain)
    #执行插入语句
        try:
            print "数据正在插入数据库请稍等（loading.....）"
            for i in code_list:
                cursor.execute("insert into ActiveCode (activecode) values(%s)",i)
                db.commit()
        except:
            db.rollback()#发生错误时回滚
            print "插入数据库发生错误，数据已回滚"
        db.close()

    #执行查询语句
    def sql_select(self):
        db=MySQLdb.connect("localhost","root","root","test")
    # 使用cursor()方法获取操作游标
        cursor=db.cursor()
        cursor.execute("select * from ActiveCode")
        results_select=cursor.fetchall()
    #读取查询结果并打印结果
        for row in results_select:
            id=row[0]
            activecode=row[1]
            print "id=%s,activecode=%s" % (id,activecode)
        db.close()


#调用ActiveCode_StoreMysql1类，并进行数据库操作
file=ActiveCode_StoreMysql1("activecode.txt",1) #参数：0表示追加数据，1表示清空数据表重新写入
file.sql_insert()
file.sql_select()

