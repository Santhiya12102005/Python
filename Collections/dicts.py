dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# print key + value
print(dict)

# get function
print("get function:",dict.get("model"))

# add new item to dict
dict["color"] = "Red"       #dict.update({"color": "Red"})
print("After adding new element:",dict)

# return values
print("get values:",dict.values())

# changing values in dict
dict["year"] = 2023         #dict.update({"year": 2023})
print("After making changes:",dict)

# check if key exist
if "model" in dict:
    print("Yes, Key exist")


# deleting item from dict
dict.pop("color")
print("After popping:",dict)

# multiple dictionaries
students = {
    "stud1" : {
        "name" : "ravi",
        "age" : 23
    },
    "stud2" : {
        "name" : "kumar",
        "age" : 24
    }
}

print("multiple dictionaries:",students)

# Access items in nested dictionaries
#print(students["stud1"]["name"])
print("Items in Nested Dictionaries:")
for k,v in students.items():
    print(k)
    for i in v:
        print(i+':',v[i])

# set default function
print("Set Default:",dict.setdefault("color","Red"))
print(dict)