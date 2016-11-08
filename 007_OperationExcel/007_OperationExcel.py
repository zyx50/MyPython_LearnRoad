#coding=utf-8
__author__ = 'zyx'
# 纯文本文件 student.txt为学生信息,请将上述内容写到 student.xls 文件中
import xlwt
import xlrd
import json

def add_excel_1():
    data=json.loads('{"1":["张三",150,120,100],"2":["李四",90,99,95],"3":["王五",60,66,68]}')
    file=xlwt.Workbook()
    table=file.add_sheet('student1')
    for row,i in enumerate(data):    #enumerate(data)获取data的下标和值
        table.write(row,0,i)#write()参数：行、列、值
        for col,j in enumerate(data[i]):
            table.write(row,col+1,j)
        file.save('student.xls')

def add_excel_2():
    data={"1" : "11","2" : "22","3" : "33"}
    file_1=xlwt.Workbook()
    sheet_2=file_1.add_sheet('student2')
    for i in range(len(data)):
        sheet_2.write(i,0,data.keys()[i])
        sheet_2.write(i,1,data.values()[i])
    file_1.save('student.xls')

def add_excel_3():
    data=[[2, 82, 65535], [20, 90, 13],[26, 809, 1024]]
    file=xlwt.Workbook()
    sheet_3=file.add_sheet('sheet3')
    [sheet_3.write(i,j,data[i][j]) for i in range(len(data)) for j in range(len(data))]
    file.save('student.xls')

def row():
    file=xlrd.open_workbook('student.xls')
    n=file.sheets()[0].nrows
    print n

if __name__=='__main__':
    #add_excel_1()
    #add_excel_2()
    #add_excel_3()
    row()