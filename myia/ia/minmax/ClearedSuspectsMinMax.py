from myia.game_element.Character import Character
from myia.ia.minmax.MinMax import MinMax


class ClearedSuspectsMinMax(MinMax):

    def get_current_state(self) -> int:
        return self.__get_number_of_cleared_character()

    def get_winning_state(self) -> int:
        return len(self.game.get_map().get_list_of_characters())

    def get_current_ratio(self) -> float:
        return self.get_current_ratio() / self.get_winning_state()

    def __get_number_of_cleared_character(self) -> int:
        count_cleared_character: int = 0
        list_of_characters: list[Character] = self.game.get_map().get_list_of_characters()

        for character in list_of_characters:
            if character.is_cleared():
                count_cleared_character += 1

        return count_cleared_character
