import random

print(".: THE HIGHER LOWER GAME :.")
print("---------------------------")
print("Welcome to the Higher Lower \nGame. I  will  randomize  a \nnumber between  0  and  99. \nCan you guess it?")
print("---------------------------")

rand_num = random.randint(0, 100)
guesses = 0

while True:
    guess = int(input("Your guess > "))
    guesses += 1
    if guess < rand_num:
        print("HIGHER!")
    elif guess > rand_num:
        print("LOWER!")
    else:
        print("---------------------------")
        print(str(guess) + " is correct!")
        print("It took you " + str(guesses) + " guesses.")
        print("Good job!")
        break

