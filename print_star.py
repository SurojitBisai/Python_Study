# rows = int(input("Enter the number of rows:-"))
# k = 0
# for i in range (1,rows + 1):
#    for j in range (rows - i):
#     print(end = " ")
#     while(k != 2 * - 1):
#        for k in range (2 * i - 1):
#         print(" * ", end = " ")
#         k += 1
#         k = 0
#         print( )

rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end=" ")
    
    # Print stars
    for k in range(2 * i - 1):
        print("*", end=" ")
    
    # Move to the next line after each row
    print()
