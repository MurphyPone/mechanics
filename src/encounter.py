import random
from rich.console import Console

from player import Player 
from enemy import Enemy
from tracks import TRACKS, TRACKS_META, get_track_color
from utils import TARGET2STRING


# an encounter is a sub game loop ?
# each loop there should be a chance to add another cog from the queue to the active slots if # < 4
class Encounter():
    # difficulty is a term which scales the average level of the enemies
    def __init__(self, player=Player(), num_enemies=random.randint(1,4), difficulty=0.75, console=Console(highlight=False)):
        self.player = player
        self.console = console
        
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
        self.xp_earned = [{track: 0 for track in c.tracks} for c in self.player.party]
        # select up to 4 enemies to be moved to the active slot
        

    def fill_active_slots(self, init=False):

        open_slots = 4 if init else len(self.active_enemies)
        amt_to_add = 0 if open_slots == 0 else random.randint(1, open_slots)

        for i in range(1, amt_to_add+1):
            if len(self.remaining_enemies) > 0:
                self.active_enemies.append(self.remaining_enemies[0])
                self.remaining_enemies = self.remaining_enemies[1:]

    def enemies_alive(self):
        if len(self.remaining_enemies) > 0:
            return True 
        
        for e in self.active_enemies:
            if e.is_alive():
                return True 
        
        return False

    
    def resolve(self):
        # print(f"player alive: {self.player.is_alive()} and enemies alive {self.enemies_alive()}")
        while self.player.is_alive() and self.enemies_alive():
            player_cmd = -1
            while player_cmd == "" or int(player_cmd)-1 < 0 or int(player_cmd) > len(self.player.party):
                # TODO improve this prompt 
                player_cmd = self.console.input(f'''[yellow]Your party members are[/yellow]\n\t{[f"{i+1, char.name}" for i, char in enumerate(self.player.party) ]}\nselect a character from your party: ''').strip()
                
                # invalid 
                if player_cmd.strip() == "" or not player_cmd.isnumeric():
                    self.console.print("[yellow]Invalid character selection, try again. [/yellow]", end='')
                    continue 
                else:
                    # Do combat in here 
                    player_cmd = int(player_cmd) - 1
                    self.console.log(f"player_cmd: {player_cmd}")
                    char = self.player.party[player_cmd]
                    self.console.print(char.__repr__())
                    
                    # get an attak for that character
                    track_cmd = ""
                    while track_cmd == "":
                        track_cmd = self.console.input(f"[yellow]Select an attack Ability Track for[/yellow] {char.name}: ").strip()
                        for track in TRACKS.keys():
                            if track_cmd.lower() == track.lower():
                                track_cmd = track
                                max_lvl = char.get_track_max_level(track_cmd)

                                self.console.log(f"track_cmd: {track_cmd}, max_level: {max_lvl}")
                                
                                # Garbage 
                                color = get_track_color(track_cmd)
                                self.console.print(f"\t[bold {color}]{track_cmd}[/bold {color}]\t{TRACKS_META['descriptions'][track_cmd]}\n")
                                
                                max_width = max([len(atk['name']) for atk in TRACKS[track]])
                                self.console.print(f"\t  [bold]{'attack'.ljust(max_width)}\t{'target'.ljust(len('a single enemy'))}\toutput range[/bold]")
                                for i, atk in enumerate(TRACKS[track]):
                                    if i < max_lvl:
                                        just_name = f"{atk['name']}".ljust(max_width)
                                        self.console.print(f"\t{i+1} [bold]{just_name}[/bold]\t{TARGET2STRING[atk['target']]}\t{atk['range']}")

                                lvl_cmd = self.console.input(f"[yellow]Select which level you'd like use: [/yellow]")
                                # TODO number norm on this
                                # lvl_cmd = self.console.input(f"[yellow]Select an attack Ability Track for[/yellow] {self.player.party[player_cmd].name}: ").strip()

                        pass 




    def __repr__(self):
        res = ""
        res += f"{[c.name for c in self.player.party]}\nvs.\n"
        res += "[ACTIVE ENEMIES]\n"
        for e in self.active_enemies:
            res += f"{e}\n"
        res += "[REMAINING ENEMIES]\n"
        for e in self.remaining_enemies:
            res += f"{e}\n"

        res += "\nxp earned\n"
        for i, c in enumerate(self.xp_earned):
            # TODO, this chould be their name
            res += f"{i+1} - {self.player.party[i].name}:\n"
            for track, ls in c.items():
                res += f"\t{track}: {ls}\n"
        return res

e = Encounter()
print(e)
e.resolve()

