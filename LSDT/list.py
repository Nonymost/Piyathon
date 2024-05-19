#List are ordered, changeable and allow duplicate values, is index
fruits = ["apple","pineapple","sweetapple",420] 

#accessing list items 
apple, pineapple = fruits[0],fruits[1] 

# List constructer to create list 
l = list(("ram","shyam","hari")) 

#negative indexing --> starts from the end 
neg = l[-1] , l[-2] 
print(neg)
# print(fruits)

#range of index
ind = l[-3:-1]
print(ind)
# print("banana" in l)

#changing values in a list 
l[0] = "abhinav" 

l[1:2] = ["sabirn" , "abhirn" , "devrin"]
print(l)
l[0:2] = ["haerin"]
# print(len(l))
# print(l)

#inserting new values to certain index in a list 
lis = list(("this","is","a","test"))
lis.insert(2,"not")
# print(lis) #--> outputs this , is , not , a , test

#adding values to a list 
lis.append("!")
# print(lis)   #--> outputs this , is , not , a , test , !

l.extend(lis) #--> extends list by appending the values of another iterables(list,tuple,dictionary,sets)

lis.remove("not") #--> outputs this , is , a , test , !
lis.pop()         #--> outputs this , is , a , test 
print(lis.pop(1))        #--> outputs this , a , test
print(lis)
del lis[2]
# del lis
print(lis)
lis.clear()
l.clear()
print(l)

