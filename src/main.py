#!/usr/bin/env python3
import sys, os, json
from rich.console import Console

from utils import TARGET2STRING, SAVE_FILE
from command_parser import Parser
from player import Player
from tracks import TRACKS, TRACKS_META, get_track_color
from character import get_random_character, Character
from lore import PROLOGUE

console = Console(highlight=False)

if len(sys.argv) > 1 and sys.argv[1] in ["new"]:
    console.log("new game")
    player = Player()
    console.rule(":gear: [bold yellow]Greetings Player, welcome back to [italic]Mechanics[/italic]![/bold yellow] :gear:")
    console.print(f"[italic]{PROLOGUE}[/italic]")
else:
    console.log("Checking for save file")
    if os.path.isfile(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            player_dict = json.load(f)
            player = Player(player_dict)
        console.rule(":gear: [bold yellow]Greetings player, Welcome to [italic]Mechanics[/italic]![/bold yellow] :gear:")
    else:
        player = Player()
        console.rule(":gear: [bold yellow]Greetings Player, welcome back to [italic]Mechanics[/italic]![/bold yellow] :gear:")
        console.print(f"[italic]{PROLOGUE}[/italic]")

parser = Parser(console=console, player=player)


def main():

    # while True:
    #     inpt = console.input()
    #     parser.parse_command(inpt)
    parser.cmdloop()
        

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        parser.safely_quit()

