fruits = ["apple","banana","orange","pineapple"]
vegetable = ["lettuce","spinach"]
string = "Hello, this is a string"

for fruit in fruits:
    pass

temp = ""

for s in vegetable:
    for i in fruits:
        temp += f"{s,i}"
else:
    print(temp)
