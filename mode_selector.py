def mode_selection(modes: list) -> int:
    """Takes in a list of modes and returns the user's selection."""
    while True:
        print("Select mode:")
        for index, mode in enumerate(modes):
            print(f"{index + 1}. {mode}")
        try:
            user_input = int(input("< "))
            if len(modes) >= user_input > 0:
                return user_input
            else:
                print("Invalid input")
                print("\n")
        except ValueError:
            print("Invalid input")
            print("\n")


if __name__ == "__main__":
    # mode_selection()
    pass
