from enum import Enum
GEAR_CHAR = "*"
wfile = open("log.txt", "a")


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


def fetch_value_from_coord(row, found_index, max_index_value):
    num = row[found_index]
    for rindex in range(found_index, 0, -1):
        value = row[rindex-1]
        if get_char_context(value) == CharContextEnum.NUMERIC:
            num = value + num
        else:
            break
    for index in range(found_index + 1, max_index_value):
        value = row[index]
        if get_char_context(value) == CharContextEnum.NUMERIC:
            num += value
        else:
            break
    return num


def get_int_from_row(row, start_index, end_index, max_index_value):
    if (row is None):
        return []

    num = []
    locked = False
    for i in range(start_index, end_index + 1):
        char_context = get_char_context(row[i])
        if (locked == False and char_context == CharContextEnum.NUMERIC):
            value = fetch_value_from_coord(row, i, max_index_value)
            if (value is not None):
                num.append(value)
        locked = char_context == CharContextEnum.NUMERIC
    return num


def get_values_around_symbol(prev_row, row, next_row, start_index, end_index, max_index_value):

    numbers_from_prev_row = get_int_from_row(
        prev_row, start_index, end_index, max_index_value)
    numbers_from_in_row = get_int_from_row(row, start_index,
                                           end_index, max_index_value)
    numbers_from_next_row = get_int_from_row(next_row, start_index,
                                             end_index, max_index_value)
    return numbers_from_prev_row + numbers_from_in_row + numbers_from_next_row


def get_product_of_adjacent(prev_row, curr_row, next_row, coord, row_length):
    max_index_value = row_length - 1
    start_index = coord - 1 if coord > 0 else 0
    end_index = coord + \
        1 if coord < max_index_value else max_index_value

    values = get_values_around_symbol(prev_row, curr_row, next_row, start_index,
                                      end_index, max_index_value)

    if (len(values) < 2):
        return 0

    assert len(values) == 2, f"SOMETHING WENT WRONG! Got Length of {len(values)} for {
        values} from prev:{prev_row}, row:{curr_row}, or next{next_row}"

    wfile.write(f"Product for : {values[0]} and {values[1]}\n")
    return int(values[0]) * int(values[1])


def get_values_from_row(prev_row, row, next_row):
    row_length = len(row)
    result = 0
    for char_index in range(row_length):
        char = row[char_index]
        char_context = get_char_context(char)

        if (char_context != CharContextEnum.GEAR):
            continue

        wfile.write(f"----\n\n")
        wfile.write(f"Found * index:{char_index}\n")
        wfile.write(f"{prev_row}\n")
        wfile.write(f"{row}\n")
        wfile.write(f"{next_row}\n")

        product = get_product_of_adjacent(
            prev_row, row, next_row, char_index, row_length)
        result += product

        wfile.write(f"Product:{product}\n")
        wfile.write(f"Result from row: {result}\n")
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
        wfile.write(f"ROW-INDEX: {index}\n")
        wfile.write(f"Total Result: {result}\n")
        wfile.write(
            f"########~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        wfile.write("\n\n\n")
        prev_row = row
    return result


challenge_string = read_file("Dec03/Dec03.txt")  # 467835
sample_string = read_file("Dec03/Dec03_Sample.txt")  # ?
print(get_product_of_gear(challenge_string))
wfile.close()

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
