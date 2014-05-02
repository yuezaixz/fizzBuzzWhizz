# -*- coding:utf-8 -*-
from const import const
def haHeiAh(num_a,num_b,num_c,num_person):
    print "%d个学生开始报数："%num_person
    for num in xrange(1,num_person+1):
        if num != 1 and (num-1) %const.INDENT == 0 :
            command = raw_input("继续查看下%d个请按ENTER（回车），退出请输入q按回车:" %const.INDENT )
            if command == 'q':
                break
        print "第%s个学生报数%s！" %(str(num) , str(hhaHandle(num,num_a,num_b,num_c)))

def hhaHandle(num,num_a,num_b,num_c):
    return const.WORD1[0 if str(num).find(str(num_a)) >= 0 else len(const.WORD1):] or const.WORD1[num%num_a*len(const.WORD1)::]+const.WORD2[num%num_b*len(const.WORD2)::] +const.WORD3[num%num_c*len(const.WORD3)::] or num;

 
