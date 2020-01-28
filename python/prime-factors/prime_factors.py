def factors(value):
    prime_factors = []
    divisor = 2

    while divisor <= value:
        while value % divisor == 0:
            value /= divisor
            prime_factors.append(divisor)
    
        divisor += 1

    return prime_factors
