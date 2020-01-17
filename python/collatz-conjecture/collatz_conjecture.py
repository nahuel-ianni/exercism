def steps(number, step = 0):
    guard_value(number)

    if number == 1:
        return step

    return steps(number / 2 if number % 2 == 0 else 3 * number + 1, step + 1)
    

def guard_value(number):
    if number < 1:
        raise ValueError("Value cannot be lower than 1")
