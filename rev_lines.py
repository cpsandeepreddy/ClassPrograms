#!/usr/bin/python
#rev_lines
#python program to reverse the lines.

class rev_lines:
     def read1(self,file):
	self.f=file
	fd=open(self.f,'r')
	txt=fd.read()
	return txt
class main(rev_lines):
    def method(self,nam):
	data=rev_lines.read1(self,nam)
	lst=data.split('\n')
	lst.reverse()
	for i in lst:
	    print i

a=main()
a.method('gr.txt')