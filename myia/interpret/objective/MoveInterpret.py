from myia.interpret.CharacterState import CharacterState
from myia.interpret.objective.MoveType import MoveType


class MoveInterpret:

    def __init__(self):
        pass

    @staticmethod
    def get_nature_of_movement(prev_state: CharacterState, new_state: CharacterState) -> MoveType:
        move_type: MoveType = None

        if (prev_state == CharacterState.ALONE or prev_state == CharacterState.IN_GROUP) and prev_state == new_state:
            move_type = MoveType.EQUIVALENT_MOVE
        elif prev_state.value > 2 and new_state.value <= 2:
            move_type = MoveType.DISPERSE_MOVE
        elif prev_state.value <= 2 and new_state.value > 2:
            move_type = MoveType.RALLY_MOVE
        else:
            move_type = MoveType.EQUIVALENT_MOVE

        return move_type
