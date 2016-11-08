#coding=utf-8
__author__ = 'zyx'
# 第001题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果

from PIL import Image,ImageDraw,ImageFont
import random

def PicAddnum(picpath,num):
    pic = Image.open(picpath)
    x,y=pic.size
    print pic.size
    myfont=ImageFont.truetype('Arial.ttf',size=x/3)
    ImageDraw.Draw(pic).text((x*2/3,50),str(num),fill='red',font=myfont)
    pic.save("2.jpg")
    pic.show("2.jpg")

if __name__=='__main__':

    PicAddnum("1.jpg",int(random.random()*100))