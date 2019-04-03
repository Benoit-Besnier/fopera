from myia.ia.GhostAI import GhostAI

# Default playerId which is associated to the folder where server expect us to listen and answer
player_id = 1

def lancer():
    starter = Starter(player_id)
    ai = GhostAI(player_id)
    starter.run(ai)
