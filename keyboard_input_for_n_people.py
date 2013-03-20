#!/usr/bin/python
#keyboard_input_for_n_people.py
#python program to input the data.

class pc:
    def input(self):
	print 'your name is:%r\nyour age is %r \nyour height is %r' %(self.name,self.age,self.height)

class exe11(pc):
    def method(self):
	self.name=raw_input('your name please: ')
	self.age=raw_input('ur age please" ')
	self.height=raw_input('ur height please')
	pc.input(self)

a=exe11()
for i in range(1,3):
    a.method()

