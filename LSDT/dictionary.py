#-------------creating dictionary-----------

dict0 = {
    "name" : "ramesh",
    "class" : "jhakass",
    "tuple" : ("one","two","three")
}

dict1 = dict(name="ramu",grade="jamu",list=["2",1])

newList = []
for x in dict0["tuple"]:
    newList.append(x)

# print(newList)

# print(dict0.keys()) -->outputs keys in a dictionary
# print(dict0.values()) --> outputs values in a dictionary

if 'ramesh' in dict0.values():
    # print(dict0.items())
    pass

#---------adding key and value in dictionary--------------

dict2 = dict(what = "name",name = "cl")

#------------updating key and values in dictionary-----------

dict2.update({"name":"Who"}) #-> updating items in a dictionary, if no key:value is present then will create a new one
dict2["what"] = "Idk"  #-> changing items in a dictionary, same as above
dict2["check"] = "one" #-> will add a new key with value
dict2.update({"model":"new","test":"okay?"}) #-> same as above but allows multiple creation at once

for x in dict2.items():
    # print(x)
    pass

#------------removing items from the dictionary-------------

dict2.pop("test") #-> will pop the specified key
del dict2["check"] 
dict2.popitem() #->will pop the last item inserted
dict2.clear() #-> will clear the dictionary
# del dict2 

dict2.update({"name":"Ramu","age":"Navanu"})
for values in dict2:
    # print(values)
    pass

for x, y in dict2.items():
    # print(x, y)
    pass

dict1.clear()
dict2.clear()

#------------Copying items from another dictionary
dict2.update({"name":"Rames","class":"jj"})
dict1 = dict2.copy()
dict3 = dict(dict1)

dict3.clear()

dict3 = {           #dictionary nesting
    "name" : "Ramesh",
    "list" : {
        "fruits" : ["Apple","oranges","mangoes"],
        "drink" : ["softdrink","harddrink","juice"]
    }
}

# print(dict3["list"]["fruits"])
# print(dict3.get("name"))






    
    