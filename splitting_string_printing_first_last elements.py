#!/usr/bin/python
#splitting_string_printing_first_last elements.py
#python program to print the first and last elemts by splitting the string.

class word:
    def word(self,a):
	self.word=a
    def break1(self,wor):
	brwo=wor.split()
	return brwo
    def sort(self,str):
	brwo=str.split()
	return sorted(brwo)

class main(word):
    def method(self,str):
	self.lst=word.break1(self,str)
	self.sort=word.sort(self,str)
	print 'Befoer sorting list is\n',self.lst
	print 'After sorting list is\n',self.sort
	last=self.lst[len(self.lst)-1]
	print 'Before sorting last element is:\n',last
	first=self.lst[0]
	print 'Before sorting first element is:\n',first
	sort_last=self.sort.pop(-1)
	print 'After sorting last element is:\n',sort_last
	sort_first=self.sort[0]
	print 'After sorting first element is:\n',sort_first
a=main()
a.method('sandeep reddy chinna papanna sree vidya nikethan')