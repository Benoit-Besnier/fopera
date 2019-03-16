from typing import List

from myia.game_element.Game import Game
from myia.io.MoveHistory import MoveHistory
from myia.io.Parser import Parser
from myia.io.TextFileManager import TextFileManager
from myia.ia.AI import AI


class Starter:

    def __init__(self, player_id):
        self.__textFileManager = TextFileManager(player_id)
        self.__parser = Parser()
        self.__game = Game()

    def initialize(self):
        pass

    def run(self, ai: AI):

        previous_line: str = None

        while self.__textFileManager.game_is_ongoing():
            print("running")

            # Get history
            history: List[MoveHistory] = self.__parser\
                .translate_history(self.__textFileManager.get_history_from_info_file())

            if len(history) > 0:

                if self.__game.get_map() is None:
                    self.__game.set_default_state(history[0])
                print("history size :", len(history))

                # Update current game state
                self.__game.update_game_state(history)

                # Get current question
                line = self.__textFileManager.get_question()

                if line == "" and line == previous_line:
                    print("Question is either empty or already treated.")
                else:
                    question = self.__parser.parse_question(line)
                    print("question :", line, "| understood :", question.server_asking, question.option_available)

                    # If current question is invalid
                    if question is None:
                        print("Question couldn't be parsed.")
                    # Else, we let our IA process data and give us a response
                    else:
                        # IA process data to give us a response
                        response = ai.process(self.__game, question, history)
                        # We write the response in the 'reponses.txt'
                        self.__textFileManager.write_response(response)
                        # We make define current question as treated (to be omitted if nothing happen until next loop)
                        previous_line = line
                        print("Question processed. Given response : ", response)
