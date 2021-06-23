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
        self.all_enemies = []
        for i in range(num_enemies+1):
            lo = 1
            hi = min(12, int(random.randint(1,6) * (difficulty)) + random.randint(0,1))
            lvl = max(lo, hi)
            self.all_enemies.append(Enemy(lvl=lvl))

        self.active_enemies = []

    def enemies_alive(self):
        all_dead = True
        for e in self.all_enemies:
            if e.is_alive():
                all_dead = False 
        
        return all_dead

    
    def resolve(self):
        while self.player.is_alive() and self.enemies_alive():
            player_cmd = input("select a character to attack")

    def __repr__(self):
        res = ""
        for e in self.all_enemies:
            res += f"{e}\n"
        return res

print(Encounter())
