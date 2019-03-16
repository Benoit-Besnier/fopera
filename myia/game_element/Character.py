

class Character:

    __color: str = None
    __is_suspect: bool = False
    __current_position: int = None

    def __init__(self, color: str, current_position: int):
        self.__color = color
        self.__is_suspect = True
        self.__current_position = current_position

    def get_color(self) -> str:
        return self.__color

    def is_suspect(self) -> bool:
        return self.__is_suspect

    def get_current_position(self) -> int:
        return self.__current_position

    def set_current_position(self, room_id: int):
        self.__current_position = room_id

    def is_cleared(self):
        self.__is_suspect = False
