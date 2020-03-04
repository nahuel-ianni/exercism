def primes(limit):
    numbers = set(range(2, limit + 1))
    multiples = { multiple for n in numbers for multiple in range(n * 2, limit + 1, n) }
    
    return sorted(numbers - multiples)
