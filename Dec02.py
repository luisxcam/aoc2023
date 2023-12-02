# To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

# You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

# For example, the record of a few games might look like this:

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

# In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

# The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

# In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once;
# similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

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

    def is_cube_combination_possible_in_turn(self):
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

    def is_game_cube_combination_possible(self):
        return self.__turn.is_cube_combination_possible_in_turn()


class GameCollection:
    def __init__(self, text_input):
        self.__collection = []
        for s in text_input:
            self.__collection.append(Game(s))

    def append(self, game: Game):
        self.__collection.append(game)

    def get_id_sum_for_possible_games(self):
        result = 0
        for g in self.__collection:
            if (g.is_game_cube_combination_possible()):
                result += g.get_game_id()
        return result


def read_file(txtFile):
    file = open(txtFile)
    data = file.readlines()
    file.close()
    return data


# challenge01: result: 8
# game02_text_input = read_file("Dec02_Sample.txt")
# challenge01: result: 2149
game02_text_input = read_file("Dec02.txt")

games = GameCollection(game02_text_input)
# print(f"result:{games.get_id_sum_for_possible_games()}")
