#!/usr/bin/python
#printing_data_in_file.py
#python program to print the data of file.

class file:
    def rea(self):
    	from sys import argv
    	self.script,self.fil=argv
    	fd=open(self.fil)
    	self.txt=fd.read()
class exe15(file):
    def method(self):
	file.rea(self)
	print 'file name: ',self.fil
	print self.txt

a=exe15()
a.method()
    
