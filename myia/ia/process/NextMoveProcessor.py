from typing import List, Optional

from myia.game_element.Character import Character
from myia.game_element.Game import Game
from myia.game_element.Room import Room
from myia.ia.minmax.ClearedSuspectsMinMax import ClearedSuspectsMinMax
from myia.ia.minmax.ScoringMinMax import ScoringMinMax
from myia.ia.minmax.MinMax import MinMax
from myia.ia.process.PlanedMove import PlanedMove
from myia.ia.process.selector.CharacterSelector import CharacterSelector
from myia.ia.process.selector.GhostCharacterSelector import GhostCharacterSelector
from myia.ia.process.selector.InspectorCharacterSelector import InspectorCharacterSelector
from myia.interpret.PlayerType import PlayerType
from myia.interpret.objective.InterpretedMove import InterpretedMove
from myia.interpret.subjective.OpponentStrategyInterpolation import OpponentStrategyInterpolation
from myia.io.MoveHistory import MoveHistory


class NextMoveProcessor:

    def __init__(self):
        pass

    @staticmethod
    def predict_next_move(game: Game,
                          history: List[MoveHistory],
                          remaining_characters: List[Character],
                          player: PlayerType) -> Optional[PlanedMove]:

        if len(remaining_characters) <= 0:
            return None

        character_and_possible_move_selection: (Character, List[List[Room]]) = NextMoveProcessor\
            .__build_character_selector(player, game).get_selected_character(remaining_characters)
        return PlanedMove(character_and_possible_move_selection[0], character_and_possible_move_selection[1], False)

    @staticmethod
    def __get_min_max_criteria(player: PlayerType, game: Game) -> MinMax:
        return ClearedSuspectsMinMax(game) if player.INSPECTOR else ScoringMinMax(game)

    @staticmethod
    def __build_character_selector(player: PlayerType, game: Game) -> CharacterSelector:
        return InspectorCharacterSelector(game) if player == PlayerType.INSPECTOR else GhostCharacterSelector(game)
