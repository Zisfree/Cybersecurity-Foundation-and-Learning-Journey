import random

print("_______Number Guesser_______")

x = 75000000
for i in range(3):
    print("Choosing a random number between 1 - 100. Please wait....")
    for m in range(x):
        pass
print("Done!")

ranum = random.randint(1, 101)
guessn = 0
guess = 0
x = 0

while guess != ranum:
    guess = int(input("Your guess = "))
    if ranum >= guess:
        print("High")
    elif ranum <= guess:
        print("Low")
    guessn += 1

print(f"Correct! You took {guessn} attempts.")
