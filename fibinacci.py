#!/usr/bin/python
#fibinacci.py
#python program to print fibinacci series.

class fibinacci:
    def __init__(self):
	pass
    def series(self,n):
	self.number=n
	print 0,
	ele=0
	printers=1
	fib=1
	while printers<n:
	    print fib,
	    temp=fib
	    fib=fib+ele
	    ele=temp
	    printers+=1
a=fibinacci()
a.series(10)
	    
	    
	    
		