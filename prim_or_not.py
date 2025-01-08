num = int(input("enter the number :-"))
flog =0
if(num > 1):
    for i in range (2, num):
        if(num % i == 0):
            flog = 1
            break
    if flog == 1:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")