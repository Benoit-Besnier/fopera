from myia.game_element.Character import Character
from myia.ia.minmax.MinMax import MinMax


class ScoringMinMax(MinMax):

    def get_current_state(self) -> int:
        return self.game.get_current_score()

    def get_winning_state(self) -> int:
        return len(self.game.get_limit_score())

    def get_current_ratio(self) -> float:
        return self.get_current_ratio() / self.get_winning_state()
