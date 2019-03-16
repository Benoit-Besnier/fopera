from typing import List

from myia.game_element.Character import Character


class Room:

    __id: int = 0
    __inhabited_by: List[Character] = []

    def __init__(self, room_id: int):
        self.__id = room_id
        self.__inhabited_by = []

    def get_id(self):
        return self.__id

    def move_in(self, character: Character) -> bool:
        if character in self.__inhabited_by:
            return False
        self.__inhabited_by.append(character)
        return True

    def move_out(self, character: Character) -> bool:
        if character in self.__inhabited_by:
            return False
        self.__inhabited_by.remove(character)
        return True

    def get_inhabitant(self) -> List[Character]:
        return self.__inhabited_by
