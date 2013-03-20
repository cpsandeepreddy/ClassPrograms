#!/usr/bin/python
#argument_passing.py
#python program for passing the arguments.

class exe13:
    def pc(self):
    	from sys import argv
    	self.script,self.first,self.second,self.third=argv
class main(exe13):
    def method(self):
	exe13.pc(self)
	print 'Script name is ',self.script
	print 'First argumrent is ',self.first
	print 'second argument is ',self.second
	print 'Third argument is ',self.third
a=main()
a.method()

	
