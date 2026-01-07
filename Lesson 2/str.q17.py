string = str(input("Enter a string: "))
trnslte = str.maketrans ( {"a" : "*", "e" : "*", "i" : "*", "o" : "*", "u" : "*"})
result = string.translate(str.maketrans(trnslte))
print(result)