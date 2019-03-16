from typing import List

from myia.game_element.Character import Character
from myia.game_element.Room import Room


class PlanedMove:

    def __init__(self, selected_character: Character, selected_position_ordered_by_preference: List[List[Room]],
                 ability_triggered: bool):
        self.selected_character: Character = selected_character
        self.selected_positions_ordered_by_preference: List[List[Room]] = selected_position_ordered_by_preference
        self.ability_triggered: bool = ability_triggered
