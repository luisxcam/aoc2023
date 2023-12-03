from enum import Enum
INVALID_CHAR = "."


class CharContextEnum(Enum):
    NUMERIC = 1
    SYMBOL = 2
    INVALID = 3


def read_file(txtFile):
    file = open(txtFile)
    data = file.readlines()
    file.close()
    return data


challenge_string = read_file("Dec03/Dec03.txt")
sample_string = read_file("Dec03/Dec03_Sample.txt")


def get_char_context(char):
    if (char.isnumeric()):
        return CharContextEnum.NUMERIC
    elif (char == INVALID_CHAR):
        return CharContextEnum.INVALID
    else:
        return CharContextEnum.NUMERIC


def get_values_from_row(row, next_row):
    max_length = len(row)
    store = ""
    isValidSymbol = False
    isInvalidChar = False
    for char_index in len(row):
        char_context = get_char_context(char_index[row])

    return 1


def get_sum_of_symbol_to_number(text_arr):
    result = 0
    for index in range(len(text_arr)):
        next_row = None
        if (index < len(text_arr) - 1):
            next_row = text_arr[index+1].strip()
        result += get_values_from_row(text_arr[index].strip(), next_row)
    return result


print(get_sum_of_symbol_to_number(sample_string))
