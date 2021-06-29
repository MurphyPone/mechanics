# Mechanics

A strategy rpg shell-based game written in Python.

TODOS
- [ ] - rebranding
    - [x] - rename all tracks
    - [x] - rename all abilities
    - [ ] Solamente Botafumieros - just a lil smoke thrower
    - [ ] - come up with a cooler name:
        - "Haunted, Horrid Hamlet"
        - "Grim Grove"
        - "Cadaverous, Cursed Conurbation"
        - "Marauders' Metropolis"
        - "Battles of the Burgh, Burrough, Bailiwick"
        - "Vile, Violent Village"
- [ ] - build a cmd history - extend the [cmd](https://docs.python.org/3/library/cmd.html) module
- [ ] - finish encounter
- [ ] - dynamic shell?
- [ ] - standardize new line spacing
- [ ] - installation
    - `install.sh`
    - 



## ToonTown Stat Blocks:

```json
TRACKS = {
    "Healing": [ # toonup # entries in this list are indexed by level
        {
            "name": "Feather",
            "prop_acc": 70, # used for calculating accuracy
            "target": Target.ONE_T, # who can this attack target
            "range": (8, 10), # the output range
        },
        {
            "name": "Megaphone",
            "prop_acc": 70, 
            "target": Target.ALL_T, 
            "range": (15, 18), 
        },
        {
           "name": "Lipstick",
            "prop_acc": 70, 
            "target": Target.ONE_T, 
            "range": (25, 30), 
        },
        {
           "name": "Bamboo Cane",
            "prop_acc": 70, 
            "target": Target.ALL_T, 
            "range": (40, 45), 
        },
        {
           "name": "Pixie Dust",
            "prop_acc": 70, 
            "target": Target.ONE_T, 
            "range": (60, 70), 
        },
        {
           "name": "Juggling Cubes",
            "prop_acc": 70, 
            "target": Target.ALL_T, 
            "range": (90, 120), 
        },
        {
           "name": "High Dive",
            "prop_acc": 100, 
            "target": Target.ALL_T, 
            "range": (210, 210), 
        },
    ], 
    "Ambush": [ # trap 
        {
            "name": "Banana Peel",
            "prop_acc": 0, # used for calculating accuracy
            "target": Target.ONE_E, # who can this attack target
            "range": (10, 12), # the output range
        },
        {
            "name": "Rake",
            "prop_acc": 0, 
            "target": Target.ONE_T, 
            "range": (18, 20), 
        },
        {
            "name": "Marbles",
            "prop_acc": 0, 
            "target": Target.ONE_T, 
            "range": (30, 35), 
        },
        {
            "name": "Quicksand",
            "prop_acc": 0, 
            "target": Target.ONE_T, 
            "range": (40, 50), 
        },
        {
            "name": "Trap Door",
            "prop_acc": 0, 
            "target": Target.ONE_T, 
            "range": (60, 70), 
        },
        {
           "name": "TNT",
            "prop_acc": 0, 
            "target": Target.ONE_T, 
            "range": (90, 180), 
        },
        {
           "name": "Railroad",
            "prop_acc": 0, 
            "target": Target.ALL_T, 
            "range": (195, 195), 
        },
    ], 
    "Illusion": [ # / psychosis? # lure
        {
            "name": "$1 Bill",
            "prop_acc": 50, # used for calculating accuracy
            "target": Target.ONE_E, # who can this attack target
            "range": 0
        },
        {
            "name": "Small Magnet",
            "prop_acc": 50, 
            "target": Target.ALL_E, 
            "range": 0
        },
        {
            "name": "$5 Bill",
            "prop_acc": 60, 
            "target": Target.ONE_E, 
            "range": 0
        },
        {
            "name": "Big Magnet",
            "prop_acc": 60, 
            "target": Target.ALL_E, 
            "range": 0
        },
        {
            "name": "$10 Bill",
            "prop_acc": 70, 
            "target": Target.ONE_E, 
            "range": 0, 
        },
        {
           "name": "Lure Goggles",
            "prop_acc": 70, 
            "target": Target.ALL_E, 
            "range": 0,
        },
        {
           "name": "Presentation",
            "prop_acc": 90, 
            "target": Target.ALL_E, 
            "range": 0
        },
    ], 
    "Hex": [ # Sound
        {
            "name": "Bike Horn",
            "prop_acc": 95, # used for calculating accuracy
            "target": Target.ALL_E, # who can this attack target
            "range": (3, 3), # the output range
        },
        {
            "name": "Whistle",
            "prop_acc": 95, 
            "target": Target.ALL_E, 
            "range": (5, 7), 
        },
        {
            "name": "Bugle",
            "prop_acc": 95, 
            "target": Target.ALL_E, 
            "range": (9, 11), 
        },
        {
            "name": "Aoogah",
            "prop_acc": 95, 
            "target": Target.ALL_E, 
            "range": (14, 16), 
        },
        {
            "name": "Elephant Trunk",
            "prop_acc": 95, 
            "target": Target.ALL_E, 
            "range": (19, 21), 
        },
        {
            "name": "Foghorn",
            "prop_acc": 95, 
            "target": Target.ALL_E, 
            "range": (25, 50), 
        },
        {
            "name": "Opera Singer",
            "prop_acc": 95, 
            "target": Target.ALL_E, 
            "range": (90, 90), 
        },
    ], 
    "Physicality": [ # throw
        {
            "name": "Cupcake",
            "prop_acc": 75, # used for calculating accuracy
            "target": Target.ONE_E, # who can this attack target
            "range": (4, 6), # the output range
        },
        {
            "name": "Fruit Pie Slice",
            "prop_acc": 75, 
            "target": Target.ONE_E, 
            "range": (8, 10), 
        },
        {
            "name": "Cream Pie Slice",
            "prop_acc": 75, 
            "target": Target.ONE_E, 
            "range": (14, 17), 
        },
        {
            "name": "Whole Fruit Pie",
            "prop_acc": 75, 
            "target": Target.ONE_E, 
            "range": (24, 27), 
        },
        {
            "name": "Whole Cream Pie",
            "prop_acc": 75, 
            "target": Target.ONE_E, 
            "range": (36, 40), 
        },
        {
            "name": "Birthday Cake",
            "prop_acc": 75, 
            "target": Target.ONE_E, 
            "range": (48, 100), 
        },
        {
            "name": "Wedding Cake",
            "prop_acc": 75, 
            "target": Target.ALL_E, 
            "range": (120, 120), 
        },
    ], 
    "Precision": [ # squirt
        {
            "name": "Squirting Flower",
            "prop_acc": 95, # used for calculating accuracy
            "target": Target.ONE_E, # who can this attack target
            "range": (3, 4), # the output range
        },
        {
            "name": "Glass of Water",
            "prop_acc": 95, 
            "target": Target.ONE_E, 
            "range": (6, 8), 
        },
        {
            "name": "Squirt Gun",
            "prop_acc": 95, 
            "target": Target.ONE_E, 
            "range": (10, 12), 
        },
        {
            "name": "Seltzer Bottle",
            "prop_acc": 95, 
            "target": Target.ONE_E, 
            "range": (18, 21), 
        },
        {
            "name": "Fire Hose",
            "prop_acc": 95, 
            "target": Target.ONE_E, 
            "range": (27, 30), 
        },
        {
            "name": "Storm Cloud",
            "prop_acc": 95, 
            "target": Target.ONE_E, 
            "range": (36, 80), 
        },
        {
            "name": "Geyser",
            "prop_acc": 95, 
            "target": Target.ALL_E, 
            "range": (105, 105), 
        },
    ], 
    "Berserking": [ # drop
        {
            "name": "Flower Pot",
            "prop_acc": 50, 
            "target": Target.ONE_E, 
            "range": (10, 10), 
        },
        {
            "name": "Sandbag",
            "prop_acc": 50, 
            "target": Target.ONE_E, 
            "range": (18, 18), 
        },
        {
            "name": "Anvil",
            "prop_acc": 50, 
            "target": Target.ONE_E, 
            "range": (30, 30), 
        },
        {
            "name": "Big Weight",
            "prop_acc": 50, 
            "target": Target.ONE_E, 
            "range": (45, 45), 
        },
        {
            "name": "Safe",
            "prop_acc": 50, 
            "target": Target.ONE_E, 
            "range": (60, 60), 
        },
        {
            "name": "Grand Piano",
            "prop_acc": 50, 
            "target": Target.ONE_E, 
            "range": (85, 170), 
        },
        {
            "name": "Toontanic LMAOOOO",
            "prop_acc": 50, 
            "target": Target.ALL_E,
            "range": (180, 180),
        },
    ],
}
```