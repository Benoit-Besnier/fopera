class MoveHistory:
    turn = None
    score = None
    dark = None
    blocked = None
    suspects = None
    cry = None
    ability_type = None
    player = None
    characters = None
    played_character = None
    movement = None
    is_ability_used = None
    final_score = None

    def __init__(self, move: dict):
        self.turn = move.get('tour')
        self.score = move.get('score')
        self.dark = move.get('ombre')
        self.blocked = move.get('bloqué')
        self.suspects = move.get('suspects')
        self.cry = move.get('cri')
        self.ability_type = move.get('pouvoir action')
        self.player = move.get('joueur')
        self.characters = move.get('tuiles')
        self.played_character = move.get('perso joué')
        self.movement = move.get('déplacement')
        self.is_ability_used = move.get('pouvoir utilisé')
        self.final_score = move.get('score fin')
