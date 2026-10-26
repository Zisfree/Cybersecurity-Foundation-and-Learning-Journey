num = int(input())

a = 0
for primes in range(2, num):
    a = True
    for divisor in range(2, primes):
        if primes%divisor == 0:
            a = False
    if a == True:
        print(primes)
