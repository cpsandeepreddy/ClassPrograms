#!/usr/bin/python
#lst-occurance.py
#python programm to eliminate the duplicate values without using set datatype.

class list:
    def __init__(self,rem,value,list):
	self.value=value
	self.rem=rem
	self.list=list
	count=1
	while self.value>count:
	    self.list.remove(self.rem)
	    count+=1
	a= self.list.index(self.rem)
	print a+self.value-1

a=list(3,8,[1,2,3,4,2,5,3,3,6,3,3,3,3,3,4])
	
	
	    