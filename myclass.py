#! usr/bin/env pyton3 -*- coding:utf-8 -*-

class Student(object):
	count =0
	__slots__ = ('__name','__gender','__score') #限制class实例能添加的属性
	def __init__(self, name, gender,score):
		self.__name = name
		self.__gender = gender
		Student.count=Student.count+1
		self.__score = score

	def get_gender(self):
		return self.__gender
	def set_gender(self,gender):
		self.__gender = gender
		return self.__gender
	@property		#将方法变为属性
	def score(self):
		return self.__score
	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be integer!')
		if value<0 or value>100:
			raise ValueError('score must btween 0~100')
		self.__score = value


bart = Student('Bart','male',60)
print(bart.get_gender())
print(bart.set_gender('female'))
print(bart.get_gender())
print(bart.count)
print(Student.count)

Bob = Student('bob','male',80)
print(Bob.count)

print(bart.score)
bart.score = 30
print(bart.score)


class Screen(object):
	__slots__ = ('__width','__height')
	
	def __str__(self):
		return 'width: %s  hight: %s' %(self.__width, self.__height)
	__repr__ = __str__

	@property
	def width(self):
		return self.__width
	@width.setter
	def width(self,value):
		if not isinstance(value,int):
			raise ValueError('please input integer!')
		if value<0:
			raise ValueError('value must be greater than 0')
		self.__width = value
	@property
	def height(self):
		return self.__height
	@height.setter
	def height(self,value):
		if not isinstance(value,int):
			raise ValueError('please input integer!')
		if value<0:
			raise ValueError('value must be greater than 0')
		self.__height = value

	@property
	def resolution(self):
		return self.__height * self.__width

s = Screen()
s.width = 1024
s.height = 768
print('width: %s; height: %s; resolution: %s' %(s.width,s.height,s.resolution))
print(s)

class Fib(object):
	def __init__(self):
		self.a,self.b = 0,1
	def __iter__(self):
		return self
	def __next__(self):
		self.a ,self.b = self.b,self.a+self.b
		if self.a>50:
			raise StopIteration()
		return self.a
	def __getitem__(self,n):
		if isinstance(n,int):
			a,b = 1,1
			for x in range(n):
				a,b = b, a+b
			return a
		if isinstance(n,slice):
			start = n.start
			stop = n.stop
			if start is None:
				start =0
			a,b = 1,1
			L = []
			for x in range(stop):
				if x>=start:
					L.append(a)
				a, b = b, a+b
			return L

f = Fib()
for n in Fib():
	print(n)
for i in range(10):
	print(f[i])
print(f[5:10])		
