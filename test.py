a = 10

def function():
    a = 20
    global b
    b = 22
    print("The answer is :",a)

function()

print("The answer here is :",a)
print("The answer here is :",b)
