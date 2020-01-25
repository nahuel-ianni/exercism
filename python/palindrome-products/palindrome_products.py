def largest(min_factor, max_factor):
    combinations = _get_combinations(min_factor, max_factor)
    palindromes = _get_palindromes(combinations)

    return sorted(palindromes.items())[-1] if palindromes else (None, [])


def smallest(min_factor, max_factor):
    combinations = _get_combinations(min_factor, max_factor)
    palindromes = _get_palindromes(combinations)

    return sorted(palindromes.items())[0] if palindromes else (None, [])


def _get_combinations(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("The order of the parameter is inverted.")
    
    valid_combinations = []

    for x in range(min_factor, max_factor + 1):
        for y in range(min_factor, max_factor + 1):
            s = str(x * y)

            if s == s[::-1] and (y, x) not in valid_combinations:
                valid_combinations.append((x, y))

    return valid_combinations


def _get_palindromes(combinations):
    palindromes = {}

    for c in combinations:
        value = c[0] * c[1]

        if str(value) == str(value)[::-1]:
            if value in palindromes.keys():
                palindromes[value].append(c)
            
            else:
                palindromes.update({value: [c]})
    
    return palindromes
