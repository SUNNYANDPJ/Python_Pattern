#coding:utf-8
from Singleton_1 import Singleton as single
from Singleton_1_1 import Singleton as single1

def main():
	
	"""Singleton test"""
	s1 = single()
	s2 = single()
	print id(s1),s1.display()
	print id(s2),s2.display()
	
	s1 = single1()
	s2 = single1()
	print id(s1),s1.display()
	print id(s2),s2.display()

if __name__ == '__main__':
	main()
