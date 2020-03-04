def primes(limit):
    numbers = set(range(2, limit + 1))
    composite_numbers = { composite for n in numbers for composite in range(n * 2, limit + 1, n) }
    
    return sorted(numbers - composite_numbers)
