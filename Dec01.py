import time


def measure_performance(f):
    start_time = time.perf_counter()
    f()
    end_time = time.perf_counter()
    print(f"ellapsed: {end_time - start_time}")


def read_file(txtFile):
    file = open(txtFile)
    data = file.readlines()
    file.close()
    return data


challenge_string = read_file("Dec01.txt")


def cleanse_string(txt):
    return txt.strip()


def reverse_string(txt):
    return txt[::-1]


def get_first_number_from_string(str):
    for s in range(len(str)):
        if str[s].isnumeric():
            return str[s]
    return None


def get_first_and_last_numeric(input_string):
    clean_string = cleanse_string(input_string)
    first = get_first_number_from_string(clean_string)
    inverted_string = reverse_string(clean_string)
    last = get_first_number_from_string(inverted_string)
    if (last is None):
        last = first
    return int(str(first) + str(last))


def sum_values_in_range(arr):
    acc = 0
    for r in arr:
        acc += get_first_and_last_numeric(r)
    return acc


def challenge_wrapper():
    sum_values_in_range(challenge_string)


measure_performance(challenge_wrapper)

result_challenge_01 = sum_values_in_range(challenge_string)
assert result_challenge_01 == 55834, f"Result from challenge 01 should be 55834 but it was {
    result_challenge_01}"
print(f"First Challenge Result: {result_challenge_01}")


# def get_number_strings():
#     file_num = read_file("Dec01Numbers.txt")
#     string_num = []
#     for s in file_num:
#         string_num.append(cleanse_string(s))
#     return string_num


# numbers_in_string = get_number_strings()


# number_to_str = ['one', 'two', 'three', 'four',
#                  'five', 'six', 'seven', 'eight', 'nine']
# number_to_str_backwards = ['eno', 'owt', 'eerht',
#                            'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']
# str_to_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# def find_alpha(vstr, nts):
#     placements = []
#     for s in range(len(nts)):
#         try:
#             val = vstr.index(nts[s])
#         except:
#             val = None
#         if val is not None:
#             placements.append([val, str_to_number[s]])
#     if len(placements) <= 0:
#         return None
#     index = 9999
#     val = 0
#     for v in range(len(placements)):
#         ind = placements[v][0]
#         if ind < index:
#             index = ind
#             val = placements[v][1]
#     if index == 9999:
#         return None
#     return [index, val, nts[val-1]]


# def reverse_the_string(vstr):
#     return vstr[::-1]


# def find_reverse_alpha(vstr):
#     v = find_alpha(reverse_the_string(vstr), number_to_str_backwards)
#     if v is None:
#         return None
#     v[0] = len(vstr) - len(v[2]) - v[0] + 1
#     return v


# def get_value_from_str2(vstr):
#     first = None
#     last = None
#     for s in range(len(vstr)):
#         if (vstr[s].isnumeric()):
#             val = int(vstr[s])
#             if val >= 0 and val < 10:
#                 if first is None:
#                     first = [s, val, 'isNumeric']
#                 else:
#                     last = [s, val, 'isNumeric']
#     if last is None and first is not None:
#         last = first
#     return [first, last]


# def get_all_arr(vstr):
#     first_str = find_alpha(vstr, number_to_str)
#     last_str = find_reverse_alpha(vstr)
#     if first_str is None:
#         first_str = last_str
#     if last_str is None:
#         last_str = first_str

#     num = get_value_from_str2(vstr)
#     first = -1
#     last = -1
#     if (first_str is not None and len(first_str) > 0):
#         if num[0] is None:
#             first = first_str[1]
#         else:
#             if (first_str[0] > num[0][0]):
#                 first = num[0][1]
#             else:
#                 first = first_str[1]
#     else:
#         first = num[0][1]
#     if (last_str is not None and len(last_str) > 0):
#         if num[1] is None:
#             last = last_str[1]
#         else:
#             if (last_str[0] < num[1][0]):
#                 last = num[1][1]
#             else:
#                 last = last_str[1]
#     else:
#         last = num[1][1]

#     return int(str(first) + str(last))


# def calc_from_range2(arr):
#     acc = 0
#     for r in range(len(arr)):
#         vstr = get_all_arr(arr[r])
#         acc = acc + int(vstr)
#     return acc


# letter_sample_should_be_281 = ['two1nine', 'eightwothree', 'abcone2threexyz',
#                                'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']
# print(calc_from_range2(letter_sample_should_be_281))
# print(calc_from_range2(challenge_string))
