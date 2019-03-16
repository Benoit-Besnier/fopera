from enum import Enum
from typing import List

from helper import Tuile
from myia.io.MoveHistory import MoveHistory


class Parser:

    def __init__(self):
        pass

    @staticmethod
    def translate_history(history: list) -> List[MoveHistory]:
        move_history: List[MoveHistory] = []

        for move in history:
            if move.get('tour') is not None:
                move_history.append(MoveHistory(move))
        return move_history

    class Parse:

        @staticmethod
        def parse_available_characters(line: str):
            """ ex: Tuiles disponibles : [rose-3-clean, gris-4-clean] choisir entre 0 et 2 """
            q = line
            new_tuiles = {
                Tuile.Color[x[0]]: Tuile(
                    Tuile.Color[x[0]],
                    Tuile.Status[x[2].strip()],
                    int(x[1].strip())
                ) for x in [x.strip().split('-') for x in q[q.index('[') + 1: q.index(']')].split(',')]
            }
            return new_tuiles

        @staticmethod
        def parse_available_rooms(line: str):
            """ positions disponibles : {1, 3}, choisir la valeur """
            q = line
            return [int(x) for x in q[q.index('{') + 1:q.index('}')].split(',')]

        @staticmethod
        def parse_ability_triggering(line: str):
            """ Voulez-vous activer le pouvoir (0/1) ?  """
            return [0, 1]

        @staticmethod
        def parse_rooms_to_put_in_darkness(line: str):
            """ Quelle salle obscurcir ? (0-9) """
            return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        @staticmethod
        def parse_rooms_to_block(line: str):
            """ Quelle salle bloquer ? (0-9) """
            return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        @staticmethod
        def parse_path_to_selected_room_to_block(line: str):
            """ Quelle sortie ? Chosir parmi : {0, 2} """
            q = line
            return [int(x) for x in q[q.index('{') + 1:q.index('}')].split(',')]

        @staticmethod
        def parse_transposition_with_another_character(line: str, lst: list):
            """ Avec quelle couleur échanger (pas violet!) ?  """
            return [x for x in lst if x.color is not Tuile.Color.violet]

        @staticmethod
        def parse_expulse_other_characters_to_next_rooms(line: str):
            """ rose-6-suspect, positions disponibles : {5, 7}, choisir la valeur """
            q = line
            [int(x) for x in q[q.index('{') + 1:q.index('}')].split(',')]
            return [int(x) for x in q[q.index('{') + 1:q.index('}')].split(',')]

    class Question:

        class ServerQuestion(str, Enum):
            TUILES_DISPONIBLES = 'Tuiles disponibles :',
            POSITIONS_DISPONIBLES = 'positions disponibles :'
            ACTIVER_POUVOIR = 'Voulez-vous activer le pouvoir'
            OBSCURCIR_SALLE = 'Quelle salle obscurcir ? (0-9)'
            BLOQUER_SALLE = 'Quelle salle bloquer ? (0-9)'
            BLOQUER_PATH = 'Quelle sortie ? Chosir parmi :'
            ECHANGER_POSITION = 'Avec quelle couleur échanger (pas violet!) ?'
            REPOUSSER_PERSONNAGE = ', positions disponibles :'

            @staticmethod
            def get_all_server_questions():
                return [Parser.Question.ServerQuestion.TUILES_DISPONIBLES,
                        Parser.Question.ServerQuestion.POSITIONS_DISPONIBLES,
                        Parser.Question.ServerQuestion.ACTIVER_POUVOIR,
                        Parser.Question.ServerQuestion.OBSCURCIR_SALLE,
                        Parser.Question.ServerQuestion.BLOQUER_SALLE,
                        Parser.Question.ServerQuestion.BLOQUER_PATH,
                        Parser.Question.ServerQuestion.ECHANGER_POSITION,
                        Parser.Question.ServerQuestion.REPOUSSER_PERSONNAGE]

        def __init__(self, server_asking: ServerQuestion, result_available):
            self.server_asking = server_asking
            self.option_available = result_available

    # Parse input get from 'questions.txt' file in order to know what server is asking and which options are available
    def parse_question(self, line: str) -> Question:
        server_questions = self.Question.ServerQuestion.get_all_server_questions()
        for server_question in server_questions:
            if server_question.value in line:
                return Parser.Question(server_question, self.__parse_options_from_question(server_question, line))

        return None

    # Depending of the question, we trigger the parse method to get available option given by server
    # Work the same way as a switch/case (most languages) or a array of pointer over functions (in C)
    @staticmethod
    def __parse_options_from_question(question: Question.ServerQuestion, line: str):
        return {
            Parser.Question.ServerQuestion.TUILES_DISPONIBLES: Parser.Parse.parse_available_characters,
            Parser.Question.ServerQuestion.POSITIONS_DISPONIBLES: Parser.Parse.parse_available_rooms,
            Parser.Question.ServerQuestion.ACTIVER_POUVOIR: Parser.Parse.parse_ability_triggering,
            Parser.Question.ServerQuestion.OBSCURCIR_SALLE: Parser.Parse.parse_rooms_to_put_in_darkness,
            Parser.Question.ServerQuestion.BLOQUER_SALLE: Parser.Parse.parse_rooms_to_block,
            Parser.Question.ServerQuestion.BLOQUER_PATH: Parser.Parse.parse_path_to_selected_room_to_block,
            Parser.Question.ServerQuestion.ECHANGER_POSITION: Parser.Parse.parse_transposition_with_another_character,
            Parser.Question.ServerQuestion.REPOUSSER_PERSONNAGE: Parser.Parse.parse_expulse_other_characters_to_next_rooms,
        }[question](line)
