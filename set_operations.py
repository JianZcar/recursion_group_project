def set_intersection(set_a: set, set_b: set) ->tuple:
    """Function to find the intersection of two sets."""
    return tuple(set_a.intersection(set_b))


def set_difference(set_a: set, set_b: set) -> tuple:
    """Function to find the difference of two sets."""
    return tuple(set_a.difference(set_b))


def set_union(set_a: set, set_b: set) -> tuple:
    """Function to find the union of two sets."""
    return tuple(set_a.union(set_b))
