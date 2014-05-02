#!/usr/bin/python
# -*- coding: utf-8 -*- 

from const import const
from sys import exit

def testHaHeiAh(p_a=3,p_b=5,p_c=7):
    moduleName = const.MODULE_NAME
    methodName = const.METHOD_NAME

    module = __import__(moduleName)
    method = getattr(module,methodName)
    print "三个特殊数字为%d、%d和%d" %(p_a,p_b,p_c)
    method(p_a,p_b,p_c,const.NUM_PERSON)
    

def getInputInt(title):
    for i in range(0,3):
        attr = raw_input("请输入%s：" %title).strip()

        if len(attr) == 0:
            print "您输入的%s为空，请重新输入" %title
            continue
        elif len(attr) != 1:
            print "您输入的%s不是个位整数，请重新输入" %title
            continue
        else:
            try:
                return int(attr)
            except ValueError:
                print "您输入的%s不是数字，请重新输入" %title
    else:
        print "连续3次输入错误，程序退出！"
        exit() 


if __name__ == '__main__':
    testHaHeiAh(getInputInt('第一个数字'),getInputInt('第二个数字') ,getInputInt('第三个数字') )
        
