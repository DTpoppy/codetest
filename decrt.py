#! usr/bin/python3 -*- coding:utf-8 -*-
# decorater

def log(func):
	def wrapper(*arg,**kw):
		print('call %s():' % func.__name__)
		return func(*arg,**kw)
	return wrapper
@log
def now():
	print('2018-7-9')

now()

def log2(text):
	def dectorator(func):
		def wrapper(*arg,**kw):
			print('%s %s():' % (text, func.__name__))
			return func(*arg,**kw)
		return wrapper
	return dectorator

@log2('execute')
def now2():
	print('2018-7-9')
now2()


import functools
def log3(func):
	@functools.wraps(func)
	def wrapper(*arg,**kw):
		print('%s %s():' % (text, func.__name__))
		return func(*arg,**kw)
	return wrapper

@log3
def now3():
	print('2018-7-9')

print(now2.__name__)
print(now3.__name__)

import functools
import time

def log4(text = None):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*arg, **kw):
			if text is None:
				start_time =time.time()
				print("%s is begining" %func.__name__)
				t = func(*arg, **kw)
				print('%s is end' % func.__name__)
				end_time = time.time()
				dtime = start_time-end_time
				print('%s is executed in %s ms' %(fun.__name__,dtime))
			else:
				print(text)
				start_time =time.time()
				print("%s is begining" %func.__name__)
				t=func(*arg, **kw)
				print('%s is end' % func.__name__)
				end_time = time.time()
				dtime = start_time-end_time
				print('%s is executed in %s ms' %(fun.__name__,dtime))
			return t
		return wrapper
	return decorator
@log4
def fast(x,y):
	time.sleep(0.0012)
	return x+y
@log4('slow')
def slow(x,y,z):
	time.sleep(0.1234)
	return x*y*z	

f = fast(11,22)
s = slow(11,22,33)				 
print(f)
print(s)				
