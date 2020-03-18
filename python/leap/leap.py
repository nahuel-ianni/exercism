def leap_year(year):
    check1 = is_divisible(year, 4) and not is_divisible(year, 100)
    check2 = is_divisible(year, 400)

    return check1 or check2


def is_divisible(a: int, b: int) -> bool:
    return (a % b) == 0
