import pytest
from main import sieve_of_eratosthenes
from main import is_prime
from main import process_prime_numbers

@pytest.fixture
def inputs():
    return [sieve_of_eratosthenes(i) for i in range(2, 1000)]

@pytest.fixture
def not_prime_inputs():
    return [i for i in range(2, 1000) if i not in sieve_of_eratosthenes(i)]

@pytest.fixture
def primes():
    return sieve_of_eratosthenes(1000)

def test_sieve_is_prime(inputs):
    for primes_list in inputs:
        for num in primes_list:
            assert is_prime(num)


def test_is_prime_false(not_prime_inputs):
    for num in not_prime_inputs:
        assert is_prime(num) == False

def test_process_prime_numbers(capsys, primes, not_prime_inputs):

    process_prime_numbers(primes)
    captured = capsys.readouterr()

    expected_output = '\n'.join(map(str, primes))
    assert captured.out.strip() == expected_output

    process_prime_numbers(not_prime_inputs)
    captured = capsys.readouterr()

    assert captured.out.strip() == ''


def test_sieve_of_eratosthenes(inputs):
    for primes_list in inputs:
        for num in primes_list:
            assert num in primes_list