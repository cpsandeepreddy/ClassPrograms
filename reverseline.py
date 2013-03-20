#!/usr/bin/python
#reverseline.py
#python program to reverse the lines.

class reverse:
    def read1(self,file):
	self.f=file
	fd=open(self.f,'r')
	txt=fd.read()
	return txt
class main(reverse):
    def method(self,nam):
	data=reverse.read1(self,nam)
	s=''
	for i in data:
	    if i!='\n':
		s=s+i
	    else:
		l=list(s)
		l.reverse()
		temp=''
		for j in l:
		    temp=temp+j
		print temp
	        s=''

a=main()
a.method('reverse.txt')