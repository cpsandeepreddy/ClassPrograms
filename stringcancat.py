#!/usr/bin/python
#stringcancat.py
#python program to perform the string concatenation.

class pc:
    def pcm(self):
	print 'mary had a little lamb'
	print 'its flence was white as snow'
	print 'mAnd every where mary want'
	print '$'*20

class main(pc):
    def method(self):
	pc.pcm(self)
	end1='a'
	end2='s'
	end3='h'
	end4='o'
	end5='k'
	print end1+end2+end3+end4+end5
	pc.pcm(self)
a=main()
a.method()
