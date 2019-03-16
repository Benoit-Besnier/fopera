from myia.game_element.Game import Game


class MinMax:

    def __init__(self, game: Game):
        self.game = game

    def get_current_state(self):
        raise NotImplementedError("MinMax.get_current_state isn't implemented, need to be overwrite.")

    def get_winning_state(self):
        raise NotImplementedError("MinMax.get_winning_state isn't implemented, need to be overwrite.")

    def get_current_ratio(self):
        raise NotImplementedError("MinMax.get_current_ratio isn't implemented, need to be overwrite.")
