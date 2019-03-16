from typing import List

from myia.game_element.Board import Board
from myia.game_element.BoardFactory import BoardFactory
from myia.io.MoveHistory import MoveHistory
from myia.io.TextFileManager import GameStartingState


class Game:
    __current_turn: int = 0
    __limit_score: int = 0
    __current_score: int = 0
    __map: Board = None

    __history_index_ref: int = 0

    def __init__(self):
        pass

    def set_default_state(self, first_iteration: MoveHistory):
        self.__current_turn = first_iteration.turn
        self.__current_score = first_iteration.score
        self.__limit_score = first_iteration.final_score
        self.__map = BoardFactory.build_board(first_iteration)

    def update_game_state(self, history: List[MoveHistory]):
        for move in history:
            self.__update_game_state_from_current_step(move)
        return

    def __update_game_state_from_current_step(self, move: MoveHistory):
        self.__current_turn = move.turn
        self.__current_score = move.score
        self.__map.set_dark_room(move.dark)
        self.__map.set_blocked_path(
            BoardFactory.get_blocked_path_id(move.blocked, self.__map.get_list_of_paths()))

        # We first check if some characters have been moved with some ability (used on previous turn)
        if move.suspects is not None:
            for character in move.suspects:
                character_info: str = character.split("-")
                self.__update_character_position(character_info[0], int(character_info[1]))

        if move.played_character is not None and move.movement is not None:
            self.__update_character_position(str(move.played_character).split("-")[0], int(move.movement))

    def __update_character_position(self, color: str, new_position: int):
        list_of_rooms = self.__map.get_list_of_rooms()
        played_character = self.__map.get_target_character(color)
        previous_position = list_of_rooms[played_character.get_current_position()]

        if new_position != previous_position.get_id():
            previous_position.move_out(played_character)
            new_position = list_of_rooms[new_position]
            new_position.move_in(played_character)
            played_character.set_current_position(new_position.get_id())

    def get_current_turn(self) -> int:
        return self.__current_turn

    def increment_turn(self):
        self.__current_turn += 1

    def get_limit_score(self) -> int:
        return self.__limit_score

    def get_current_score(self) -> int:
        return self.__current_score

    def set_current_score(self, new_score: int):
        self.__current_score = new_score

    def get_map(self) -> Board:
        return self.__map
