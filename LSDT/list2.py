list1 = ["banana","strawberry","mango","apple"]
intList = [1,6,2,7,3]

newlist = [i+"yes" for i in list1 if "t" in i]
# print(newlist)

intList = [2,23,4,1,2]
for i in intList:
     pass
    
newIntList = [i for i in intList]
# print(type(newIntList))

UpperNewList = [i.upper() for i in newlist]
# print(UpperNewList)

list1.sort(key = str.upper)
intList.sort(reverse = True)


# l = list(list1)
l = list1.copy()
l2 = list1 + intList

l.extend(l2)
print(l)
print((l.count(4)))

print(list1.index("apple"))