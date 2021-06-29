
import sys 
import os
import cmd 
from rich.console import Console

from player import Player
from tracks import TRACKS, TRACKS_META, get_track_color
from utils import TARGET2STRING
from encounter import Encounter, ENCOUTERS_META

COMMANDS = {
    "help": "Displays a list of commands",
    "tutorial": "Leads the player through the tutorial",
    "tracks" :"Displays Information about character ability tracks",
    "party": "Display an overview of your party",
    "inventory": "Displays a character's inventory",
    "fight": "Begin a combat encounter"
}

COMBAT_ALLOWABLE = ["h", "help", "p", "party", "i", "inv", "inventory", "t", "tracks", "quit", "exit"]

class Parser(cmd.Cmd):
    def __init__(self, player, console=Console(highlight=False) ):
        super(Parser, self).__init__()
        self.console = console
        self.player = player
        self.prompt = " "

    # cmd.Cmd overrides
    def cmdloop(self):
        self.console.print(":gear:[yellow] Enter a command:[/yellow]", end="")
        return cmd.Cmd.cmdloop(self)
    
    def postcmd(self, stop: bool, line: str) -> bool:
        self.console.print(":gear:[yellow] Enter a command:[/yellow]", end="")
        return super().postcmd(stop, line)
    
    def parseline(self, line):
        line.lower()
        ret = cmd.Cmd.parseline(self, line)
        return ret

    def do_EOF(self, line):
        self.safely_quit()

    def default(self, line):
        self.console.print(f"[italic red]Command '{line}' not recognized [/italic red]")
        return

    def emptyline(self):
        return 

    # def default(self, line):
    #     print 'default(%s)' % line
    #     return cmd.Cmd.default(self, line)


    def clean_input(self, inpt) -> str:
        """strips excessive whitespace and from a raw input, converts it to lowercase and returns a tuple of the first command and the args"""
        inpt = inpt.lower().split()
        cmd = inpt[0]
        args = inpt[1:]

        return cmd, args

    def do_help(self, cmd=None, args=None):
        """displays a list of commands"""

        max_width = max([len(c) for c in COMMANDS.keys()])
        for command, description in COMMANDS.items():
            justified_command = f"{command}".ljust(max_width)
            self.console.print(f"\t[bold]{justified_command}[/bold]\t{description}")

    def do_party(self, args):
        """displays info about the player as well as each of the Character members of the party"""

        self.console.print(self.player)

    def do_tracks(self, track):
        """displays all the tracks, or a specific track""" 
        # TODO error handle track not in 

        self.console.log(track)
        if len(track) > 0:
           self.specific_track(track)

        else: 
            self.all_tracks()
            
    def all_tracks(self):
        """displays all tracks"""

        max_width = max([len(key) for key in TRACKS.keys()])
        for track, desc in TRACKS_META["descriptions"].items():
            just_track = f"{track}:".ljust(max_width)
            color = get_track_color(track)
            self.console.print(f"\t[bold {color}]{just_track}[/bold {color}]\t{desc}")
        self.console.print(f"\n\tType [bold]tracks <track>[/bold] information on a specific track") 
    
    
    def specific_track(self, the_track):
        """displays a single track"""
        for track in TRACKS_META["descriptions"].keys():
            if the_track.lower() == track.lower():
                color = get_track_color(track)
                self.console.print(f"\t[bold {color}]{track}[/bold {color}]\t{TRACKS_META['descriptions'][track]}\n")
                
                max_width = max([len(atk['name']) for atk in TRACKS[track]])
                self.console.print(f"\t[bold]  {'attack'.ljust(max_width)}\t{'target'.ljust(len('a single enemy'))}\toutput range\tdescription[/bold]")
                for i, atk in enumerate(TRACKS[track]):
                    justified_name = f"{atk['name']}".ljust(max_width)
                    self.console.print(f"\t{i+1} [bold]{justified_name}[/bold]\t{TARGET2STRING[atk['target']]}\t{str(atk['range']).ljust(len('output range'))}\t{atk['description']}")

    def do_inventory(self, args=None):
        """displays the inventory of all characters or a specified character"""
       
        if args and len(args) > 0 and args[0].isnumeric():
            idx = int(args[0])
            self.console.print(self.player.show_inventory(idx=idx))
        else:
            self.console.print(self.player.show_inventory())

    def fight(self):
        # move this corny stuff to take place once a fight is begun
        max_width = len("3 Factory")
        self.console.print(f"\t0 [bold]{'Cancel'.ljust(max_width)}[/bold]\tI actually am too scared to do combat rn")
        self.console.print(f"\t1 [bold yellow]{'Street'.ljust(max_width)}[/bold yellow]\t{ENCOUTERS_META['descriptions']['Street']}")
        self.console.print(f"\t2 [bold orange1]{'Tower'.ljust(max_width)}[/bold orange1]\t{ENCOUTERS_META['descriptions']['Tower']}")
        self.console.print(f"\t3 [bold bright_red]{'Factory'.ljust(max_width)}[/bold bright_red]\t{ENCOUTERS_META['descriptions']['Factory']}")

        inpt = self.console.input("\n[italic yellow]Select an encounter[/italic yellow]: ")
        # (inpt.lower() not in ["cancel", "street", "tower", "factory"])
        while inpt == "" or not inpt.isnumeric() or int(inpt) < 0 or int(inpt) > 3:
            self.console.print(f"[italic red]invalid encounter selector[/italic red]")
            inpt = self.console.input("\n[italic yellow]Select an encounter: [/italic yellow]")

        if inpt.lower() == "cancel" or int(inpt) == 0:
            return 

            # BEFORE A FIGHT BEGINS
            # self.player.fighting = True
            # save the game
        elif inpt.lower() == "steet" or int(inpt) == 1:
            self.console.print(f"commense street fight")
            Encounter(self.player).resolve()
        else:
            # self.player.fighting = True
            self.console.print(f"under construction")

    def safely_quit(self):
        """saves the user file before exiting"""
        try:
            self.console.print(f"\n[italic yellow]Saving game to file... [/italic yellow]")
            self.player.save()
            sys.exit(0)
        except SystemExit:
            os._exit(0)







    