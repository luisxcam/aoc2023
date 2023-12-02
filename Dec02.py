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


class Turn:
    def __init__(self, turn_pulls):
        self.__turn_results = []
        self.__fill_turn_results(turn_pulls)

    def __fill_turn_results(self, turn_pulls):
        pulls_array = self.__split_turns_string(turn_pulls)
        for p in pulls_array:
            splited_pulls = self.__split_pulls(p)
            tally = self.__split_pull_tally(splited_pulls)
            self.__turn_results.append(tally)

    def __split_turns_string(self, turns_string):
        return turns_string.strip().split(TURN_SEPARATOR)

    def __split_pulls(self, pulls_string):
        return pulls_string.strip().split(",")

    def __split_pull_tally(self, split_pulls):
        tally = {}
        for s in split_pulls:
            split_tally = s.strip().split(" ")
            tally[split_tally[1]] = int(split_tally[0])
        return tally


class Game:
    def __init__(self, game_turn):
        game_array = self.__split_game_string(game_turn)
        self.__game_id = self.__set_game_id(game_array[0])
        self.turn = Turn(game_array[1])

    def __split_game_string(self, game_string):
        return game_string.strip().split(GAME_TO_TURN_SEPARATOR)

    def __set_game_id(self, value):
        return int(value.replace(GAME_LABEL, ""))

    def get_game_id(self):
        return self.__game_id


class GameCollection:
    def __init__(self):
        self.__collection = []

    def append(self, game: Game):
        self.__collection.append(game)


def read_file(txtFile):
    file = open(txtFile)
    data = file.readlines()
    file.close()
    return data


game02_text_input = read_file("Dec02.txt")


def create_game_data(game02_text_input):
    games = GameCollection()
    for s in game02_text_input:
        games.append(Game(s))


games = create_game_data(game02_text_input)
