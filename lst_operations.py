#!/usr/bin/python
#lst_operations.py
#python program to perform all list operations.

class lstoper:
    def __init__(self):
        pass
    def lst(self,lst1,lst2):
	self.lst1=lst1
	self.lst2=lst2
	print self.lst1
	print self.lst2
    def append(self):
	print 'inside append'
        self.lst2.append(self.lst1)
	print self.lst1
	print self.lst2
    def extend(self):
	print 'inside extend'
	self.lst2.extend(self.lst1)
	print self.lst1
	print self.lst2
    def insert(self,index,value):
	print 'inside insert'
	self.index=index
	self.value=value
	self.lst1.insert(self.index,self.value)
	self.lst2.insert(self.index,self.value)
	print self.lst1
	print self.lst2
    def pop(self):
	print 'inside pop'
	self.lst2.pop()
	self.lst1.pop()
	print self.lst1
	print self.lst2
    def remove(self,element):
	print 'inside remove'
	self.element=element
	self.lst1.remove(element)
	self.lst2.remove(element)
	print self.lst1
	print self.lst2

a=lstoper()
a.lst([1,2,3,4],[5,6,7,8,4])
a.append()
a.extend()
a.insert(2,6)
a.pop()
a.remove(6)
	
	