import random

secret = random.randint(1, 20)
tries = 0
guess = 0
print("Guessing a number between 1 and 20...")

while guess != secret:
    text = input("Your guess:")
    guess = int(text)

    tries += 1

    if guess < 1 or guess > 20:
        print("You guessed it out of the range!")
    elif guess < secret:
        print("Your guess is short.")
    elif guess > secret:
        print("Your guess is high.")
    else:
        print("Correct! In ", tries, "tries")
 
