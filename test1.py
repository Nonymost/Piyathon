#Casting

#--> Casting is the process of changing the data type of one variable to another.
# It can be achieved with the int(), float(), str() functions

# x = int(input("Enter a number \n"))
# y = float(input("Enter any decimal value \n"))
z = 18
z = str(z)

# print(x,y,z)
# print(type(x), type(y), type(z))

#Multiline String 
 
a = """Thisstringlt'scheck"""

# print(len(a))
if((" " not in a)): # this syntax help to check if a value is within a string or not 
    print(a[4:10]) #slicing is python is done using the syntax var[index:index]
    print(a[:10]) # var[:index] slices from the start to the index 
    print(a[4:]) #var[index:] slices from the index to the end of the index
else:
    print("Bye")