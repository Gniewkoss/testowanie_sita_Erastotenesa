def sieve_of_eratosthenes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p**2 <= n:
        if is_prime[p]:
            for i in range(p**2, n+1, p):
                is_prime[i] = False
        p += 1
    return [i for i in range(2, n+1) if is_prime[i]]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def process_prime_numbers(primes):
    for num in primes:
        if is_prime(num):
            print(num)

if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
        primes = sieve_of_eratosthenes(n)
        process_prime_numbers(primes)
    except ValueError:
        print("Error: Please enter a valid number.")
