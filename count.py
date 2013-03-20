#!/usr/bin/python
#count.py
#python program to count the strings in the line.

class strcou:
    def method(self,str):
	self.str=str
	a=self.str.split()
	temp=[]
	for i in a:
	    temp.append(i)
	    if temp.count(i)==1:
		print i,a.count(i)

z=strcou()
z.method("""sandeep reddy chinna papanna svec tirupathi
krishna puram""")