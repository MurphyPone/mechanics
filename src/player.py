from collections import OrderedDict
from character import Character, get_random_character
from utils import SAVE_FILE
from enemy import Enemy
import json

class Player():
    def __init__(self, dic=None):
        if dic is not None:
            self.party = [Character(dic=v) for v in dic["party"]]
            self.coins = dic["coins"]
        else: 
            self.party = [Character()]
            self.coins = 10
        self.save_location = "save_file.json"

    def add_party_member(self):
        if len(self.party) < 4:
            self.party.append(Character())

    def buy_attack(self, char_idx, track, level):
        # ensure buying items for a valid char
        if char_idx <= len(self.party-1):
            if self.coins > 0:
                return self.party[char_idx].buy_attack(track, level)
            else:
                print("insufficient funds")
        else:
            print("that party member does not exist")

    def show_inventory(self, idx=0):
        if idx >= 0 and idx < len(self.party):
            return self.party[idx].show_inventory()
        else:
            return self.party[0].show_inventory()



    def __rich__(self, index=None):
        if index and index >= 0 and index < len(self.party):
            return self.party[index]

        res = f"Coins: {self.coins}\nParty Member(s)\n"
        for character in self.party:
            res += character.__repr__()
            res += "-" * 46  + "\n"
        return res
    
    def to_dict(self):
        return {
            "party": [c.to_dict() for c in self.party],
            "coins": self.coins
        }

    def save(self):
        with open(self.save_location, 'w') as f:
            json.dump(self.to_dict(), f)

        
    


# p = Player()
# p.add_party_member(get_random_character())
# p.add_party_member(get_random_character())
# p.add_party_member(get_random_character())
# print(p.to_dict())