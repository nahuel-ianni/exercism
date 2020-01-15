import re as regex


def is_valid(isbn):
    pattern = "^([0-9]-*)([0-9]{3}-*)([0-9]{5}-*)([0-9]|X)$"
    formula = "(n0 * 10 + n1 * 9 + n2 * 8 + n3 * 7 + n4 * 6 + n5 * 5 + n6 * 4 + n7 * 3 + n8 * 2 + n9 * 1) % 11 == 0"
    result = False

    if regex.findall(pattern, isbn):
        isbn = isbn.replace("-", "")

        for index in range(0, len(isbn)):
            formula = formula.replace(f"n{index}", isbn[index])

        formula = formula.replace("X", "10")
        result = eval(formula)
        
    return result
