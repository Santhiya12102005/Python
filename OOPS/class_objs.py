class person:
        x = 10
        def show(self):    # self -> refers to object p1
                return "In show Function"
        
        def __init__(self,name=None,rollno=None):
                self.name = name
                self.rollno = rollno
                

p1 = person()
p2 = person("Sandy","23BCS075")
print(p1.x)
print(p1.show())
print(p2.show())

# __init__()
print("P2 Name is:",p2.name)
print("P2 rollno is:",p2.rollno)



