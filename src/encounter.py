import random
from rich.console import Console
from rich.table import Table

from player import Player 
from enemy import Enemy
from tracks import TRACKS, TRACKS_META, get_track_color
from utils import TARGET2STRING


ENCOUTERS_META = {
    "descriptions": {
        "Street":   "Fight a single wave of 2-8 enemies",
        "Tower":    "Battle through 1-5 floors of increasingly difficult enemies",
        "Factory":  "Test your strength a sprawling dungeon of enemies"
    }
}


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
        """attempts to fill any active slots from remaining_enemies"""

        open_slots = 4 if init else len(self.active_enemies)
        amt_to_add = 0 if open_slots == 0 else random.randint(1, open_slots)

        for i in range(1, amt_to_add+1):
            if len(self.remaining_enemies) > 0:
                self.active_enemies.append(self.remaining_enemies[0])
                self.remaining_enemies = self.remaining_enemies[1:]

    def enemies_alive(self):
        """determines whether or not any enemies are alive"""
        if len(self.remaining_enemies) > 0:
            return True 
        
        for e in self.active_enemies:
            if e.is_alive():
                return True 
        
        return False

    
    def resolve(self):
        # print(f"player alive: {self.player.is_alive()} and enemies alive {self.enemies_alive()}")

        # while one side of the party is alive
        while self.player.is_alive() and self.enemies_alive():
            self.console.print(self.combat_table())
            player_cmd = -1

            # prompt the player to select a character from party by index
            while player_cmd == "" or int(player_cmd)-1 < 0 or int(player_cmd) - 1 > len(self.player.party)-1:

                player_cmd = self.console.input(f'''[yellow]Select a character from your party {[i+1 for i in range(len(self.player.party))]}[/yellow]: ''').strip()
                
                # handle invalid input
                if player_cmd.strip() == "":
                    continue
                elif not player_cmd.isnumeric():
                    self.console.print("[yellow]Invalid character selection, try again. [/yellow]", end='')
                    continue 
                elif int(player_cmd)-1 < 0 or int(player_cmd) - 1 > len(self.player.party)-1:
                    self.console.print(f"[yellow]Invalid character selection ({int(player_cmd)} not ∈ {[i+1 for i in range(len(self.player.party))]}), try again. [/yellow]", end='')
                    continue
                else:
                    # Do combat in here 
                    player_cmd = int(player_cmd) - 1
                    self.console.log(f"player_cmd: {player_cmd}")
                    char = self.player.party[player_cmd]
                    self.console.print(char.__repr__())
                    
                    # get an attack for that character
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
                                self.console.print(f"\t  [bold]{'attack'.ljust(max_width)}\t{'target'.ljust(len('a single enemy'))}\toutput range\tinventory[/bold]")
                                for i, atk in enumerate(TRACKS[track]):
                                    if i < max_lvl:
                                        just_name = f"{atk['name']}".ljust(max_width)
                                        inv = f"{char.inventory[track][i]}/{TRACKS_META['max_holdable'][i]}"
                                        just_range = str(atk['range']).ljust(len('output range'))
                                        self.console.print(f"\t{i+1} [bold]{just_name}[/bold]\t{TARGET2STRING[atk['target']]}\t{just_range}\t{inv}")

                                lvl_cmd = self.console.input(f"[yellow]Select which level you'd like use: [/yellow]")
                                while lvl_cmd == "" or char.inventory[track][int(lvl_cmd)-1] < 0:
                                    if not lvl_cmd.isnumeric():
                                        lvl_cmd = self.console.input(f"[yellow]Invalid casting level, pick [{1}, {max_lvl}][/yellow]")
                                    else:
                                        lvl_cmd = self.console.input(f"[yellow]{char.name} does not have any {TRACKS[track][int(lvl_cmd)-1]}[/yellow]")
                                
                                self.console.log(lvl_cmd)

                                # TODO number norm on this
                                # lvl_cmd = self.console.input(f"[yellow]Select an attack Ability Track for[/yellow] {self.player.party[player_cmd].name}: ").strip()

                        pass 
    
    def combat_table(self, encounter_name="Encounter Name"):
        table = Table(title=encounter_name)
        
        table.add_column("Your Party", justify="left", style="green")
        table.add_column("Active Enemies", justify="right", style="bright_red")
        table.add_column("Remaining Enemies", justify="right", style="bright_red")

        len_party = len(self.player.party)
        len_active = len(self.active_enemies)
        len_remaining = len(self.remaining_enemies)

        for i in range(max([len_party, len_active, len_remaining])):
            char = f"{i+1} - {self.player.party[i].name} ({self.player.party[i].current_hp}/{self.player.party[i].max_hp})" if i < len_party else ""
            active = self.active_enemies[i].__repr__() if i < len_active else ""
            remaining = self.remaining_enemies[i].__repr__() if i < len_remaining else ""

            table.add_row(char, active, remaining)
        
        return table 






    def __repr__(self):
        
        self.console.print(self.combat_table())
        
        for i, xp_dict in enumerate(self.xp_earned):
            table = Table(title=f"{i} - {self.player.party[i].name}'s XP Earned")
            table.add_column("Track", justify="left")
            table.add_column("XP", justify="right")

            for track, amt in xp_dict.items():
                color = get_track_color(track)

                table.add_row(f"[{color}]{str(track)}[/{color}]", str(amt))

            self.console.print(table)

        
        

        # res += "\nxp earned\n"
        # for i, c in enumerate(self.xp_earned):
        #     # TODO, this chould be their name
        #     res += f"{i+1} - {self.player.party[i].name}:\n"
        #     for track, ls in c.items():
        #         res += f"\t{track}: {ls}\n"

        return ""

# e = Encounter()
# # print(e)
# e.resolve()

