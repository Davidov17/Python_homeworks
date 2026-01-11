# q2
for i in range(5):
    if i == 3:
        break
    print(i)
# q3
# for loop
for i in range(5):
    print(i)

# while loop
i = 0
while i < 5:
    print(i)
    i += 1
# q4
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
# hw1
list1 = [1, 1, 2]
list2 = [2, 3, 4]

result = []

for x in list1:
    if x not in list2:
        result.append(x)

for x in list2:
    if x not in list1:
        result.append(x)

print(result)
# hw2
n = 5

for i in range(1, n):
    print(i * i)
# hw3
txt = "hello"
vowels = "aeiou"
result = ""
count = 0

for i in range(len(txt)):
    result += txt[i]
    count += 1

    if count == 3 and i != len(txt) - 1:
        if txt[i] in vowels:
            continue
        result += "_"
        count = 0

print(result)
# hw4
import random

while True:
    number = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        guess = int(input("Guess the number: "))

        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print("You guessed it right!")
            break

        attempts -= 1

    if attempts == 0:
        print("You lost. Want to play again?")

    choice = input().lower()
    if choice not in ['y', 'yes', 'ok']:
        break

# hw5
password = input("Enter password: ")

if len(password) < 8:
    print("Password is too short.")
elif not any(ch.isupper() for ch in password):
    print("Password must contain an uppercase letter.")
else:
    print("Password is strong.")
# hw6
for num in range(2, 101):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
# hw6
for num in range(2, 101):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)

# bonus question
import random

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

while player_score < 5 and computer_score < 5:
    player = input("rock, paper, or scissors: ").lower()
    computer = random.choice(choices)

    print("Computer chose:", computer)

    if player == computer:
        print("Tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print("Score:", player_score, "-", computer_score)

print("Game over!")
