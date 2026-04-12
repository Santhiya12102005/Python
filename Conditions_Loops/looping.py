a = int(input("Enter a:"))

#while loop(Square of a numbers)
i=1
while i<=a:
    print(i*i)
    i+=1

#for loop(multiplication of a num)
num = int(input("Enter a num:"))

print(f"Multiplication of a {num} is :")
for i in range(1,11):
    print(f"{i} * {num} = {i*num}")

#while with break
print("with break:")
i=1
while i<6:
    print(i)
    if i == 3: break
    i+=1

#for with continue
print("With continue:")
for k in range(1,6):
    if k==3:
        continue
    print(k)

# for loop in list
ls = [10, 20, 30, 40]
print("Values in the list :")
for i in ls:
    print(i)

# for loop in tuple
tup = (1, 2, 3, 4)
print("Values in the tuple :")
for i in tup:
    print(i)

# for loop in set
s = {100, 200, 300, 400}
print("Values in the set :")
for i in s:
    print(i)

# for loop in dict
d = {'a': 1, 'b': 2, 'c': 3}
print("loop only keys")
for i in d:
    print(i)

print("loop only values")
for i in d.values():
    print(i)

print("loop key + value")
for key, value in d.items():
    print(key, value)