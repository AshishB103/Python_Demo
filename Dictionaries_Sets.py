##Dictionaries
from itertools import count

student = {
    "Name": "Alan",
    "Subjects" : {
               "maths" : 89,
                "Science" : 76,
                  "Chemistry" : 65},
    "Class" : 9
}

print(student["Subjects"]["Science"])
print(student.keys())
print(student.values())
print(list(student.keys()))
print(len(student))
print(len(list(student.keys())))
print(student.items())
print(list(student.items()))
pairs = list(student.items())
print(pairs[0])
##print(student["Name2"]) #gives error since key does not exist
print(student.get("Name2")) #gives none if key does not exist

student.update({"City" : "Jaisalmer"})

#Sets
collection = {1,2,3,4,5, "Sun", 4 , "moon"}
print(collection)
print(type(collection))
print(len(collection))

new_collection = set()
new_collection.add(1)
new_collection.add(2)
new_collection.add(2)
new_collection.add((1,2,3))
#new_collection.add([1,2,3])  - cannot add list in the set, since list is mutable and unhashable, whereas SET is immutable/hashable
print(new_collection)
new_collection.clear()
print(new_collection)

set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))

story = {
    "table" : ["a piece of furniture", "list of facts and figures"],
    "cat" : "a small animal"
}
print(story)
print(type(story))


set = {"Java", "C++", "Python", "JavaScript"}
print(set)
print(len(set))