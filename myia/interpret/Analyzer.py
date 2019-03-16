from typing import List

from myia.interpret.CharacterState import CharacterState
from myia.interpret.objective.HistoryInterpret import HistoryInterpret
from myia.interpret.objective.InterpretedMove import InterpretedMove
from myia.interpret.objective.MoveInterpret import MoveInterpret
from myia.interpret.objective.MoveType import MoveType
from myia.io.MoveHistory import MoveHistory


class Analyzer:

    history_interpret: HistoryInterpret
    move_interpret: MoveInterpret()

    def __init__(self):
        self.history_interpret = HistoryInterpret()
        self.move_interpret = MoveInterpret()

    def analyse_history(self, history: List[MoveHistory]) -> List[InterpretedMove]:
        list_of_interpreted_move: List[InterpretedMove] = []

        for move in history:
            character: str = move.played_character
            if character is not None and move.movement is not None:

                # Get previous state of character
                previous_state: CharacterState = self.history_interpret.get_previous_state_of_character(move)
                # Get new state of character
                new_state: CharacterState = self.history_interpret.get_new_state_of_character(move)
                # Get type of movement
                move_type: MoveType = self.move_interpret.get_nature_of_movement(previous_state, new_state)

                # Get character color and suspect state
                character_info = character.split("-")
                character_color = character_info[0]
                character_suspect_state = character_info[2]

                # Get player
                player: int = int(move.player)

                # Add interpreted move in list
                list_of_interpreted_move.append(
                    InterpretedMove(previous_state, new_state, move_type, character_color, character_suspect_state, player))
        return list_of_interpreted_move

