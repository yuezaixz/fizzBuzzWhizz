# -*- coding:utf-8 -*-
class ConstError(Exception): pass

class _const(object):
    def __setattr__(self, k, v): 
        if k in self.__dict__:
            raise ConstError
        else:
            self.__dict__[k] = v 

const = _const()
#三个转换单词
const.WORD1 = 'Fizz'
const.WORD2 = 'Buzz'
const.WORD3 = 'Whizz'
#模块名
const.MODULE_NAME = 'haHeiAh'
#方法名
const.METHOD_NAME = 'haHeiAh'
#报数人数
const.NUM_PERSON = 100
#报数间隔，如果不希望间隔请设置个大数字
const.INDENT = 15
