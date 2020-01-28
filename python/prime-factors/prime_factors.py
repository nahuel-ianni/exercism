def factors(value):
    prime_factors = []
    divisor = 2

    while value != 1 or divisor <= value:
        if value % divisor == 0:
            value /= divisor
            prime_factors.append(divisor)
    
        else:
            divisor += 1

    return prime_factors
