set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print("Set:",set1)

#length of a set
print("Length: ",len(set1))

# loop in set
print("Printing set items:")
for i in set1:
    print(i)

#check if the element present in set
print("if banana in set1:","banana" in set1)
print("if banana not in set1:","banana" not in set1)

# add item to set
set1.add("Kiwi")
print("After adding item:",set1)

# remove item from set1
set1.remove("cherry")
print("After removing an item:",set1)

# Add a list in set
list1=[1,2,3,4]
set1.update(list1)
print("After adding list:",set1)

# Joins in set
# Union(|)
set3 = set1.union(set2)
print("Union:",set3)

# Intersection(&)
set4 = set1.intersection(set2)
print("Intersection:",set4)

# Difference(-)
set5 = set1.difference(set2)
print("Difference:",set5)

# Symmetric Difference
set6 = set1.symmetric_difference(set2)
print("Symmetric Difference:",set6)

# subset and superset in frozenset
a = frozenset({1, 2})
b = frozenset({1, 2, 3})

print("Is Subset: ",a.issubset(b))
print("Is Superset: ",b.issuperset(a))
print("Is Disjoint: ",a.isdisjoint(b))