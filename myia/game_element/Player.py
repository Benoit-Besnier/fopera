from myia.game_element import Character


class Player:

    __is_inspector = False
    __phantom_character = None

    def __init__(self, is_inspector: bool, phantom_character: Character):
        self.__is_inspector = is_inspector
        if self.is_inspector() is False:
            self.__phantom_character = phantom_character

    def is_inspector(self):
        return self.__is_inspector

    def get_phantom_character(self):
        return self.__phantom_character
