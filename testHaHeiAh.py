#!/usr/bin/env python  
# -*- coding:utf-8 -*-
  
import unittest
import haHeiAh as testClass
from const import const
    
class testHaHeiAh(unittest.TestCase):

    #初始化工作
    def setUp(self):
        pass
    
    #推出清理工作
    def tearDown(self):
        pass

    def testHhaHandle(self):
        #测试被第一个数（3）整除
        self.assertEqual(testClass.hhaHandle(3,3,5,7),const.WORD1,'fail')
        #测试不被任何数整除，且不含有第一个数（3）
        self.assertEqual(testClass.hhaHandle(4,3,5,7),4,'fail')
        #测试被第二个数（5）整除
        self.assertEqual(testClass.hhaHandle(5,3,5,7),const.WORD2,'fail')
        #测试被第三个数（7）整除
        self.assertEqual(testClass.hhaHandle(7,3,5,7),const.WORD3,'fail')
        #测试同时被两个数整除
        self.assertEqual(testClass.hhaHandle(15,3,5,7),const.WORD1+const.WORD2,'fail')
        #测试同时被三个数整除
        self.assertEqual(testClass.hhaHandle(105,3,5,7),const.WORD1+const.WORD2+const.WORD3,'fail')
        #以下测试除3 5 7外别的数字组合
        self.assertEqual(testClass.hhaHandle(16,4,6,9),const.WORD1,'fail')
        self.assertEqual(testClass.hhaHandle(18,3,6,9),const.WORD1+const.WORD2+const.WORD3,'fail')
        self.assertEqual(testClass.hhaHandle(24,3,6,8),const.WORD1+const.WORD2+const.WORD3,'fail')
        self.assertEqual(testClass.hhaHandle(24,1,2,3),const.WORD1+const.WORD2+const.WORD3,'fail')

if __name__ == '__main__':
    unittest.main()
