# Arithmetic Operators
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("Addition: ",(a+b))
print("Subraction: ",(a-b))
print("Multiplication: ",(a*b))
print("Division: ",(a/b))
print("Modulus: ",(a%b))
print("Exponential: ",(a**b))
print("Floor division: ",(a//b))

""" 
Assignment Operators:
= : Assign the value
+=: add and assign
-= : subract and assign
*= : multiply and assign
/=: divide and assign
%= : modulus and assign
//=: floor divition and assign
** = : exponential and assign
"""

"""
Comparision:
== : Equal
!= : Not equal
> : greater than
< : less than
>= : greater than or equal to
<= : lessthan or equal to
"""

"""
Logical: returns only true/false
and: if both are true
or: true <- if any one statement is true
not: reverse of the result true->false, false->true
"""

"""
identity and membership: returns only true/false
is: true if both variables are in same object
is not: false if both variables are not in same object

in: True if a sequence with the specified value is present in the object
not in: True if a sequence with the specified value is not present in the object
"""

"""
Bitwise:
&: AND -> Sets each bit to 1 if both bits are 1
|: OR -> Sets each bit to 1 if one of two bits is 1
^: XOR -> Sets each bit to 1 if only one of two bits is 1
<< : Left shift -> Shift left by pushing zeros in from the right
>> : Right shift -> Shift right by pushing copies of the leftmost bit in from the left
~: NOT -> Invert all the bits
"""

"""
Ternary operator:
value_if_true if condition else value_if_false
"""
max = a if a>b else b
print("Maximum",max)