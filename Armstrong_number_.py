num = int (input("Enter a number:-"))
sum = 0
temp = num 
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print("It is an Armstrong number")
else:
    print("It is not Armstrong number")


# Python program to check if the number is an Armstrong number or not

# take input from the user
# num = int(input("Enter a number: "))

# initialize sum
# sum = 0

# find the sum of the cube of each digit
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10

# display the result
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")

