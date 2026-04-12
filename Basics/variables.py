a = 5
b = "Word"
print(a)
print(b)

""" Variables do not need to declare, 
# it change their type after they have been set """
x = 5
x = "Word"
print(x) # o/p : Word

# Case Sensitive
a = 5
A = 6
print(a)
print(A) # A will not overwrite a

# Local and Global variables
p = 10
def show():
    p = 20
    print("Local variable:",p )

show()
print("Global variable:",p)

d = 10
def display():
    global d
    d = 80
    print("Global declaration:",d) # o/p : 80
display()
print(d) # o/p : 80

# Assingn Multiple values
i,o,p = 'A','B','C'
print(i,o,p)

u = v = 10
print(u,v) # same values for u and v