from typing import List, Optional

from myia.game_element.Character import Character
from myia.game_element.Game import Game
from myia.game_element.Path import Path
from myia.game_element.Room import Room
from myia.ia.process.selector.CharacterSelector import CharacterSelector


class InspectorCharacterSelector(CharacterSelector):

    def __int__(self, game: Game):
        super().__init__(game)

    def get_selected_character(self, remaining_characters: List[Character]) -> (Character, List[List[Room]]):
        remaining_characters_in_dark_room: List[Character] = super()\
            .get_remaining_characters_in_dark_room(remaining_characters, self.game)
        remaining_characters_alone: List[Character] = super()\
            .get_remaining_characters_alone(remaining_characters, self.game)

        if len(remaining_characters_in_dark_room) > 0:
            return self.__find_most_efficient_move(remaining_characters_in_dark_room)
        elif len(remaining_characters_alone) > 0:
            return self.__find_most_efficient_move(remaining_characters_alone)
        return self.__find_most_efficient_move(remaining_characters)

    def __find_most_efficient_move(self, remaining_characters: List[Character]) -> (Character, List[List[Room]]):
        aggregator: List[(Character, List[List[Room]], int)] = []
        higher_score: int = 0
        most_efficient_move: (Character, List[Room]) = ()

        for remaining_character in remaining_characters:
            available_paths: List[Path] = super().get_character_available_paths(remaining_character, self.game)
            paths_ordered_by_preference: List[List[Room]] = self\
                .__get_adjacent_rooms_ordered_by_preference(remaining_character, available_paths, self.game)
            aggregator.append((
                remaining_character,
                paths_ordered_by_preference,
                len(available_paths) + len(paths_ordered_by_preference[0])))

        for elem in aggregator:
            if elem[2] > higher_score:
                higher_score = elem[2]
                most_efficient_move = (elem[0], elem[1])

        return most_efficient_move

    @staticmethod
    def __get_adjacent_rooms_ordered_by_preference(character: Character, available_paths: List[Path],
                                                   game: Game) -> List[List[Room]]:
        inhabiting_room: Room = game.get_map().get_list_of_rooms()[character.get_current_position()]
        efficient_move: List[Room] = []
        neutral_move: List[Room] = []
        inefficient_move: List[Room] = []

        for available_path in available_paths:
            adjacent_room: Room = available_path.get_adjacent_room(inhabiting_room)
            inhabitant_adjacent_room: List[Character] = adjacent_room.get_inhabitant()

            if adjacent_room.get_id() == game.get_map().get_dark_room().get_id():
                inefficient_move.append(adjacent_room)
            elif len(inhabitant_adjacent_room) == 1:
                efficient_move.append(adjacent_room)
            elif len(inhabitant_adjacent_room) > 1:
                neutral_move.append(adjacent_room)
            else:
                inefficient_move.append(adjacent_room)

        return [efficient_move, neutral_move, inefficient_move]



