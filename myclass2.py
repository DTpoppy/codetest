#! /usr/bin/env python3 -*- coding:utf-8 -*-

from enum import Enum

Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

for name,member in Month.__members__.items():
	print(name,'=>',member,'.',member.value)


from enum import unique

@unique  #检查保证没有重复值
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6


day1 = Weekday.Mon
print(day1,Weekday.Mon,Weekday['Mon'],Weekday(1),Weekday.Mon.value)


class Gender(Enum):
	Male = 0
	Female = 1

class Student(object):
	def __init__(self,name,gender):
		self.name = name
		self.gender = Gender(gender)
bart = Student('Bart',Gender.Male)
print(bart.name,bart.gender)





