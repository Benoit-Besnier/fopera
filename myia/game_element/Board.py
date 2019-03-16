from typing import List, Optional

from myia.game_element.Character import Character
from myia.game_element.Path import Path
from myia.game_element.Room import Room


class Board:

    __dark_room: int = 0
    __blocked_path: int = 0
    __list_of_rooms: List[Room] = []
    __list_of_paths: List[Path] = []
    __list_of_characters: List[Character] = []

    def __init__(self, dark_room: int, blocked_path: int, list_of_rooms: List[Room],
                 list_of_paths: List[Path], list_of_characters: List[Character]):
        self.__dark_room = dark_room
        self.__blocked_path = blocked_path
        self.__list_of_rooms = list_of_rooms
        self.__list_of_paths = list_of_paths
        self.__list_of_characters = list_of_characters

    def set_dark_room(self, room_id: int):
        self.__dark_room = room_id

    def get_dark_room(self) -> Room:
        return self.__list_of_rooms[self.__dark_room]

    def set_blocked_path(self, path_id: int):
        self.__blocked_path = path_id

    def get_blocked_path(self) -> Path:
        return self.__list_of_paths[self.__blocked_path]

    def get_list_of_rooms(self) -> List[Room]:
        return self.__list_of_rooms

    def get_list_of_paths(self) -> List[Path]:
        return self.__list_of_paths

    def get_list_of_characters(self) -> List[Character]:
        return self.__list_of_characters

    def get_target_character(self, color: str) -> Optional[Character]:
        for character in self.__list_of_characters:
            if character.get_color() == color:
                return character
        return None
