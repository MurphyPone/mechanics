import random

from player import Player 
from enemy import Enemy


# an encounter is a sub game loop ?
# each loop there should be a chance to add another cog from the queue to the active slots if # < 4
class Encounter():
    # difficulty is a term which scales the average level of the enemies
    def __init__(self, player=Player(), num_enemies=random.randint(1,4), difficulty=0.75):
        self.player = player
        
        if difficulty > 2:
            difficulty = 2

        self.num_enemies = num_enemies
        self.remaining_enemies = []
        for i in range(num_enemies+1):
            lo = 1
            hi = min(12, int(random.randint(1,6) * (difficulty)) + random.randint(0,1))
            lvl = max(lo, hi)
            self.remaining_enemies.append(Enemy(lvl=lvl))

        self.active_enemies = []
        self.fill_active_slots(init=True)
        # select up to 4 enemies to be moved to the active slot
        

    def fill_active_slots(self, init=False):

        open_slots = 4 if init else len(self.active_enemies)
        amt_to_add = 0 if open_slots == 0 else random.randint(1, open_slots)

        for i in range(1, amt_to_add+1):
            if len(self.remaining_enemies) > 0:
                self.active_enemies.append(self.remaining_enemies[0])
                self.remaining_enemies = self.remaining_enemies[1:]

    def enemies_alive(self):
        for e in self.remaining_enemies:
            if e.is_alive():
                return False 
        
        return True

    
    def resolve(self):
        import pdb
        pdb.set_trace()
        print(f"player alive: {self.player.is_alive()} and enemies alive {self.enemies_alive()}")
        while self.player.is_alive() and self.enemies_alive():
            player_cmd = -1
            while int(player_cmd) < 1 or int(player_cmd) > len(self.player.party):
                player_cmd = input(f"select a character to attack 1 - {len(self.player.party)}")


    def __repr__(self):
        res = ""
        res += f"{self.player.__rich__()}\nvs.\n"
        res += "[ACTIVE ENEMIES]\n"
        for e in self.active_enemies:
            res += f"{e}\n"
        res += "[REMAINING ENEMIES]\n"
        for e in self.remaining_enemies:
            res += f"{e}\n"
        return res

e = Encounter()
e.resolve()

