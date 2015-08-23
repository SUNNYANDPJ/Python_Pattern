#coding:utf-8
import abc

class Fishing(object):
    """description of class"""
    __metaclass__ = abc.ABCMeta
    def finishing(self):
        self.prepare_bait()
        self.go_to_riverbank()
        self.find_location()
        print("Start fishing")

    @abc.abstractmethod
    def prepare_bait(self):
        pass

    @abc.abstractmethod
    def go_to_riverbank(self):
        pass

    @abc.abstractmethod
    def find_location(self):
        pass

class JohnFishing(Fishing):
    def prepare_bait(self):
        print "John: buy bait from Taobao"
    
    def go_to_riverbank(self):
        print "John: to river by driving"
        
    def find_location(self):
        print "John: select location on the island"
        
class SunnyFinishing(Fishing):
    def prepare_bait(self):
        print "Sunny: buy bait from Taobao"
    
    def go_to_riverbank(self):
        print "Sunny: to river by driving"
        
    def find_location(self):
        print "Sunny: select location on the island"
     
if __name__ == "__main__":
    john = JohnFishing()
    john.finishing()

    sunny = SunnyFinishing()
    sunny.finishing()
