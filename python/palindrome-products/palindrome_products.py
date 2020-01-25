def largest(min_factor, max_factor):
    _guard_min_max(min_factor, max_factor)


def smallest(min_factor, max_factor):
    _guard_min_max(min_factor, max_factor)



def _guard_min_max(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("The order of the parameter is inverted.")
