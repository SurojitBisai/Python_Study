my_str = input("Enter a string:-")
words = [word.lower() for word in my_str.split()]
words.sort()
print("The sorted words are:")
for word in words:
    print(word)
    
#The quick brown fox jump over a lazy dog

# my_str = input("Enter a string: ")
# words = [word.lower() for word in my_str.split()]
# words.sort()
# print("The sorted words are:")
# for word in words:
#     print(word)
