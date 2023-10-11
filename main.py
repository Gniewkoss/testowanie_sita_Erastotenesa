def sito(number: int):
    primes = []
    for i in range(2, number + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

num = int(input("Podaj liczbę: "))

primes_list = sito(num)

for i in primes_list:
    print(i)
