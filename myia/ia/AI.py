from typing import List

from myia.game_element.Game import Game
from myia.ia.minmax.ClearedSuspectsMinMax import ClearedSuspectsMinMax
from myia.ia.process.MovePlaner import MovePlaner
from myia.io.MoveHistory import MoveHistory
from myia.io.Parser import Parser
from myia.interpret.Analyzer import Analyzer


class AI:

    player_id: int
    analyzer: Analyzer
    move_planer: MovePlaner

    def __init__(self, player_id: int):
        self.player_id = player_id
        self.analyzer = Analyzer()
        self.move_planer = MovePlaner()

    def process(self, game: Game, question: Parser.Question, history: List[MoveHistory]) -> str:
        raise NotImplementedError("AI.process isn't implemented, need to be overwrite.")
