#coding=utf-8
__author__ = 'zyx'

#第 002 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import string,random

def ActiveCode(num,length):
    ActiveCode_file=open('activecode.txt','w')
    CodeStr=string.letters+string.digits#生成随机码
    for i in range(num):
        # ActiveCode_Str=[random.choice(CodeStr) for i in range(length)]    #循环生成特定长度的列表
        ActiveCode_Str=random.sample(CodeStr,length)    #sample函数从列表中随机选择一组元素
        ActiveCode_file.write(''.join(ActiveCode_Str)+'\n') #join函数连接list中的元素成字符串
        print (''.join(ActiveCode_Str))
    ActiveCode_file.close()

if __name__=='__main__':
    ActiveCode(200,10)


