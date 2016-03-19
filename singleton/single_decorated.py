#coding: utf8

class SingleClass:
    def __init__(self, cls):
        self.cls = cls

    def Instance(self):
        try:
            return self._instance
        except:
            self._instance = self.cls()
            return self._instance

    def __call__(self):
        raise TypeError("EOFError")

@SingleClass
class A:
    def __init__(self):
        pass

    def display(self):
        return id(self)


if __name__ == "__main__":
    a = A.Instance()
    b = A.Instance()
    print id(a), a.display()
    print id(b), b.display()
