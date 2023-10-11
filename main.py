def sito(number: int):
    primes = []
    for i in range(2, number + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

print(sito(10))