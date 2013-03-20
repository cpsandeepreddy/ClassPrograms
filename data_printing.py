#!/usr/bin/python
#data_printing.py
#python programme for data printing.

class ch1:
    def ch_and_cra(self, a,b):
	self.a=a
	self.b=b
	print 'cheese are',self.a,'crackers are',self.b
class dir(ch1):
    def count(self):
	ch1.ch_and_cra(self,20,30)
class sup(ch1):
    def math1(self):
	chese=100
	crackers=200
	ch1.ch_and_cra(self, chese,crackers)
class main(dir,sup):
    def method(self):
	dir.count(self)
	sup.math1(self)
aa=main()
aa.method()
	