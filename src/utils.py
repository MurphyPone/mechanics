import math

import discord 
from tracks import Target


def millify(n):
    millnames = ['','K','M',' B',' T']
    n = int(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '{:.1f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

TARGET2STRING = {
    Target.ALL_E: "all enemies",
    Target.ONE_E: "a single enemy",
    Target.ALL_T: "all allies",
    Target.ONE_T: "a single ally",
}



SAVE_FILE = "save_file.json"

## Discord utils
def std_embed(title=None, description=None):
    if title and description:
        embed = discord.Embed(
            color=0x6666FF,
            title=title,
            description=description
        )

    elif title and not description:
        embed = discord.Embed(
            color=0x6666FF,
            title=title
        )
    elif description and not title:
        embed = discord.Embed(
            color=0x6666FF,
            title=title
        )
    else: 
        embed = discord.Embed(
            color=0x6666FF
        )

    return embed 

def std_footer(embed):
    embed.add_field(
        name="idk brug just leave me aloen",
        value="don't talk about it ",
        inline=False
    )