num = int (input("how many trems"))
n1, n2 = 0,1
count = 0
if num <= 0:
    print("entre a positive integer:")
elif num == 1:
    print("Fibonacci sequence uoto", num)
    print(n1)
else:
    print("Fibonacci sequencci sequence")
    while count < num:
        print(n1)
        result = n1 +n2
        n1 = n2
        n2 = result
        count += 1




