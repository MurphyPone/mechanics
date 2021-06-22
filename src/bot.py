import discord 
from discord.ext import commands, tasks
import pyrebase 
from datetime import datetime

from conf import DISCORD_KEY, FIREBASE_CONFIG, CMD_PREFIX
from utils import std_embed, std_footer, COMMANDS, TARGET2STRING
from player import Player
from tracks import TRACKS, TRACKS_META
from character import get_random_character, Character

# initial setup
client = commands.Bot(command_prefix=CMD_PREFIX)
client.remove_command('help')

# Firebase config
firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
db = firebase.database()
# create 'users' path if none exists
if not db.child('users').shallow().get().val():
    db.child("users")
    print("Initializing users database")

# debug commands
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("God, I love Toontown"))
    print('[LOG] mechanics coming online')

# Interaction commands
@client.command(name="generate_party", aliases=["gen_party"])
async def generate_party(ctx):
    player = Player()
    player.add_party_member(Character())

    embed = std_embed(title="Party Overview")
    for char in player.party:
        embed.add_field(name=f"{char.name}", value=f"{char.__repr__()}", inline=False)

    # push the party to the database
    payload = player.to_dict()
    payload["username"] = f"@{ctx.message.author.name}"
    key = str(ctx.message.author.id)

    db.child("users").child(key).set(payload)
    print(f'[LOG] Creating user database entry for {ctx.message.author.name}')

    await ctx.send(embed=embed)

@client.command(name="view_party", aliases=["vp"])
async def generate_party(ctx): 
    embed = std_embed(title="your party")
    
    # If user in db already  
    # print( str(ctx.message.author.id), list(db.child("users").shallow().get().val()))
    if str(ctx.message.author.id) in list(db.child("users").shallow().get().val()):
        # recreated Player instance from ordered dict??
        player_db = db.child("users").child(str(ctx.message.author.id)).get()
        player = Player(dic=player_db.val())
        
        for char in player.party:
            embed.add_field(name=f"{char.name}", value=f"{char.__repr__()}", inline=False)
        
    
    else: # prompt the user to generate a p
        embed.add_field(name=f"You need to create a party!", value=f"`{CMD_PREFIX} gen_party`", inline=False)
    await ctx.send(embed=embed)

@client.command(name="inventory", aliases=["inv"])
async def inventory(ctx, args=None): 
    
    if str(ctx.message.author.id) in list(db.child("users").shallow().get().val()):
        # recreated Player instance from ordered dict??
        player_db = db.child("users").child(str(ctx.message.author.id)).get()
        player = Player(dic=player_db.val())
        
        if len(player.party) == 1:
            embed = std_embed(title=f"{player.party[0].name}'s inventory")
            for k,v in player.party[0].inventory.items():
                embed.add_field(name=k, value=v, inline=False)        
    
    
    else: # prompt the user to generate a p
        embed.add_field(name=f"You need to create a party!", value=f"`{CMD_PREFIX} gen_party`", inline=False)
    await ctx.send(embed=embed)



# TODO disband party
@client.command(name="disband_party", aliases=["dbp"])
async def disband_party(ctx): 
    embed = std_embed()
    embed.add_field(name=f"disband", value=f"Are you sure you want to disband your party? This action cannot be undone.  You will lose all your party members and be given a new first level character\n`yes`, `no`", inline=False)
    await ctx.send(embed=embed)

@client.command(name="help", aliases=["h"])
async def help(ctx, *args):
    embed = std_embed(title="help")
    if len(args) == 0:
        for cmd in COMMANDS:
            embed.add_field(name=cmd["name"], value=cmd["description"], inline=False)
        
    else:
        print(args)
        if args[0] == "tracks":
            # info on specific track
            if len(args) > 1 and args[1] in TRACKS.keys(): 
                verb = "heals" if args[1] == "Healing" else "deals"
                
                for atk in TRACKS[args[1]]:     
                    rng, tgt = atk["range"], TARGET2STRING[atk["target"]]
                    embed.add_field(name=atk["name"], value=f"{verb} {rng} hit points to {tgt}", inline=False)
            
            else: # info on all track
                for k,v in TRACKS_META["descriptions"].items():
                    embed.add_field(name=k, value=v, inline=False)
            
            embed.add_field(name="additional help", value=f"`{CMD_PREFIX} help tracks <track>` for more information about a specific track", inline=False)

    await ctx.send(embed=embed)





client.run(DISCORD_KEY)