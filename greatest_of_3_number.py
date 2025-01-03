a = int(input("enter the first number"))
b = int(input("enter th second number"))
c = int(input("enter the third number"))
d = int(input("enter the forth number"))
if(a >= b and  a >= c and a >= d):
    print("first number  is largest", a)
elif(b >= c):
    print("second number is largest", b)
elif(c >= d):
    print("third number is largest", c)
else:
    print("forth number is largest", d)