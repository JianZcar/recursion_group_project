class ParenthesisNumber:
    """Class to keep track of the number of parenthesis and their indexes."""
    def __init__(self):
        self.open_par = 0
        self.close_par = 0
        self.open_index = 0
        self.close_index = 0
        self.open_anchor = 0
        self.close_anchor = 0

    def reset(self):
        self.open_par = 0
        self.close_par = 0
        self.open_index = 0
        self.close_index = 0
        self.open_anchor = 0
        self.close_anchor = 0


def append_to_list(input_list: list, input_str: str) -> None:
    """Takes in a list and a string and appends the string to the list."""
    if is_number(input_str):
        input_list.append(int(input_str))
    else:
        input_list.append(input_str)


def valid_input() -> str:
    """Takes in a string of numbers and symbols and returns and checks for invalid input."""
    while True:
        user_input = input("Enter a set: ")
        for x in user_input:
            if x not in "0123456789,()abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                print("Invalid input")
        return user_input


def is_number(input_str: str) -> bool:
    """Takes in a string and returns True if it is a number."""
    try:
        int(input_str)
        return True
    except ValueError:
        return False


def str_int(input_str: str, input_list: list):
    """Takes in a string of numbers and converts them to integers and appends them to a list."""
    if input_str != "":
        for x in input_str.split(", "):
            if x != "(" or x != ")" or x != ",":
                append_to_list(input_list, x)


def num_to_data_list(input_set: str, number_list: list = None,
                     par_num: ParenthesisNumber = ParenthesisNumber()) -> list:

    """Takes in a string of numbers and symbols and returns a list of numbers properly formatted."""

    if number_list is None:
        number_list = []

    for index, character in enumerate(input_set):
        if character == "(":
            par_num.open_par += 1
            par_num.open_index = index
        elif character == ")":
            par_num.close_par += 1
            par_num.close_index = index

        if (par_num.open_par - par_num.close_par) == 1 and par_num.open_par >= 1 and index != len(input_set) - 1:
            if character == ")":
                number_list.append(input_set[par_num.open_anchor:par_num.close_index + 1])
                par_num.close_anchor = index

        elif (par_num.open_par - par_num.close_par) == 2 and character == "(":
            par_num.open_anchor = index

        elif par_num.open_par == par_num.close_par:
            if par_num.open_par == 1:
                str_int(input_set[par_num.open_index + 1:par_num.close_index], number_list)
            elif input_set[par_num.close_anchor + 3:index] != "":
                str_int(input_set[par_num.close_anchor + 3:index], number_list)

        if index + 3 <= len(input_set) and (par_num.open_par - par_num.close_par) <= 1:
            if character + input_set[index + 1] + input_set[index + 2] == ", (":
                if par_num.close_anchor == 0:
                    str_int(input_set[par_num.open_index + 1:index], number_list)
                elif par_num.close_anchor != 0:
                    str_int(input_set[par_num.close_anchor + 3:index], number_list)

    else:
        if par_num.open_par != par_num.close_par:
            par_num.reset()
            raise ValueError

    for index_2, item in enumerate(number_list):
        if type(item) == str and item[0] == "(" and item[-1] == ")":
            number_list[index_2] = []
            num_to_data_list(item, number_list[index_2], ParenthesisNumber())
    return number_list


if __name__ == '__main__':
    # print(num_to_data_list("(1, (2, 3, (4, 5, 6), 7), 8, (9, 10, 11), 12)"))
    number = valid_input()
    print(number)
    print(num_to_data_list(number), "Type : ", type(num_to_data_list(number)))
