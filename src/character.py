import random

from tracks import TRACKS, TRACKS_META, get_track_color
from tracks import *

from utils import millify
from lore import NAMES

class Character:
    def __init__(self, dic=None):
        if dic is not None: # recreate character from dictionary
            self.name = dic["name"]
            self.max_hp = dic["max_hp"]
            self.current_hp = dic["current_hp"]
            self.tracks = [t for t in dic["tracks"]]
            self.track_xp = {k:v for k,v in dic["track_xp"].items()}
            self.inventory = {k:v for k,v in dic["inventory"].items()}
        else:  # generate a blank, new character
            self.name = random.choice(NAMES)
            self.max_hp = 25
            self.current_hp = self.max_hp
            self.tracks = ["Physicality", "Precision"] # just the keys which refer to the TRACKS lookup table
            self.track_xp = {"Physicality": 0, "Precision": 0} 
            self.inventory = {"Physicality": [5, 0, 0 , 0, 0, 0, 0], "Precision": [5, 0, 0 , 0, 0, 0, 0]} # need to add check to make sure the gag limit not exceeded

    def add_xp(self, track, amount):
        if track in self.tracks:
            self.track_xp[track] += int(amount)

    def get_available_attacks(self, track):
        atks = []
        for i, atk in enumerate(TRACKS[track]):
            if self.track_xp[track] >= TRACKS_META["xp_unlock"][i]:
                atks.append(atk['name'])
        return atks

    # returns the level of the maximum unlocked ability in a track [1, 7]
    def get_track_max_level(self, track):
        i = 0
        while i < 6 and self.track_xp[track] >= TRACKS_META["xp_unlock"][i+1]:
            i += 1
        return i

    def unlock_track(self, track):
        if track in TRACKS.keys() and track not in self.tracks:
            self.tracks.append(track)
            self.track_xp[track] = 0

    def get_atk_acc(self, track, lvl, enemy):
        prop_acc = TRACKS[track][lvl]["prop_acc"]
        track_xp = (self.get_track_max_level(track) - 1) * 10
        tgt_def = enemy.defense
        bonus = 0 

        return prop_acc + track_xp + tgt_def + bonus

    def is_alive(self):
        return self.current_hp > 0

    # should get called by player which checks if user has enough coin
    # todo allow the user to purchase an amount?
    def buy_attack(self, track, level):
        # check to make sure character has track and level unlocked
        if track in self.tracks and level <= self.get_track_max_level(track):
            if self.inventory[track][level] < TRACKS_META["max_holdable"][level]:
                self.inventory[track][level-1] += 1
                print(f"{self.name} purchased a {TRACKS[track][level-1]['name']}")    
                return True 
            else:
                print(f"{self.name} is holding the maximum amount of that item")    

        else:
            print(f"{self.name} doesn't have that attack unlocked")
            return False 

    def __repr__(self):
        res = f"{self.name}\t{self.current_hp}/{self.max_hp} [red]:heart:[/red]\n\n"
        res += "XP\t\tAbility Track\tProgress\n"
        for i, track in enumerate(TRACKS.keys()):
            if track in self.tracks:
                lvl = self.get_track_max_level(track) + 1
                # instead of squares, we could use emojis and blank squares?
                max_width = max([len(key) for key in TRACKS.keys()])
                just_track = f"{track}:".ljust(max_width)
                color = get_track_color(track)
                res += f"({millify(self.track_xp[track])}/{millify(TRACKS_META['xp_unlock'][min(lvl, 6)])})\t[{color}]{just_track}[/{color}]\t" + ("■ " * lvl) + ("□ " * (7 - lvl)) + "\n"

        return res + "\n"

    def show_inventory(self):
        res = f"{self.name}'s Inventory\n"
        for i, track in enumerate(TRACKS.keys()):
            if track in self.tracks:
                max_width = max([len(key) for key in TRACKS.keys()])
                just_track = f"{track}:".ljust(max_width)
                color = get_track_color(track)
                res += f"\t[{color}]{just_track}[/{color}]\t{self.inventory[track]}\n"

        return res


    # used to send to firebase
    def to_dict(self):
        return {
            "name": self.name,
            "max_hp": self.max_hp,
            "current_hp": self.current_hp,
            "tracks": [track for track in self.tracks],
            "track_xp": {k: v for k,v in self.track_xp.items()},
            "inventory": {k:v for k,v in self.inventory.items()}
        }

def get_random_character():
    c = Character()
    for track in TRACKS.keys():
        c.unlock_track(track)
        c.add_xp(track, random.randint(0, 1e4))
    return c 

# c = Character()
# c.buy_attack("Precision", 1)
# print(c.show_inventory())


# e = Enemy(lvl=12)
# print(e)
# acc = c.get_atk_acc("Hex", 6, e)
# print(f"{c.name} attacks {e.name} with accuracy {acc}")
