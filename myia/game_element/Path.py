from typing import List

from myia.game_element.Room import Room


class Path:
    __id: int = 0
    __is_secret_stairs: bool = False
    __is_rose_special: bool = False
    __related_rooms_alpha: Room
    __related_rooms_beta: Room

    def __init__(self, path_id: int, related_room_alpha: Room, related_room_beta: Room,
                 is_secret_stairs: bool, is_rose_special: bool):
        self.__id = path_id
        self.__is_secret_stairs = is_secret_stairs
        self.__is_rose_special = is_rose_special
        self.__related_rooms_alpha = related_room_alpha
        self.__related_rooms_beta = related_room_beta

    def get_id(self) -> int:
        return self.__id

    def get_related_rooms_id(self) -> List[int]:
        return [self.__related_rooms_alpha.get_id(), self.__related_rooms_beta.get_id()]

    def is_secret_stairs(self) -> bool:
        return self.__is_secret_stairs

    def is_rose_special(self) -> bool:
        return self.__is_rose_special

    def get_adjacent_room(self, origin: Room) -> Room:
        return self.__related_rooms_beta \
            if self.__related_rooms_alpha.get_id() == origin.get_id() \
            else self.__related_rooms_alpha

    def match_rooms_id(self, id_first: int, id_second: int) -> bool:
        return self.match_room_id(id_first) and self.match_room_id(id_second)

    def match_room_id(self, room_id: int) -> bool:
        return room_id == self.__related_rooms_alpha.get_id() or room_id == self.__related_rooms_beta.get_id()
