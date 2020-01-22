def equilateral(sides):
    return _guard_triangle_shape(sides) and len(set(sides)) == 1
    

def isosceles(sides):
    return _guard_triangle_shape(sides) and len(set(sides)) in (1, 2)


def scalene(sides):
    return _guard_triangle_shape(sides) and len(set(sides)) == 3


def _guard_triangle_shape(sides):
    s, m, l = sorted(sides)

    return all(side > 0 for side in sides) and s + m >= l 
