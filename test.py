#!/usr/bin/python3  -*-coding:utf-8 -*-
def createCounter():
	def t():
		n=1
		while(True):
			yield n
			n = n+1
	s = t()
	def counter():
		return next(s)	
	return counter
counterA = createCounter()
print(counterA(),counterA(),counterA())
counterB = createCounter()
print(counterB(),counterB(),counterB())
def createCounter2():
	n = 0
	def counter():
		nonlocal n
		n = n+1
		return n
	return counter
counter2A  = createCounter2()
print(counter2A(),counter2A())
