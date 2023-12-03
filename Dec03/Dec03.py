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


def get_char_context(char):
    if (char.isdigit()):
        return CharContextEnum.NUMERIC
    elif (char == INVALID_CHAR):
        return CharContextEnum.INVALID
    else:
        return CharContextEnum.SYMBOL


def is_symbol_in_range(row, start_index, end_index):
    if (row is None):
        return False

    for i in range(start_index, end_index + 1):
        char_context = get_char_context(row[i])
        if (char_context == CharContextEnum.SYMBOL):
            return True
    return False


def get_is_valid_from_adjacent_row(prev_row, next_row, row_length, coordinates):
    max_index_value = row_length - 1
    start_index = coordinates[0] - 1 if coordinates[0] > 0 else 0
    end_index = coordinates[-1] + \
        1 if coordinates[-1] < max_index_value else max_index_value

    return is_symbol_in_range(prev_row, start_index, end_index) or is_symbol_in_range(next_row, start_index, end_index)


def get_values_from_row(prev_row, row, next_row):
    row_length = len(row)
    result = 0
    is_valid_for_sum = False
    prev_was_symbol = False
    num_store = ""
    coordinates = []
    for char_index in range(row_length):
        is_last_iteration = char_index == row_length - 1
        char = row[char_index]

        char_context = get_char_context(char)
        if (char_context == CharContextEnum.NUMERIC):
            coordinates.append(char_index)
            num_store += char

        if (len(num_store) > 0 and (char_context == CharContextEnum.SYMBOL or prev_was_symbol)):
            is_valid_for_sum = True

        if (not is_valid_for_sum and (char_context == CharContextEnum.INVALID or is_last_iteration) and len(num_store) > 0):
            is_valid_for_sum = get_is_valid_from_adjacent_row(
                prev_row, next_row, row_length, coordinates)

        if ((char_context != CharContextEnum.NUMERIC or is_last_iteration) and len(num_store) > 0 and is_valid_for_sum):
            result += int(num_store)
            num_store = ""
            coordinates = []
            is_valid_for_sum = False

        if (is_last_iteration or char_context == CharContextEnum.INVALID):
            num_store = ""
            coordinates = []
            is_valid_for_sum = False

        prev_was_symbol = char_context == CharContextEnum.SYMBOL
    return result


def get_sum_of_symbol_to_number(text_arr):
    result = 0
    prev_row = None
    for index in range(len(text_arr)):
        row = text_arr[index].strip()
        next_row = None
        if (index < len(text_arr) - 1):
            next_row = text_arr[index+1].strip()
        result += get_values_from_row(prev_row, row, next_row)
        prev_row = row
    return result


challenge_string = read_file("Dec03/Dec03.txt")  # 539713
sample_string = read_file("Dec03/Dec03_Sample.txt")  # 4361
print(get_sum_of_symbol_to_number(challenge_string))
