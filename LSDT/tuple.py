t = (12,3,"hello","5")
t1 = tuple(("this","can","be","a","test"))

# if "a" in t1:
#     print("is available")


# copying tuple and changing the data type of tuple as it is immutable and unchangeable
# to update a tuple one must change it to list  

l = list(t)
l[0] = "changed"
t = tuple(l)
# print(t)

# print(t + t1)
del t 

#packing and unpacking tuples
a = ("this","is","packing","!") #-> this is packing, adding values to the tuple
(one,two,*three) = a 

# Looping through tuple

# for i in range(len(a)):
#     print(str(i) +" "+a[i])

# i = 0
# while i < len(a):
#     print(str(i)+" "+a[i])
#     i += 1 

print(a.index("is"))
