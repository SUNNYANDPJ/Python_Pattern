#coding:utf-8
import abc

class Worker(object):

    __metaclass__ =  abc.ABCMeta

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def work(self):
        pass

class Employe(Worker):
    __metaclass__ = abc.ABCMeta

    def work(self):
        print "Employ: %s start to work" %self.name

class Leader(Worker):

    def __init__(self, name):
        self.members = []
        super(Leader, self).__init__(name)

    def add_member(self, employe):
        if employe not in self.members:
            self.members.append(employe)

    def remove_member(self, employe):
        if employe in self.members:
            self.members.remove(employe)

    def work(self):
        print "Leader:%s start to work"%self.name
        for employe in self.members:
            employe.work()

if __name__ == "__main__":
    e1 = Employe("e1")
    e2 = Employe("e2")
    l1 = Leader("l1")
    l1.add_member(e1)
    l1.add_member(e2)

    e3 = Employe("e3")
    l2 = Leader("l2")
    l2.add_member(e3)
    l2.add_member(l1)

    l2.work()