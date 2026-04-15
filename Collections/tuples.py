tp1 = ("apple","banana","cherry")
tp2 = (1,2,3)
print("Tuple: ",tp1)
# Accessing tuple items
print(tp1[1])
print(tp1[1:2])
print(tp1[:2])

# changing values in tuple
x = list(tp1)
x[1] = "Orange"
tp1 = tuple(x)
print("Upading:",tp1)

# Add a element
y = list(tp1)
y.append("kiwi")
tp1 = tuple(y)
print("Element added:",tp1)

# Remove element
z = list(tp1)
z.remove("apple")
tp1 = tuple(z)
print("Remove: ",tp1)

# Loop tuple
i=0
while i<len(tp1):
    print(tp1[i])
    i=i+1

# join 
tup3=tp1+tp2
print(tup3)