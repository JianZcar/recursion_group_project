import mode_selector
import input_converter as ic
import cartesian_product as cp
import set_operations as so

modes_function: dict = {
    1: ["Cartesian Product", cp.cartesian_product],
    2: ["Intersection", so.set_intersection],
    3: ["Difference", so.set_difference],
    4: ["Union", so.set_union],
    5: ["Exit", exit]
}


def main():
    """Main function to run the program."""
    while True:
        mode: int = mode_selector.mode_selection([modes_function[x][0] for x in modes_function])
        print("\n")

        match modes_function[mode][0]:
            case "Exit":
                modes_function[mode][1]()
            case _:
                ic.two_set_operation(modes_function[mode][1], modes_function[mode][0])


if __name__ == '__main__':
    main()
