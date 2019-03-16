from myia.interpret.CharacterState import CharacterState
from myia.interpret.PlayerType import PlayerType
from myia.interpret.objective import InterpretedMove
from myia.interpret.objective.MoveType import MoveType


class OpponentStrategyInterpolation:
    __opponent_move_type: {MoveType, int} = {}
    __characters_moved_in_dark_room: int = 0
    __characters_moved_out_dark_room: int = 0

    def __init__(self, analyzed_moves: [InterpretedMove], current_player: PlayerType):
        self.__opponent_moves = self.__get_opponent_moves(analyzed_moves, current_player)
        self.__opponent_move_type = self.__get_count_opponent_move_type(self.__opponent_moves)
        self.__characters_moved_in_dark_room = self.__get_count_of_characters_moved_in_dark_room(self.__opponent_moves)
        self.__characters_moved_out_dark_room = self.__get_count_of_characters_moved_out_dark_room(self.__opponent_moves)

    def __get_opponent_moves(self, analyzed_moves: [InterpretedMove], current_player: PlayerType) -> [InterpretedMove]:
        opponent_moves: list[InterpretedMove] = []

        for analyzed_move in analyzed_moves:
            if analyzed_move.get_player() != current_player:
                opponent_moves.append(analyzed_move)
        return opponent_moves

    def __get_count_opponent_move_type(self, opponent_moves: [InterpretedMove]) -> {MoveType, int}:
        opponent_move_type: {MoveType, int} = {MoveType.EQUIVALENT_MOVE: 0,
                                               MoveType.RALLY_MOVE: 0,
                                               MoveType.DISPERSE_MOVE: 0}

        for opponent_move in opponent_moves:
            opponent_move_type[opponent_move.get_move_type()] += 1
        return opponent_move_type

    def __get_count_of_characters_moved_in_dark_room(self, opponent_moves: [InterpretedMove]) -> int:
        count_characters_moved_in_dark_room: int = 0

        for opponent_move in opponent_moves:
            if opponent_move.get_new_state() in [CharacterState.ALONE_IN_DARKNESS, CharacterState.IN_GROUP_IN_DARKNESS]:
                count_characters_moved_in_dark_room += 1
        return count_characters_moved_in_dark_room

    def __get_count_of_characters_moved_out_dark_room(self, opponent_moves: [InterpretedMove]) -> int:
        count_characters_moved_out_dark_room: int = 0

        for opponent_move in opponent_moves:
            if opponent_move.get_previous_state() in [CharacterState.ALONE_IN_DARKNESS, CharacterState.IN_GROUP_IN_DARKNESS]:
                count_characters_moved_out_dark_room += 1
        return count_characters_moved_out_dark_room
