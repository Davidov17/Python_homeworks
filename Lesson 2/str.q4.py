word = str(input("Enter a word: "))
print(word[::-1])
if word[::-1] == word:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
