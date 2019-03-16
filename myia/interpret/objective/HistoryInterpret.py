from myia.interpret.CharacterState import CharacterState
from myia.io.MoveHistory import MoveHistory


class HistoryInterpret:

    def __init__(self):
        pass

    def get_previous_state_of_character(self, move: MoveHistory) -> CharacterState:
        character_info = str(move.played_character).split('-')

        return self.__get_state_of_character(
            move.suspects,
            character_info[0],
            int(character_info[1]),
            int(move.dark))

    def get_new_state_of_character(self, move: MoveHistory) -> CharacterState:
        return self.__get_state_of_character(
            move.suspects,
            str(move.played_character).split('-')[0],
            int(move.movement),
            int(move.dark))

    def __get_state_of_character(self, suspects, color: str, position: int, dark_room: int) -> CharacterState:
        next_to_character: int = 0

        for suspect in suspects:
            suspect_info = suspect.split("-")
            if position == int(suspect_info[1] and color != suspect_info[0]):
                next_to_character += 1

        return self.__convert_to_character_state(next_to_character, position == dark_room)

    @staticmethod
    def __convert_to_character_state(next_to_character: int, is_in_dark_room: bool) -> CharacterState:
        if next_to_character > 0:
            if is_in_dark_room:
                return CharacterState.IN_GROUP_IN_DARKNESS
            return CharacterState.IN_GROUP
        else:
            if is_in_dark_room:
                return CharacterState.ALONE_IN_DARKNESS
            return CharacterState.ALONE
