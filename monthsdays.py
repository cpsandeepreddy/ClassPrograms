#!/usr/bin/python
#monthsdays.py
#python program to print the days of the months.

class pc:
    def month(self):
	print 'months are \n' ,self.month
    def days(self):
	print 'days are', self.days

class exe9(pc):
    def method(self):
	self.days=' mon tue we thurs fri satur sun'
	self.month='jan\nfeb\nmar\napril\nmay\n'
	pc.month(self)
	pc.days(self)
a=exe9()
a.method()