tems = int(input("how many temps"))
result = list(map(lambda x : 2 ** x, range(tems)))
print("The total terms are", tems)
for i in range (tems):
 print ("2 raised to power", 1, "is",result[i])

