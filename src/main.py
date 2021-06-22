#!/usr/bin/env python3
import sys
import os
from rich.console import Console

from conf import DISCORD_KEY, FIREBASE_CONFIG, CMD_PREFIX
from utils import std_embed, std_footer, COMMANDS, TARGET2STRING
from player import Player
from tracks import TRACKS, TRACKS_META
from character import get_random_character, Character

console = Console(highlight=False)

def main():

    # check if user file saved to disk
    # if player then "welcome back" else greetings 
    player = Player()
    console.rule(":gear: [bold yellow]Greetings player, Welcome to [italic]Mechanics[/italic]![/bold yellow] :gear:")

    while True:
        cmd = console.input(":gear:[yellow] Enter a command:[/yellow] ").lower()

        # move to a helper
        if cmd == "help":
             for c, desc in COMMANDS.items():
                console.print(f"\t[bold]{c}[/bold]\t\t{desc}")
        elif cmd in ["party", "p"]:
            console.print(player)
        elif cmd in ["tracks"]:
            for track, desc in TRACKS_META["descriptions"].items():
                max_width = max([len(key) for key in TRACKS.keys()])
                just_track = f"{track}:".ljust(max_width)
                console.print(f"\t[bold]{just_track}[/bold]\t{desc}")
            console.print(f"\n\tType [bold]tracks <track>[/bold] information on a specific track") 
        elif cmd == "exit" or cmd == "quit":
            safely_quit()
        else:
            console.print(f"[italic red]Command not recognized [/italic red]")
            
        
def safely_quit():
    console.print("\n[italic yellow]Saving game...[/italic yellow]")
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        safely_quit()

