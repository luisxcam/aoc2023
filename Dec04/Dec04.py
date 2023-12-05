import re


def read_file(txt_file):
    file = open(txt_file)
    data = file.readlines()
    file.close()
    return data


def get_numbers_from_string(text_input):
    return list(map(int, re.findall(r'\d+', text_input)))


def get_card_score(winning_numbers, participating_numbers):
    acc = 0
    for wn in winning_numbers:
        if wn in participating_numbers:
            acc = acc * 2 if acc > 0 else 1
    return acc


def challenge01(txt_input):
    total_card_score = 0
    for t in txt_input:
        game_to_card_split = t.strip().split(":")
        winning_to_card_numbers_split = game_to_card_split[1].split("|")
        winning_numbers = get_numbers_from_string(
            winning_to_card_numbers_split[0])
        participating_numbers = get_numbers_from_string(
            winning_to_card_numbers_split[1])
        total_card_score += get_card_score(winning_numbers,
                                           participating_numbers)
    return total_card_score


challenge_string = read_file("Dec04/Dec04.txt")  # 21919
sample_string = read_file("Dec04/Dec04_Sample.txt")  # 13

print(challenge01(challenge_string))
