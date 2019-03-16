from typing import List

from myia.game_element.Board import Board
from myia.game_element.Character import Character
from myia.game_element.Room import Room
from myia.game_element.Path import Path

# map happen to be something like this :
#
#   ________
#  /        \
# | 8--------9
# | |x      x|
#  \| x    x |
#   4--5--6--7
#   |  x  x  |\
#   0--1--2--3 |
#       \______/
#
from myia.io.MoveHistory import MoveHistory
from myia.io.TextFileManager import GameStartingState

LIST_OF_SIMPLE_PATH = [
    [0, 1], [0, 4],
    [1, 2], [2, 3],
    [3, 7],
    [4, 5], [4, 8],
    [5, 6],
    [6, 7],
    [7, 9],
    [8, 9]
]

# TODO : It may not be exact, need to check afterward...
LIST_OF_SECRET_STAIRS = [
    [1, 5],
    [2, 6],
    [5, 8],
    [6, 9]
]

LIST_OF_ROSE_SPECIAL_PATH = [
    [1, 7],
    [4, 9]
]

LIST_OF_CHARACTERS = ['marron', 'rose', 'violet', 'blanc', 'rouge', 'noir', 'gris', 'bleu']


class BoardFactory:

    @staticmethod
    def build_board(first_iteration: MoveHistory) -> Board:
        list_of_rooms: List[Room] = BoardFactory.__build_rooms()
        list_of_paths: List[Path] = BoardFactory.__build_paths(list_of_rooms)
        characters_states: List[List[str]] = []

        for character in first_iteration.suspects:
            characters_states.append(character.split("-"))

        list_of_characters: List[Character] = BoardFactory\
            .__build_characters(characters_states, list_of_rooms)
        blocked_path_id = BoardFactory.get_blocked_path_id(first_iteration.blocked, list_of_paths)

        return Board(first_iteration.dark, blocked_path_id, list_of_rooms, list_of_paths, list_of_characters)

    @staticmethod
    def get_blocked_path_id(blocked_path: List[int], list_of_path: List[Path]):
        for path in list_of_path:
            if path.match_rooms_id(blocked_path[0], blocked_path[1]):
                return path.get_id()

    @staticmethod
    def __build_rooms():
        rooms = []

        for index in range(0, 10):
            rooms.append(Room(index))
        return rooms

    @staticmethod
    def __build_paths(list_of_rooms: List[Room]) -> List[Path]:
        paths_to_construct = [LIST_OF_SIMPLE_PATH, LIST_OF_SECRET_STAIRS, LIST_OF_ROSE_SPECIAL_PATH]
        path_id = 0
        sublist_count = 0
        list_of_paths: List[Path] = []

        for sublist_of_path_to_construct in paths_to_construct:
            for path in sublist_of_path_to_construct:
                list_of_paths.append(Path(
                    path_id,
                    list_of_rooms[path[0]],
                    list_of_rooms[path[1]],
                    sublist_count == 1,
                    sublist_count == 2
                ))
                path_id += 1
            sublist_count += 1
        return list_of_paths

    @staticmethod
    def __build_characters(characters_states: List[List[str]], list_of_rooms: List[Room]) -> List[Character]:
        list_of_characters: List[Character] = []

        for character in characters_states:
            if character[0] in LIST_OF_CHARACTERS:
                room = list_of_rooms[int(character[1])]
                character = Character(character[0], room.get_id())
                room.move_in(character)
                list_of_characters.append(character)

        return list_of_characters
