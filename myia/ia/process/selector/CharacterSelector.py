from typing import List

from myia.game_element.Character import Character
from myia.game_element.Game import Game
from myia.game_element.Path import Path
from myia.game_element.Room import Room


class CharacterSelector:

    def __init__(self, game: Game):
        self.game = game

    def get_selected_character(self, remaining_character: List[Character]) -> (Character, List[List[Room]]):
        raise NotImplementedError("CharacterSelector.get_selected_character isn't implemented, need to be overwrite.")

    @staticmethod
    def get_remaining_characters_in_dark_room(remaining_characters: List[Character], game: Game) -> List[Character]:
        dark_room: Room = game.get_map().get_dark_room()
        remaining_characters_color: List[str] = CharacterSelector.get_characters_color(remaining_characters)
        remaining_characters_in_dark_room: List[Character] = []

        for inhabitant in dark_room.get_inhabitant():
            if inhabitant.get_color() in remaining_characters_color:
                remaining_characters_in_dark_room.append(inhabitant)
        return remaining_characters_in_dark_room

    @staticmethod
    def get_remaining_characters_out_dark_room(remaining_characters: List[Character], game: Game) -> List[Character]:
        dark_room: Room = game.get_map().get_dark_room()
        remaining_characters_color: List[str] = CharacterSelector.get_characters_color(remaining_characters)
        remaining_characters_out_dark_room: List[Character] = []

        for inhabitant in dark_room.get_inhabitant():
            if inhabitant.get_color() in remaining_characters_color:
                pass
            else:
                remaining_characters_out_dark_room.append(inhabitant)
        return remaining_characters_out_dark_room

    @staticmethod
    def get_remaining_characters_alone(remaining_characters: List[Character], game: Game) -> List[Character]:
        characters_alone: List[Character] = CharacterSelector.get_characters_alone(game.get_map().get_list_of_rooms())
        remaining_characters_color: List[str] = CharacterSelector.get_characters_color(remaining_characters)
        remaining_characters_alone: List[Character] = []

        for character_alone in characters_alone:
            if character_alone.get_color() in remaining_characters_color:
                remaining_characters.append(character_alone)
        return remaining_characters_alone

    @staticmethod
    def get_remaining_characters_in_group(remaining_characters: List[Character], game: Game) -> List[Character]:
        characters_in_group: List[Character] = CharacterSelector.\
            get_characters_in_group(game.get_map().get_list_of_rooms())
        remaining_characters_color: List[str] = CharacterSelector.get_characters_color(remaining_characters)
        remaining_characters_alone: List[Character] = []

        for character_in_group in characters_in_group:
            if character_in_group.get_color() in remaining_characters_color:
                remaining_characters.append(character_in_group)
        return remaining_characters_alone

    @staticmethod
    def get_character_available_paths(character: Character, game: Game) -> List[Path]:
        inhabiting_room: Room = game.get_map().get_list_of_rooms()[character.get_current_position()]
        paths: List[Path] = game.get_map().get_list_of_paths()
        available_paths: List[Path] = []

        for path in paths:
            if path.get_id() != game.get_map().get_blocked_path() and path.match_room_id(inhabiting_room.get_id()):
                if not path.is_rose_special() and not path.is_secret_stairs():
                    available_paths.append(path)
        return available_paths

    @staticmethod
    def get_characters_alone(rooms: List[Room]) -> List[Character]:
        characters_alone: List[Character] = []

        for room in rooms:
            room_inhabitant: List[Character] = room.get_inhabitant()
            if len(room_inhabitant) == 1:
                characters_alone.append(room_inhabitant[0])
        return characters_alone

    @staticmethod
    def get_characters_in_group(rooms: List[Room]) -> List[Character]:
        characters_alone: List[Character] = []

        for room in rooms:
            room_inhabitant: List[Character] = room.get_inhabitant()
            if len(room_inhabitant) > 1:
                for inhabitant in room_inhabitant:
                    characters_alone.append(inhabitant)
        return characters_alone

    @staticmethod
    def get_characters_color(characters: List[Character]) -> List[str]:
        characters_color: List[str] = []

        for characters in characters:
            characters_color.append(characters.get_color())
        return characters_color
