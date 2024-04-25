string = "This is a string!"
string2 = " whitespace "
string3 = "Ram,Shyam,Hari"

length = len(string) #to find the length of a string
one = string[0] #show what character is at index '0'
present = "z" in string #checks if a string is present and returns true or false 
presento = "a" not in string #checks if a string is not present and returns true or false

slicing = string[:20] #slicing 
s = string[:-2] #negative slicing --> starts from the end of the string 

upper = string.upper() #modifies string to uppercase
lower = string.lower() #modifies string to lowercase

strip = string2.strip() #removes whitespace from the start and the end of the string

replace = string2.replace("white","black") #replaces string 
replace = replace.strip()

concat = string +"\n"+ string2 +"\n"+ string3

split = string3.split(",")

string4 = f"The number of index is {length}" #this is a format string, similar to template literals in javascript
string5 = f"the result for 23588235/23582835 is {23588235/23582835:.6f}"

string6 = "this is \"Sparta\"" # Escape string --> \n, \t, \"
string6 = string6.encode()
print(string6)
