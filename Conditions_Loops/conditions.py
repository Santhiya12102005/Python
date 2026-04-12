a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

# even or odd
if a%2 == 0:
    print(a,"is Even")
else:
    print(a,"is Odd")

# positive or negative
if a < 0:
    print(a,"is Negative")
else:
    print(a,"is Positive")

# Greaterthan value
if a>b and a>c:
    print("A is Greater")
elif b>a and b>c:
    print("B is Greater")
else:
    print("C is Greater")

# Grade 
avg = (a+b+c)/3
if avg>=90 and avg<=100:
    print("A+")
elif avg>=80 and avg<=90:
    print("A")
elif avg>=70 and avg<=80:
    print("B+")
elif avg>=60 and avg<=70:
    print("B")
elif avg>=50 and avg<=60:
    print("C")
else:
    print("D")

# in and not in 
fruits = ["apple","banana","cherry"]
fruit = ["banana"]
ans = "apple" in fruits
print(ans)
ans = "apple" not in fruit
print(ans)

# string 
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)