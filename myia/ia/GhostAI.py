from typing import List

from myia.game_element.Game import Game
from myia.ia.process.PlanedMove import PlanedMove
from myia.interpret.PlayerType import PlayerType
from myia.interpret.subjective.OpponentStrategyInterpolation import OpponentStrategyInterpolation
from myia.io.MoveHistory import MoveHistory
from myia.io.Parser import Parser
from myia.ia.AI import AI


class GhostAI(AI):

    __current_planned_move: PlanedMove = None

    def __init__(self, player_id: int):
        super().__init__(player_id)

    def process(self, game: Game, question: Parser.Question, history: List[MoveHistory]) -> str:
        # Initialize
        response: str = None
        self.move_planer.set_player_id(self.player_id)

        # Objective interpretation
        analyzed_history = self.analyzer.analyse_history(history)

        # Interpolation over opponent strategy
        opponent_strategy = OpponentStrategyInterpolation(analyzed_history, PlayerType(self.player_id))

        if self.__current_planned_move is None:
            self.__current_planned_move = self.move_planer.get_next_move(game, history, analyzed_history,
                                                                         opponent_strategy)

        if self.__current_planned_move is None:
            pass
        # React according to every data previously collected
        elif question.server_asking == Parser.Question.ServerQuestion.TUILES_DISPONIBLES:
            color_options: List[str] = self.__get_color_options(question.option_available)
            index: int = 0
            for color in color_options:
                if color == self.__current_planned_move.selected_character.get_color():
                    response = str(index)
                index += 1
        elif question.server_asking == Parser.Question.ServerQuestion.POSITIONS_DISPONIBLES:
            for rooms_subselection in self.__current_planned_move.selected_positions_ordered_by_preference:
                for room in rooms_subselection:
                    if room.get_id() in question.option_available:
                        response = room.get_id()
                        break
        elif question.server_asking == Parser.Question.ServerQuestion.ACTIVER_POUVOIR:
            response = "1" if self.__current_planned_move.ability_triggered else "0"

        return response

    @staticmethod
    def __get_color_options(option_available: List[str]) -> List[str]:
        color_option: List[str] = []

        for character in option_available:
            color_option.append(character.split("-")[0])
        return color_option
