#!/usr/bin/python
#reading_and_writing_a_file.py
#python program to perform reading and writing operations on file.\

class read:
    def meth(self):
	from sys import argv
	self.script,self.fil=argv
	fd=open(self.fil)
	self.txt=fd.read()
class writ(read):
    def meth1(self):
	from sys import argv
	self.script,self.fil=argv
	fd1=open(self.fil,'a')
	line1='sree vidyanikethan'
	fd1.write(line1)
class main(writ):
    def method(self):
	writ.meth1(self)
	read.meth(self)
	print self.txt
a=main()
a.method()

	