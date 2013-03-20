#!/usr/bin/python
#listsort.py
#python program to sort the list.

class sort:
    def parentmethod(self,l):
	self.list=l
	return self.list.sort()
class main(sort):
    def method(self,lst):
        self.lst=lst
	print 'list before sorting is :',self.lst
	lst=sort.parentmethod(self,lst)
	print 'list after sorting is: ',lst

a=main()
a.method([1,5,3,2,7])
	