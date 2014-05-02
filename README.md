fizzBuzzWhizz
=============
#概述
该项目是一个学习项目，题目是英国小学生练习除法的一个游戏，比如100名学生玩这个游戏。游戏的规则是：

* 你首先说出三个不同的特殊数，要求必须是个位数，比如3、5、7。
* 让所有学生拍成一队，然后按顺序报数。
* 学生报数时，如果所报数字是第一个特殊数（3）的倍数，那么不能说该数字，而要说Fizz；如果所报数字是第二个特殊数（5）的倍数，那么要说Buzz；如果所报数字是第三个特殊数（7）的倍数，那么要说Whizz。
* 学生报数时，如果所报数字同时是两个特殊数的倍数情况下，也要特殊处理，比如第一个特殊数和第二个特殊数的倍数，那么不能说该数字，而是要说FizzBuzz, 以此类推。如果同时是三个特殊数的倍数，那么要说FizzBuzzWhizz。
* 学生报数时，如果所报数字包含了第一个特殊数，那么也不能说该数字，而是要说相应的单词，比如本例中第一个特殊数是3，那么要报13的同学应该说Fizz。如果数字中包含了第一个特殊数，那么忽略规则3和规则4，比如要报35的同学只报Fizz，不报BuzzWhizz。
 
现在，我们需要你完成一个程序来模拟这个游戏，它首先接受3个特殊数，然后输出100名学生应该报数的数或单词。比如，
 
输入
3,5,7
输出（片段）

1
2
Fizz
4
Buzz
Fizz
Whizz
8
Fizz
Buzz
11
Fizz
Fizz
Whizz
FizzBuzz
16
17
Fizz
19
Buzz 
…
一直到100

#项目环境
项目的环境为python2.6，因为项目比较简单，没有外部依赖模块。

#常量配置
为了增加项目的maintainable性，在这里进行配置可能需要修改的信息。

```
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
```

#单元测试
项目通过python2.6内置的unittest模块进行单元测试,执行
python testHaHeiAh.py

#项目运行
在test.py里设置了main入口，执行
python test.py
后根据交互式的信息进行操作
