from character import Character, get_random_character
from enemy import Enemy

class Player():
    def __init__(self):
        self.party = []
        self.coins = 0

    def add_party_member(self, char):
        if len(self.party) < 4:
            self.party.append(char)

    def __repr__(self, index=None):
        if index and index >= 0 and index < len(self.party):
            return self.party[index]

        res = ""
        for character in self.party:
            res += character.__repr__()
            res += "-" * 46  + "\n"
        return res

    

# p = Player()
# p.add_party_member(get_random_character())
# p.add_party_member(get_random_character())
# p.add_party_member(get_random_character())
# print(p)