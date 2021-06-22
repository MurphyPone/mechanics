import random

from tracks import TRACKS, TRACKS_META
from tracks import *
from enemy import Enemy
from utils import millify, NAMES

class Character:
    def __init__(self):
        self.name = random.choice(NAMES)
        self.max_hp = 25
        self.current_hp = self.max_hp
        self.tracks = ["Physicality", "Precision"] # just the keys which refer to the TRACKS lookup table
        self.track_xp = {"Physicality": 0, "Precision": 0} # I think this can be a dict?


    # TODO refactor for uniform ordering of tracks
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
        while i < 7 and self.track_xp[track] >= TRACKS_META["xp_unlock"][i]:
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

    def __repr__(self):
        res = f"{self.name}\t{self.current_hp}/{self.max_hp}\n\n"
        res += "XP\t\tTrack\t\tunlocks\n"
        for track in TRACKS.keys():
            if track in self.tracks:
                lvl = self.get_track_max_level(track)
                # instead of squares, we could use emojis and blank squares?
                max_width = max([len(key) for key in TRACKS.keys()])
                just_track = f"{track}:".ljust(max_width)
                res += f"({millify(self.track_xp[track])}/{millify(TRACKS_META['xp_unlock'][min(lvl+1, 6)])})\t{just_track}\t" + ("■ " * lvl) + ("□ " * (7 - lvl)) + "\n"

        return res + "\n"


def get_random_character():
    c = Character()
    for track in TRACKS.keys():
        c.unlock_track(track)
        c.add_xp(track, random.randint(0, 1e4))
    return c 
## how to represent a track

# e = Enemy(lvl=12)
# print(e)
# acc = c.get_atk_acc("Hex", 6, e)
# print(f"{c.name} attacks {e.name} with accuracy {acc}")
