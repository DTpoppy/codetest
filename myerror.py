#! /usr/bin/env python3  -*-coding:utf-8 -*-

from functools import reduce
import pdb

def str2num(s):
	try:
		t = int(s)
	except Exception as e:
		pdb.set_trace()
		t = s.split('.')
		t = int(t[0])+0.1*int(t[1])
	finally:
		return t

def calc(exp):
	ss = exp.split("+")
	ns = map(str2num,ss) 
	return reduce(lambda acc, x:acc+x, ns)

def main():
	r = calc('100+200+345')
	print('100+200+345=', r)
	r = calc('99+88+7.7')
	print('99+88+7.7=',r)

main()

