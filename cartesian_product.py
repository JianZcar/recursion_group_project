def cartesian_product(set_a, set_b) -> list:
    """Function to calculate the Cartesian product of two sets."""
    product_set = []
    (lambda: [
        product_set.append((element_a, element_b)) for index_a,
        element_a in enumerate(set_a) for index_b,
        element_b in enumerate(set_b)])()
    return product_set


def get_cartesian_product():
    """Function to take user input for sets A and B, calculate the Cartesian product, and find total cardinality."""
    inputs: list = [
        input("Enter elements for set A separated by commas: ").split(','),
        input("Enter elements for set B separated by commas: ").split(',')]
    product_set = cartesian_product(inputs[0], inputs[1])
    cardinality_set = len(product_set)
    return product_set, cardinality_set


if __name__ == '__main__':
    product, cardinality = get_cartesian_product()
    print("Cartesian product of set A and set B:", product)
    print("Total cardinality of the Cartesian product:", cardinality)
