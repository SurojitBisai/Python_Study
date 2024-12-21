x = int(input("enter 1'st number"))
y = int(input("enter 2'st number"))
z = int(input("enter 3'st number"))
if(x >= y) and (x >= z) :
    largest = x
elif (y >= x) and (y >= z):
    largest = y
else:
    largest = z
print("the larges number is ", largest)