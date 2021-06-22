from collections import OrderedDict
from character import Character, get_random_character
from enemy import Enemy

class Player():
    def __init__(self, dic=None):
        if dic is not None:
            self.party = [Character(dic=v) for v in dic["party"]]
            self.coins = dic["coins"]
        else: 
            self.party = []
            self.coins = 10

    def add_party_member(self, char):
        if len(self.party) < 4:
            self.party.append(char)

    def buy_attack(self, char_idx, track, level):
        # ensure buying items for a valid char
        if char_idx <= len(self.party-1):
            if self.coins > 0:
                return self.party[char_idx].buy_attack(track, level)
            else:
                print("insufficient funds")
        else:
            print("that party member does not exist")



    def __repr__(self, index=None):
        if index and index >= 0 and index < len(self.party):
            return self.party[index]

        res = "Coins: {self.coins}\n"
        for character in self.party:
            res += character.__repr__()
            res += "-" * 46  + "\n"
        return res
    
    def to_dict(self):
        return {
            "party": [c.to_dict() for c in self.party],
            "coins": self.coins
        }
    


# p = Player()
# p.add_party_member(get_random_character())
# p.add_party_member(get_random_character())
# p.add_party_member(get_random_character())
# print(p.to_dict())