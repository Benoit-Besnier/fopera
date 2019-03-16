from myia.game_element.Character import Character
from myia.game_element.Game import Game
from myia.ia.minmax.MinMax import MinMax
from myia.ia.process.NextMoveProcessor import NextMoveProcessor
from myia.ia.process.PlanedMove import PlanedMove
from myia.ia.process.selector.CharacterSelector import CharacterSelector
from myia.ia.process.selector.GhostCharacterSelector import GhostCharacterSelector
from myia.ia.process.selector.InspectorCharacterSelector import InspectorCharacterSelector
from myia.interpret.PlayerType import PlayerType
from myia.interpret.objective.InterpretedMove import InterpretedMove
from myia.interpret.subjective.OpponentStrategyInterpolation import OpponentStrategyInterpolation
from myia.io.MoveHistory import MoveHistory

from typing import Sequence, List, Optional


class MovePlaner:

    __player_type: PlayerType

    def __init__(self):
        pass

    def get_next_move(self, game: Game, history: List[MoveHistory], analyzed_history: List[InterpretedMove],
                      opponent_strategy: OpponentStrategyInterpolation) -> Optional[PlanedMove]:
        turns_count: int = len(history)
        remaining_characters: List[Character] = self.__get_remaining_characters(history[turns_count - 1])
        remaining_player_turn_rotation: List[PlayerType] = self.__get_remaining_turn_player_rotation(
            history, turns_count, len(remaining_characters))

        return NextMoveProcessor.predict_next_move(game, history, remaining_characters, self.__player_type)

    def __get_remaining_turn_player_rotation(self, history: List[MoveHistory], turns_count: int,
                                             remaining_characters_count: int) -> List[PlayerType]:
        turn_rotation: List[PlayerType] = []

        # We get the last two last steps which is enough to calculate all following rotation
        for i in range(turns_count - 2, turns_count):
            turn_rotation.append(PlayerType(history[i].player))
        self.__calculate_turn_rotation(turn_rotation, remaining_characters_count)
        for i in range(0, 2):
            turn_rotation.pop(i)
        return turn_rotation

    # For the next 'n' steps (excluding the two last steps) calculate rotation for four turns with the two last move
    @staticmethod
    def __calculate_turn_rotation(turn_rotation: List[PlayerType], deepness: int) -> List[PlayerType]:
        for i in range(1, deepness + 2):
            if turn_rotation[i - 1] == turn_rotation[i]:
                turn_rotation.append(PlayerType((i + 1) % 2))
            else:
                turn_rotation.append(PlayerType(turn_rotation[i].value))
        return turn_rotation

    @staticmethod
    def __get_remaining_characters(move_history: MoveHistory) -> List[Character]:
        remaining_characters: List[Character] = []
        move_history.characters = [] if move_history.characters is None else move_history.characters

        for character in move_history.characters:
            elem: List[str] = character.split("-")
            remaining_characters.append(Character(elem[0], int(elem[1])))
        return remaining_characters

    def set_player_id(self, player_id: int):
        self.__player_type = PlayerType(player_id)
