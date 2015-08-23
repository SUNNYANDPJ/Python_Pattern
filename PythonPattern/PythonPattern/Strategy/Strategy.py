#coding:utf-8
'''
Created on 2015��8��14��

@author: sunny
'''
import abc
class AbsShow(object):
    '''
    classdocs
    '''
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def show(self):
        pass

class AdmineShow(AbsShow):
    def show(self):
        return "show the admine"
    
class UserShow(AbsShow):
    
    def show(self):
        return "show the user"

class Question(object):
    def __init__(self, show_obj):
        self.show_obj = show_obj
        
    def show(self):
        return self.show_obj.show()
    
if __name__=='__main__':
    q = Question(show_obj=AdmineShow())
    print q.show()
    q.show_obj = UserShow()
    print q.show()