#coding:utf-8
import abc

class VmReceiver(object):
    """description of class"""
    def start(self):
        print "Virtual machine start"

    def stop(self):
        print "Virtual machine stop"

class Command(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        pass

class StartVmCommand(Command):
    def __init__(self, receiver):
        self.recevier = receiver

    def execute(self):
        self.recevier.start()
     
class StopVmCommand(Command):
    def __init__(self, recevier):
        self.recevier = recevier

    def execute(self):
        self.recevier.stop()

class ClientInvoker(object):
    def __init__(self, command):
        self.command = command

    def do(self):
        self.command.execute()

if __name__ == "__main__":
    receiver = VmReceiver()
    start_cmd = StartVmCommand(receiver)
    client = ClientInvoker(start_cmd)
    client.do()

    stop_cmd = StopVmCommand(receiver)
    client.command = stop_cmd
    client.do()