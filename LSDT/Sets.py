set1 = {"apple","banana","cherry"}
set2 = set(("cat","dog","cow"))


# for i in set1:
#     print(i)

txt = f"the sets are: {set1}"
# print(txt)
# print("banana" in set1)
# print(str.index())

set3 = {"Name",}
set3.add("Class")
set3.update(set1)
set3.remove("apple") #--> will remove the apple from the set
set3.discard("apple") #--> will also remove apple from the set but if not exist will not throw an error
set3.pop() #--> will remove/pop items in random order
set3.clear() #-> will clear all the items
del set3 #--> will delete the set. will cause error if printed after this 
# print(set3) 

setA = {"a","b","c"}
setB = {"b","a","e","g"}
setC = {1,2,3}
AnB = setA.intersection(setB)
AUB = setA.union(setB,setC)
AdiffB = setA.difference(setB)
symetric = setA.symmetric_difference(setB)

print(AnB)
print(AUB)
print(AdiffB)
print(symetric)