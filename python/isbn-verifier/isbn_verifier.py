def is_valid(isbn):
    result = False    
    isbn = _parse_ISBN(isbn)

    if len(isbn) == 10:
        operation_check = (isbn[0] * 10 + isbn[1] * 9 + isbn[2] * 8 + isbn[3] * 7 + isbn[4] * 6 + isbn[5] * 5 + isbn[6] * 4 + isbn[7] * 3 + isbn[8] * 2 + isbn[9] * 1)
        result = operation_check % 11 == 0

    return result


def _parse_ISBN(isbn):
    if not isbn:
        return list()

    try:
        isbn = list(isbn.replace("-", ""))

        if isbn[-1] == "X":
            isbn[-1] = 10

        result = list(map(int, isbn))

    except ValueError:
        result = list()

    return result#list(map(int, isbn))
