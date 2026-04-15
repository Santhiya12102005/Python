a = [1,2,3,4]
b = [5,6,7,8]

# append()
a.append(10)
print("Append : ",a)

# copy()
c = a.copy()
print("copy : ",c)

# count
print("count:",a.count(3))

# extend
e=(20,30)
b.extend(e)
print("extend:",b)

# index
print("index :",a.index(3))

# insert
a.insert(0,0)
print("insert: ",a)

# pop
print("pop:",a.pop())
print(a)

# remove
a.remove(2)
print("remove:",a)

# reverse
b.reverse()
print("reverse:",b)

# sort
b.sort()
print("sort:",b)

# clear
a.clear()
print("Clear: ",a)

# join the lists
list1 = [1,2,3,4]
list2 = ["apple","banana","cherry"]
list3 = list1 + list2
print("List Join:",list3)

# looping list
print("Printing elements in list:")
[print(x) for x in list2]