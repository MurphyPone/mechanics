#!/usr/bin/env python3
import sys
import os
import json
from rich.console import Console

from utils import COMMANDS, TARGET2STRING, SAVE_FILE
from command_parser import *
from player import Player
from tracks import TRACKS, TRACKS_META, get_track_color
from character import get_random_character, Character
from lore import PROLOGUE


console = Console(highlight=False)
player = None

if os.path.isfile(SAVE_FILE):
    with open(SAVE_FILE, "r") as f:
        player_dict = json.load(f)
        player = Player(player_dict)
    console.rule(":gear: [bold yellow]Greetings player, Welcome to [italic]Mechanics[/italic]![/bold yellow] :gear:")
else:
    player = Player()
    console.rule(":gear: [bold yellow]Greetings Player, welcome back to [italic]Mechanics[/italic]![/bold yellow] :gear:")
    console.print(f"[italic]{PROLOGUE}[/italic]")

def main():

    # check if user file saved to disk
    # if player then "welcome back" else greetings

    while True:
        inpt = console.input(":gear:[yellow] Enter a command:[/yellow] ").lower().split(' ')
        cmd = inpt[0]
        args = inpt[1:]
        console.log(f"cmd: {cmd}, args: {args}")

        # TODO move commands into "in-combat" and "not-in-combat" groups
        # move to a helper that parses commands
        if cmd == "":
            pass

        elif cmd in ["help", "h"]:
            max_width = max([len(c) for c in COMMANDS.keys()])
            for c, desc in COMMANDS.items():
                just_cmd = f"{c}".ljust(max_width)
                console.print(f"\t[bold]{just_cmd}[/bold]\t{desc}")

        elif cmd in ["party", "p"]:
            console.print(player)

        elif cmd in ["tracks"]:
            if len(args) > 0:
                for track in TRACKS_META["descriptions"].keys():
                    if args[0].lower() == track.lower():
                        color = get_track_color(track)
                        console.print(f"\t[bold {color}]{track}[/bold {color}]\t{TRACKS_META['descriptions'][track]}\n")
                        
                        max_width = max([len(atk['name']) for atk in TRACKS[track]])
                        console.print(f"\t[bold]  {'attack'.ljust(max_width)}\t{'target'.ljust(len('a single enemy'))}\toutput range[/bold]")
                        for i, atk in enumerate(TRACKS[track]):
                            just_name = f"{atk['name']}".ljust(max_width)
                            console.print(f"\t{i+1} [bold]{just_name}[/bold]\t{TARGET2STRING[atk['target']]}\t{atk['range']}")

            else: # just `tracks`
                max_width = max([len(key) for key in TRACKS.keys()])
                for track, desc in TRACKS_META["descriptions"].items():
                    just_track = f"{track}:".ljust(max_width)
                    color = get_track_color(track)
                    console.print(f"\t[bold {color}]{just_track}[/bold {color}]\t{desc}")
                console.print(f"\n\tType [bold]tracks <track>[/bold] information on a specific track") 
        
        elif cmd in ["inventory", "i"]:
            if len(args) > 0:
                # TODO typecheck that the arg is an int
                console.print(player.show_inventory(int(args[0])))
            else:
                console.print(player.show_inventory())

        elif cmd in ["fight"]:
            pass

        elif cmd == "exit" or cmd == "quit":
            safely_quit()
        else:
            console.print(f"[italic red]Command not recognized [/italic red]")
            
        
def safely_quit():
    try:
        console.print(f"\n[italic yellow]Saving game to file... [/italic yellow]")
        player.save()
        sys.exit(0)
    except SystemExit:
        os._exit(0)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        safely_quit()

