#coding:utf-8

import random

class BasicCourse(object):
	def get_labs(self):
		return "basic_course: labs"
	
	def __str__(self):
		return "BasicCourse"

class ProjectCourse(object):
	def get_labs(self):
		return "project_course: labs"

	def __str__(self):
		return "ProjectCourse"

class SimpleFactory(object):
	
	@staticmethod
	def create_course(type):
		if type == 'bc':
			return BasicCourse()
		elif type == 'pc':
			return ProjectCourse()
