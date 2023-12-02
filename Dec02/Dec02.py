GAME_LABEL = "Game "
GAME_TO_TURN_SEPARATOR = ":"
TURN_SEPARATOR = ";"
QUESTION_CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14
}


class Pull:
    def __init__(self, pull_string):
        self.__pull_result = {}
        self.__set_pull_result(pull_string)

    def __set_pull_result(self, pull_string):
        for s in pull_string:
            split_tally = s.strip().split(" ")
            self.__pull_result[split_tally[1]] = int(split_tally[0])

    def get_pull_results(self):
        return self.__pull_result


class Turn:
    def __init__(self, turn_pulls):
        self.__pull_results = []
        self.__fill_turn_results(turn_pulls)

    def __fill_turn_results(self, turn_pulls):
        pulls_array = self.__split_turns_string(turn_pulls)
        for p in pulls_array:
            splited_pulls = self.__split_pulls(p)
            self.__pull_results.append(Pull(splited_pulls))

    def __split_turns_string(self, turns_string):
        return turns_string.strip().split(TURN_SEPARATOR)

    def __split_pulls(self, pulls_string):
        return pulls_string.strip().split(",")

    def __get_max_cube_color_per_turn(self):
        tally = {}
        for pull in self.__pull_results:
            pull_result = pull.get_pull_results()
            for color_count in pull_result:
                if (color_count not in tally):
                    tally[color_count] = pull_result[color_count]
                else:
                    tally[color_count] = tally[color_count] if tally[color_count] > pull_result[color_count] else pull_result[color_count]
        return tally

    def get_product_of_minimun_set_of_cubes(self):
        max_cube_color_count_in_turn = self.__get_max_cube_color_per_turn()
        product = 1
        for cube_color in max_cube_color_count_in_turn:
            amount_in_color = max_cube_color_count_in_turn[cube_color]
            product *= amount_in_color
        return product

    def is_cube_combination_possible_challenge01(self):
        max_cube_color_count_in_turn = self.__get_max_cube_color_per_turn()

        for cube_color in QUESTION_CUBES:
            if (cube_color in max_cube_color_count_in_turn):
                if (QUESTION_CUBES[cube_color] < max_cube_color_count_in_turn[cube_color]):
                    return False
        return True


class Game:
    def __init__(self, game_turn):
        game_array = self.__split_game_string(game_turn)
        self.__game_id = self.__set_game_id(game_array[0])
        self.__turn = Turn(game_array[1])

    def __split_game_string(self, game_string):
        return game_string.strip().split(GAME_TO_TURN_SEPARATOR)

    def __set_game_id(self, value):
        return int(value.replace(GAME_LABEL, ""))

    def get_game_id(self):
        return self.__game_id

    def is_game_cube_combination_possible_challenge01(self):
        return self.__turn.is_cube_combination_possible_challenge01()

    def get_game_product_of_minimun_set_of_cubes(self):
        return self.__turn.get_product_of_minimun_set_of_cubes()


class GameCollection:
    def __init__(self, text_input):
        self.__collection = []
        for s in text_input:
            self.__collection.append(Game(s))

    def append(self, game: Game):
        self.__collection.append(game)

    def challenge01(self):
        result = 0
        for g in self.__collection:
            if (g.is_game_cube_combination_possible_challenge01()):
                result += g.get_game_id()
        return result

    def challenge02(self):
        result = 0
        for g in self.__collection:
            result += g.get_game_product_of_minimun_set_of_cubes()
        return result


def read_file(txtFile):
    file = open(txtFile)
    data = file.readlines()
    file.close()
    return data


# challenge01: result: 8
# challenge02: result: 2286
# game02_text_input = read_file("Dec02/Dec02_Sample.txt")

# challenge01: result: 2149
# challenge02: result: 71274
game02_text_input = read_file("Dec02/Dec02.txt")

games = GameCollection(game02_text_input)
# print(f"result:{games.challenge01()}")

print(f"result:{games.challenge02()}")
