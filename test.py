#coding:utf-8
from Singleton_1 import Singleton as single
from Singleton_1_1 import Singleton as single1
from Singleton_2 import Singleton as single2

@single2
class S2(object):
	def __init__(self):
		pass
	def display(self):
		return id(self)

def main():
	
	"""Singleton test"""
	print "1\n"
	s1 = single()
	s2 = single()
	print id(s1),s1.display()
	print id(s2),s2.display()
	
	print "2\n"
	s1 = single1()
	s2 = single1()
	print id(s1),s1.display()
	print id(s2),s2.display()

	
	print "3\n"
	s1 = S2.Instance()
	s2 = S2.Instance()
	print id(s1),s1.display()
	print id(s2),s2.display()


if __name__ == '__main__':
	main()
