import re


def read_file(txt_file):
    file = open(txt_file)
    data = file.readlines()
    file.close()
    return data


def get_numbers_from_string(text_input):
    return list(map(int, re.findall(r'\d+', text_input)))


def get_matching_amount(winning_numbers, participating_numbers):
    acc = 0
    for wn in winning_numbers:
        if wn in participating_numbers:
            acc += 1
    return acc


def fetch_card_values(card):
    game_to_card_split = card.strip().split(":")
    winning_to_card_numbers_split = game_to_card_split[1].split("|")
    winning_numbers = get_numbers_from_string(
        winning_to_card_numbers_split[0])
    participating_numbers = get_numbers_from_string(
        winning_to_card_numbers_split[1])
    return (winning_numbers, participating_numbers)


def challenge02(txt_input):
    original_set_amount = len(txt_input)
    my_cards = [1] * original_set_amount
    for idx, card in enumerate(txt_input):
        winning, participating = fetch_card_values(card)
        score = get_matching_amount(winning, participating)
        if (score == 0):
            continue
        to_add = my_cards[idx]
        for offset in range(score):
            my_cards[idx + offset + 1] += to_add
    return (sum(my_cards))


challenge_string = read_file("Dec04/Dec04.txt")  # 9881048
sample_string = read_file("Dec04/Dec04_Sample.txt")  # 30

print(challenge02(challenge_string))
