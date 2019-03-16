from myia.Starter import Starter

# Default playerId which is associated to the folder where server expect us to listen and answer
from myia.ia.InspectorAI import InspectorAI

player_id = 0


def lancer():
    starter = Starter(player_id)
    ai = InspectorAI(player_id)
    starter.run(ai)
