num = int(input("Enter the number:-"))
factorial = 1
if num < 0:
    print("Enter the prositive integer value:")
elif num == 0:
    print("The falctorial of 0 is 1")
else:
    for i in range (1, num+1):
     factorial = factorial * i
print("The factorial of", num, "is", factorial)


# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 5

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

