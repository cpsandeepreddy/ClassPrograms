#!/usr/bin/python
#factor.py
#python program to print the factorial of a number.

class factor:
    def main(self,number):
	self.i=number
	i=2
	while self.i>=i:
	    if self.i%i==0:
		print i,
		self.i/=i
		i=2
		continue
	    i+=1

a=factor()
a.main(42)