def show():
    print("This is Show function")
show()

def add(x,y):
    print("Addition of two:",x+y)
add(10,20)

def eligibility(age):
    if age >= 18:
        print("You're eligible")
    else:
        print("You're not eligible")
Input = int(input("Enter your age:"))
eligibility(Input)

# *args and ** kwargs

def fun(*data):
    sum=0

    for i in data:
        sum+=i
    return sum

print(fun(10,20,30))


def details(**data):
     for keyword,value in data.items():
         print("%s:%s"%(keyword,value))   ## print(f"{keyword}:{value}")

details(name="Sandy",rollno="727623bcs075",dept="CSE",age=21)