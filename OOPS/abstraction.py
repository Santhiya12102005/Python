from abc import ABC,abstractmethod

class Abs:

    @abstractmethod
    def show(self):
        pass

class Sample:
    def show(self):
        print("This is Sample class")

class Test:
    def show(self):
        print("This is Test class")

s = Sample()
t = Test()
s.show()
t.show()