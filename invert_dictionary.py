#!/usr/bin/python
#invert_dictionary.py
#python program to print the dictionary swapping keys and values.

class invdict:
    def __init__(self,dic):
	add_dict={}
	keys=dic.keys()
	values=dic.values()
	for i in range(0,len(keys)):
	     add_dict[values[i]]=keys[i]
	print add_dict
a=invdict({'a':1,'b':2,'c':3})
	    
	