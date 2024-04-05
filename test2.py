#string

a = " ram singh"
 
upper = a.upper() # changes value to uppercasing 
lower = a.lower()  #changes value to lowercasing
noWhiteSpace = a.strip() #removes the whitespace before and after the string but not inbetween
replaceString = noWhiteSpace.replace("r","shy") #replaces specified old string with new string
splitString = replaceString.split(" ") #splits string into two or more list items with the help of the specifier. Here " " which is a space 
concatenation = "Ram "+"Dev" #string concatenation

print(upper)
print(lower)
print(noWhiteSpace)
print(replaceString)
print(splitString)
print(concatenation)
