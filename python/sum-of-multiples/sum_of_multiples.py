def sum_of_multiples(limit, multiples):
    multiples = [i for i in multiples if i != 0]

    return sum(i for i in range(0, limit) if next((m for m in multiples if i % m == 0), 0) != 0)
