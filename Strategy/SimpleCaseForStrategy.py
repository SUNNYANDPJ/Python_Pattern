#coding:utf-8
'''
Created on 2015年8月14日

@author: sunny
'''

class Question(object):
    '''
    classdocs
    '''

    def __init__(self, admine=True):
        '''
        Constructor
        '''
        self._admin = admine
    
    def show(self):
        if self._admin is True:
            return "Show page with admin"
        else:
            return "show page with user"

if __name__ == '__main__':
    q = Question(admine = False)
    print q.show()