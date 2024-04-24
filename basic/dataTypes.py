# type(x) -> helps to know the type of data variable x is
import random 

a = "Hello world" #string
b = 22 #integer
c = 20.5 #float
d = 124j #complex
e = ["1",2,"3",4.4] #list
f = ("1",2,3.3) #tuple
g = {               
    "name":"Ram", #dictionary
    "class":12
}

#type casting 
x = 12
x = str(x)
y = "12"
y = int(y)
y = float(y)
z = 19j #complex number cannot be type casted to another 
print(type(x))
print(x)
print(type(y))
print(y)
