import random

l = ["failed", "success"]

ranum = random.randint(0, 100)

f = 0
s = 0
for i in range(ranum):
    ranword = random.choice(l)

    if ranword == "failed":
        f += 1
    elif ranword == "success":
        s += 1
print("Total attempts: ", f+s)
print("Successfull: ", s)
print("Failed: ", f)
