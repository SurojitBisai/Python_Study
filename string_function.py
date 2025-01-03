#str.endswith("er.") #returns true if string ends with substr
str = " I am studying python from ApnaCollege"
print(str.endswith("ege"))
print(str.endswith("college"))
print(str.endswith("apna"))

# # #str.capitalizes()#apitalizes 1st char
str = "i am studying python from ApnaCollege"
# str = str.capitalize()
print(str.capitalize())
print(str)

# #str.replace(old,new)
str = "I am studying python from ApnaCollege"
print(str.replace("o", "a"))
print(str.replace("python", "java"))

# str.find(word) #returns 1st index of 1st occurrer
str = "I am from python from ApnaCollege"
print(str.find("from"))
print(str.find("apnacollee"))

#str.count("am") #count the occurrence of substr
str = "I am from python from ApnaCollege"
print(str.count("o"))


