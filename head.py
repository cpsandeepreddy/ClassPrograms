#!/usr/bin/python
#head.py
#python program to open the file, reading and printing.

class head:
    def read1(self,file):
	self.f=file
	fd=open(self.f,'r')
	txt=fd.read()
	return txt
class main(head):
    def method(self,nam,line):
	data=head.read1(self,nam)
	self.line=line
	s=''
	count=0
	for i in data:
	    if i!='\n':
		s=s+i
	    else:
		 print s
		 s=''
		 count+=1
	         if count==self.line:
		     break

a=main()
a.method('reverse.txt',5)