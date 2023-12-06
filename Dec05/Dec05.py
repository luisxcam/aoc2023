import re


def read_file(txt_file):
    file = open(txt_file)
    data = file.readlines()
    file.close()
    return data


def get_numbers_from_string(text_input):
    return list(map(int, re.findall(r'\d+', text_input)))


def get_dictionary_of_maps(text_input):
    seeds = list(
        map(int, re.findall(r'\d+', text_input.pop(0).split(":")[1].strip())))
    idx = -1
    maps_dictionary = []
    for s in text_input:
        if (s is None):
            continue
        if (s[0].isnumeric()):
            maps_dictionary[idx if idx >= 0 else 0].append(
                get_numbers_from_string(s))
        if (s[0].isalpha()):
            idx += 1
            maps_dictionary.append([])

    print(maps_dictionary)
    return (seeds)


def challenge01(text_input):
    get_dictionary_of_maps(text_input)


challenge_string = read_file("Dec05/Dec05.txt")  # 21919
sample_string = read_file("Dec05/Dec05_Sample.txt")  # 13

print(challenge01(sample_string))
