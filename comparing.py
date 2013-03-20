#!/usr/bin/python
#comparing.py
#python program for comparing two strings.

class dec:
    def method(self,people,cats):
	self.people=people
	self.cats=cats
    def print1(self):
	if self.people<self.cats:
	    print 'cats are more'
	elif self.people>self.cats:
	    print 'mans are more'
	else:
	    print 'both are equal'
a=dec()
a.method(20,30)
a.print1()