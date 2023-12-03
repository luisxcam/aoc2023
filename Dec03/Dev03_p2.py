from enum import Enum
GEAR_CHAR = "*"


class CharContextEnum(Enum):
    NUMERIC = 1
    GEAR = 2
    INVALID = 3


def read_file(txtFile):
    file = open(txtFile)
    data = file.readlines()
    file.close()
    return data


def get_char_context(char):
    if (char.isdigit()):
        return CharContextEnum.NUMERIC
    elif (char == GEAR_CHAR):
        return CharContextEnum.GEAR
    else:
        return CharContextEnum.INVALID


def scan_vertical_row(row, start_index, end_index):
    amount = 0
    locked = False
    for i in range(start_index, end_index + 1):
        char_context = get_char_context(row[i])
        if (locked == False and char_context == CharContextEnum.NUMERIC):
            amount += 1
        locked = char_context == CharContextEnum.NUMERIC
    return amount


def scan_around_symbol(prev_row, row, next_row, start_index, end_index):
    total = 0
    heat_map = {"above": 0, "bellow": 0, "next_to": 0}
    if (prev_row is not None):
        heat_map["above"] = scan_vertical_row(prev_row, start_index, end_index)
        total += heat_map["above"]

    if (next_row is not None):
        heat_map["bellow"] = scan_vertical_row(
            next_row, start_index, end_index)
        total += heat_map["bellow"]


def get_product_of_adjacent(prev_row, row, next_row, coord, row_length):
    max_index_value = row_length - 1
    start_index = coord - 1 if coord > 0 else 0
    end_index = coord + \
        1 if coord < max_index_value else max_index_value
    scan_around_symbol(prev_row, row, next_row, start_index, end_index)


def get_values_from_row(prev_row, row, next_row):
    row_length = len(row)
    result = 0
    for char_index in range(row_length):
        char = row[char_index]
        char_context = get_char_context(char)

        if (char_context != CharContextEnum.GEAR):
            continue

        result += get_product_of_adjacent(prev_row,
                                          row, next_row, char_index, row_length)
    return result


def get_product_of_gear(text_arr):
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


challenge_string = read_file("Dec03/Dec03.txt")  # 467835
sample_string = read_file("Dec03/Dec03_Sample.txt")  # ?
print(get_product_of_gear(sample_string))


# def is_symbol_in_range(row, start_index, end_index):
#     if (row is None):
#         return False

#     for i in range(start_index, end_index + 1):
#         char_context = get_char_context(row[i])
#         if (char_context == CharContextEnum.GEAR):
#             return True
#     return False


# def get_is_valid_from_adjacent_row(prev_row, next_row, row_length, coordinates):
#     max_index_value = row_length - 1
#     start_index = coordinates[0] - 1 if coordinates[0] > 0 else 0
#     end_index = coordinates[-1] + \
#         1 if coordinates[-1] < max_index_value else max_index_value

#     return is_symbol_in_range(prev_row, start_index, end_index) or is_symbol_in_range(next_row, start_index, end_index)
