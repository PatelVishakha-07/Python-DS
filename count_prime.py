# Sieve of Eratosthenes

n = int(input("enter no: "))

prime = [True] * (n+1)
prime[0], prime[1] = False, False

for i in range(2, n + 1):
    if prime[i]:
        print(i,end = " ")

        for j in range(i*2, n+1, i):
            prime[j] = False

