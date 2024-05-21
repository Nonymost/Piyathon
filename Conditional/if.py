# x = int(input("Enter a number:\n"))

# if x == 0:
#     print("Enter a non-zero value::")
# elif x<0:
#     print(x, "Lower than zero (negative)")
# else:
#     print(x, "Greater than zero (positive)")


a = 3
b = 3
c = 3

# if a>b: print("a is greater") #short hand if statement
# print("a is greater than b") if a>b else print("b is greater than a") #shorthand if else statement
# print("a is greater") if a>b else print("equals") if a==b else print("b is greater")   ->multiple if else condition

# if a==b and a==c:
#     print("all are equal")
# elif a>b and a>c:
#     print("a is greater than both")
# elif a>b or a>c:
#     print("a is greater than one out of the two")
# else:
#     print("a is smaller")
    
if not a>=b and not a>=c:
    print("a is smaller")
elif a==b==c:
    print("all are equal")
else:
    print("a is greater")