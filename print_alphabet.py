row = int(input("Enter the number of row"))
ascii_value = 65
for i in range(row):
    for j in range(i + 1):
        alphabet = chr(ascii_value)
        print(alphabet, end = " ")
    ascii_value +=  1
    print("\n")
