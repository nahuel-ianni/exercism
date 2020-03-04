def primes(limit, p = 2):
    numbers = [n for n in range(p, limit + 1)]

    while p < limit + 1:
        for value in range(p, limit + 1, p):
            value = value + p
            if value not in numbers: 
                continue
            
            numbers[numbers.index(value)] = 0

        p += 1

    return [n for n in numbers if n != 0]
