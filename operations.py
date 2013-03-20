#!/usr/bin/python
#operations.py
#python program to perform arithmetic operations.

class exe3:
    def __init__(self):
	pass
    def add(self,a,b):
	print a+b
    def sub(self,a,b):
	print a-b
    def div(self,a,b):
	print a/b
class method(exe3):
    def exe2(self,l,m):
	exe3.add(self,l,m)
	exe3.sub(self,l,m)
	exe3.div(self,l,m)	


a=method()
a.exe2(6,2)

	