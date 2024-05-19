list = ["banana","strawberry","mango","apple"]
intList = [1,6,2,7,3]

newlist = [i+"yes" for i in list if "t" in i]
# print(newlist)

intList = [2,23,4,1,2]
for i in intList:
     pass
    
newIntList = [i for i in intList]
# print(type(newIntList))

UpperNewList = [i.upper() for i in newlist]
# print(UpperNewList)

list.sort(key = str.upper)
intList.sort(reverse = True)
print(intList)
print(list)