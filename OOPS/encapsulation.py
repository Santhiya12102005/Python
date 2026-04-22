class Sample:
    
    def __init__(self):
        self.__value = 10
        
    def change_value(self,value):
        self.__value = value

    def show(self):
        print("Value is : ",self.__value)
        
s = Sample()
s.show()
s.change_value(200)
print("After changing the value:")
s.show()
s.__value=20  # can't able to change private variable outside the class
s.show()
