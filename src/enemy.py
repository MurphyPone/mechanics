import random 
from player import Player 

tgt_def = [-2, -5, -10, -15, -20, -25, -30, -35, -40, -45, -50, -55]
hp      = [6,  12,  20,  30,  42,  56,  72,  90, 110, 132, 156, 200]

class Enemy():
    def __init__(self, name="cog", lvl=1):
        self.level = lvl if lvl <= 12 else 1
        self.max_hp = hp[self.level-1]
        self.current_hp = self.max_hp
        self.defense = tgt_def[self.level-1]
        self.attack = None
        self.name = name

    def is_alive(self):
        return self.current_hp > 0

    def __repr__(self):
        return f"Level {self.level} {self.name} ({self.current_hp} / {self.max_hp})"
