import set_input_module


def two_set_operation(function_to_call, operation_: str = "") -> None:
    """Takes in a function and a string and calls the function for sets of two."""
    while True:
        try:
            print(operation_)
            print("Enter the two sets of numbers in the format: (1, 2, 3, 4, 5)(6, 7, 8, 9, 10)")
            print("Enter 'exit' to return to the main menu")
            user_input: str = input("< ").strip()
            if user_input == "exit":
                print("\n")
                return None
            else:
                list_input: list = set_input_module.num_to_data_list(f"({user_input})")

            if len(list_input) == 2:
                set_: str = str(
                    function_to_call(set(list_input[0]), set(list_input[1])
                                     )).replace("[", "").replace("]", "")
                print(set_)
                print(f"Cardinality: {len(function_to_call(set(list_input[0]), set(list_input[1])))}")
                print("\n")
                return None
            else:
                print("Invalid input")
                print("\n")
        except ValueError:
            print("Invalid input")
            print("\n")
