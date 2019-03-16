import re

# We will wrap World instance in order to get a better understanding of how it may work
# as well as a better compatibility with every other instance build afterward for this project
from typing import List

from myia.externals.helper import World
from myia.externals.parsing.parser import infos


class TextFileManager:

    def __init__(self, player_id):
        self.__player_id = player_id
        self.__world = World(player_id)

    def init_file(self):
        # Open info, question and response file in order to communicate with server
        return self.__world.init_file()

    def __get_data_from_info_file(self, file: str = 'infos.txt'):
        path = './{jid}/{file}'.format(jid=self.__player_id, file=file)
        with open(path, 'r') as f:
            return f.read().strip()

    @staticmethod
    def __parse_game_state_from_line(line: str):
        r = re.search(r'Tour:(?P<turn>[0-9]*),'
                      '.*Score:(?P<current_score>[0-9]*)/(?P<limit_score>[0-9]*),'
                      '.*Ombre:(?P<darkness>[0-9]*),'
                      '.*Bloque:{(?P<blocked>.*)}', line)

        if r is not None:
            return GameStartingState(
                int(r.group('turn')),
                int(r.group('current_score')),
                int(r.group('limit_score')),
                int(r.group('darkness')),
                [int(x) for x in r.group('blocked').split(',')],
                []
            )
        else:
            return None

    @staticmethod
    def __parse_character_position_from_line(line: str):
        user_starting_state = []
        for user in line.split(" "):
            if user is not None and user != '':
                user_starting_state.append(user.split("-"))

        return user_starting_state

    def get_starting_state(self):
        # Get starting state of the game
        info_data = self.__get_data_from_info_file()
        info_data = info_data.split("\n")
        if len(info_data) > 2:
            print(info_data)
            game_starting_state = self.__parse_game_state_from_line(info_data[1])
            if game_starting_state is None:
                return None
            game_starting_state.characters_states = self.__parse_character_position_from_line(info_data[2])
            return game_starting_state
        else:
            return None

    def get_history_from_info_file(self):
        return infos.all_turns(self.__player_id)

    def game_is_ongoing(self):
        # Check if info file is not empty (if false, then game is still ongoing)
        is_ongoing = not infos.game_over(self.__player_id)

        return is_ongoing

    def get_question(self):
        # Get line into 'questions.txt'
        return self.__world.pull_question()

    def write_response(self, response: str):
        self.__world.push_response(response)


class GameStartingState:
    turn: int
    current_score: int
    limit_score: int
    darkness: int
    blocked: List[int]
    characters_states: List[List[str]]

    def __init__(self, turn: int, current_score: int, limit_score: int,
                 darkness: int, blocked: List[int], users_states: List[List[str]]):
        self.turn = turn
        self.current_score = current_score
        self.limit_score = limit_score
        self.darkness = darkness
        self.blocked = blocked
        self.characters_states = users_states
