#!usr/bin/env python3    -*- coding:utf-8 -*-

'a test module' #任何模块的第一个字符串都被视为模块的文档注释;

__author__ = 'Lily'  #使用author变量把作者写进去

import sys

def test():
	args = sys.argv
	if len(args)==1:   #sys中有一个argv变量，用list存储命令行所有参数。argv第一个参数永远是该.py文件的名称
		print("hello world!")
	elif len(args) ==2:
		print('Hello %s' %args[1])
	else:
		print('too many arguments!')

if __name__== '__main__':
	test()


#__xxx__变量是特殊变量，可以被直接引用，但是有特殊用途;
#_xxx,__xxx变量是private，不应该被直接引用


