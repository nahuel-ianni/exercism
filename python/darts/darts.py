outer_circle_radius = 10
middle_circle_radius = 5
inner_circle_radius = 1

def score(x, y):
    point = (x ** 2 + y ** 2) ** 0.5

    if point > outer_circle_radius:
        return 0

    elif point > middle_circle_radius:
        return 1

    elif point > inner_circle_radius:
        return 5

    else:
        return 10
        