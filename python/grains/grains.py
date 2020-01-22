min_range = 1
max_range = 64

def square(number):
    if number < min_range or number > max_range:
        raise ValueError("The requested square is outside the existing range.")

    return _getGrainsAndTotalOnSquare(number)[0]


def total():
    return _getGrainsAndTotalOnSquare(max_range + 1)[1]


def _getGrainsAndTotalOnSquare(square):
    grains_sum = 0
    grains = 1
    
    for square in range(min_range, square):
        grains_sum += grains
        grains *= 2
    
    return (grains, grains_sum)
