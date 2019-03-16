from myia.interpret.CharacterState import CharacterState
from myia.interpret.objective.MoveType import MoveType
from myia.interpret.PlayerType import PlayerType


class InterpretedMove:

    __previous_state: CharacterState
    __new_state: CharacterState
    __move_type: MoveType
    __character_color: str
    __character_suspect_state: bool
    __player: PlayerType

    def __init__(self,
                 previous_state: CharacterState,
                 new_state: CharacterState,
                 move_type: MoveType,
                 character_color: str,
                 character_suspect_state: str,
                 player: int):

        self.__previous_state = previous_state
        self.__new_state = new_state
        self.__move_type = move_type
        self.__character_color = character_color
        self.__player = PlayerType(player)
        self.__character_suspect_state = character_suspect_state.__eq__("suspect")

    def get_previous_state(self) -> CharacterState:
        return self.__previous_state

    def get_new_state(self) -> CharacterState:
        return self.__new_state

    def get_move_type(self) -> MoveType:
        return self.__move_type

    def get_character_color(self) -> str:
        return self.__character_color

    def get_character_suspect_state(self) -> bool:
        return self.__character_suspect_state

    def get_player(self) -> PlayerType:
        return self.__player
