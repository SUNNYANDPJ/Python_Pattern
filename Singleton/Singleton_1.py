#coding:utf-8
class Singleton(object):
	class _A(object):
		def __init__(self):
			pass

		def display(self):
			return id(self)

	_instance = None
	
	def __init__(self):
		if Singleton._instance is None:
			Singleton._instance = Singleton._A()
	
	def __getattr__(self,attr):
		return getattr(self._instance, attr)
