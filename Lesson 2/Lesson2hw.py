# Q1
number = float(input("number:"))
print(round(number,2))
# Q2
number1 = float(input("number:"))
number2 = float(input("number:"))
number3 = float(input("number:"))
print(max(number1,number2,number3), min(number1,number2,number3))
# Q3
distanceinkim = float(input("distance in kim:"))
print(distanceinkim*1000, distanceinkim*100000)
# Q4
x = float(input("Enter a number: "))
y = float(input("Enter a number: "))
integer = x // y
remainder = x % y
print(integer, remainder)
# Q5
temperature = float(input("Enter temperature in Celsius: "))
fahrenheit = (temperature * 9 / 5) + 32
print(fahrenheit)
# Q6
number = float(input("Enter a number: "))
last_digit = number % 10
print(last_digit)
# Q7
number = float(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# strq1
name = str(input("What is your name? "))
year_of_birth = int(input("What is your year of birth? "))
from datetime import date
today = date.today()
print("Your age is: ", today.year-year_of_birth)

# strq2
txt = "LMaasleibtui"
print(txt[1]+txt[3]+txt[5]+txt[7]+txt[8]+txt[10])
print(txt[0]+txt[2]+txt[4]+txt[6]+txt[9]+txt[9]+txt[11])

# strq3
string = str(input("Enter a string: "))
length1 = len(string)
print(string.upper())
print(string.lower())

# strq4
word = str(input("Enter a word: "))
print(word[::-1])
if word[::-1] == word:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")

# strq5
word = str(input("Enter a word: "))
vowels = ['a', 'e', 'i', 'o', 'u']
consanants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
word.vowels = vowels
word.consanants = consanants
print(len(word.vowels))
print(word.consanants)

# strq6


# strq7
sentence = "I love apples"
replacement = "oranges"
sentence = "I love " + replacement
print(sentence)

# strq8
string = str(input("Enter a string: "))
print(string[0],string[-1])

# strq9
string = str(input("Enter a string: "))
print(string[::-1])

# strq10
sentence =  str(input("Enter a sentence: "))
print(len(sentence))

# strq11
string = str(input("Enter a string: "))
string.isdigit()
if string.isdigit():
    print("String has a digit.")
else:
    print("String does not have a digit.")

# strq12
words = str(input("Enter words: "))
print(words.split())

# strq13
string = str(input("Enter a string: "))
print(string.replace(" ", "")   )

# strq14
x = str(input("enter a string"))
y = str(input("enter another string"))
if x == y:
    print("x and y are equal")
else:
        print("x and y are not equal")

# strq15
sentence =  str(input("enter a sentence"))
def sentence_acronyms(sentence):
    sentence_acronyms = ''.join(word[0].upper() for word in sentence.split())
    return sentence_acronyms
print(sentence_acronyms(sentence))

# strq16
string = str(input("Enter a string: "))
character = "a"
from os import remove
remove(character)
print(string)

# strq17
string = str(input("Enter a string: "))
trnslte = str.maketrans ( {"a" : "*", "e" : "*", "i" : "*", "o" : "*", "u" : "*"})
result = string.translate(str.maketrans(trnslte))
print(result)

# strq18
sentence = str(input("Enter a sentence: "))
starting_word = sentence.split()[0]
ending_word = sentence.split()[-1]
print("Starts with: ", starting_word)
print("End with: ", ending_word)

# boolq1
username = str(input("Enter your username: "))
password = str(input("Enter your password: "))
print(bool(username))
print(bool(password))

# boolq2
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
if number1 == number2:
    print("they are equal")
else:
    print("they are not equal")

# boolq3
number = int(input("Enter a number: "))
if number % 2 == 0 and number > 0:
    print(bool(number))
else:
    print("False")

# boolq4
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
number3 = int(input("Enter another number: "))
if number1 != number2 and number1 != number3 and number2 != number3:
    print("True")
else:
    print("False")

# boolq5
word1 = str(input("Enter a word: "))
word2 = str(input("Enter another word: "))
if len(word1) == len(word2):
    print ("True")
else:
    print ("False")

# boolq6
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("True")
else:
    print("False")

# boolq7
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
if number1 + number2 > 50.8:
    print("True")
else:
    print("False")

# boolq8
number = int(input("Enter a number: "))
if 10<=number<=20:
    print("True")
else:
    print("False")
