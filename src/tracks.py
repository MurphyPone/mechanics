from enum import Enum
class Target(Enum):
    # 0 reserved for the self
    ONE_T = 1 # Any other member of the party
    ALL_T = 2 # All other members of the party
    ONE_E = 3 # Any single enemy
    ALL_E = 4 # All enemies

TRACKS = {
    "Healing": [ # toonup # entries in this list are indexed by level
        {
            "name": "Feather",
            "prop_acc": 70, # used for calculating accuracy
            "target": Target.ONE_T, # who can this attack target
            "range": range(8, 10+1), # the output range
        },
        {
            "name": "Megaphone",
            "prop_acc": 70, 
            "target": Target.ALL_T, 
            "range": range(15, 18+1), 
        },
        {
           "name": "Lipstick",
            "prop_acc": 70, 
            "target": Target.ONE_T, 
            "range": range(25, 30+1), 
        },
        {
           "name": "Bamboo Cane",
            "prop_acc": 70, 
            "target": Target.ALL_T, 
            "range": range(40, 45+1), 
        },
        {
           "name": "Pixie Dust",
            "prop_acc": 70, 
            "target": Target.ONE_T, 
            "range": range(60, 70+1), 
        },
        {
           "name": "Juggling Cubes",
            "prop_acc": 70, 
            "target": Target.ALL_T, 
            "range": range(90, 120+1), 
        },
        {
           "name": "High Dive",
            "prop_acc": 100, 
            "target": Target.ALL_T, 
            "range": range(210, 210+1), 
        },
    ], 
    "Ambush": [ # trap 
        {
            "name": "Banana Peel",
            "prop_acc": 0, # used for calculating accuracy
            "target": Target.ONE_E, # who can this attack target
            "range": range(10, 12+1), # the output range
        },
        {
            "name": "Rake",
            "prop_acc": 0, 
            "target": Target.ONE_T, 
            "range": range(18, 20+1), 
        },
        {
            "name": "Marbles",
            "prop_acc": 0, 
            "target": Target.ONE_T, 
            "range": range(30, 35+1), 
        },
        {
            "name": "Quicksand",
            "prop_acc": 0, 
            "target": Target.ONE_T, 
            "range": range(40, 50+1), 
        },
        {
            "name": "Trap Door",
            "prop_acc": 0, 
            "target": Target.ONE_T, 
            "range": range(60, 70+1), 
        },
        {
           "name": "TNT",
            "prop_acc": 0, 
            "target": Target.ONE_T, 
            "range": range(90, 180+1), 
        },
        {
           "name": "Railroad",
            "prop_acc": 0, 
            "target": Target.ALL_T, 
            "range": range(195, 195+1), 
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
            "range": range(60, 70+1), 
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
            "range": range(3, 3+1), # the output range
        },
        {
            "name": "Whistle",
            "prop_acc": 95, 
            "target": Target.ALL_E, 
            "range": range(5, 7+1), 
        },
        {
            "name": "Bugle",
            "prop_acc": 95, 
            "target": Target.ALL_E, 
            "range": range(9, 11+1), 
        },
        {
            "name": "Aoogah",
            "prop_acc": 95, 
            "target": Target.ALL_E, 
            "range": range(14, 16+1), 
        },
        {
            "name": "Elephant Trunk",
            "prop_acc": 95, 
            "target": Target.ALL_E, 
            "range": range(19, 21+1), 
        },
        {
            "name": "Foghorn",
            "prop_acc": 95, 
            "target": Target.ALL_E, 
            "range": range(25, 50+1), 
        },
        {
            "name": "Opera Singer",
            "prop_acc": 95, 
            "target": Target.ALL_E, 
            "range": range(90, 90+1), 
        },
    ], 
    "Physicality": [ # throw
        {
            "name": "Cupcake",
            "prop_acc": 75, # used for calculating accuracy
            "target": Target.ONE_E, # who can this attack target
            "range": range(4, 6+1), # the output range
        },
        {
            "name": "Fruit Pie Slice",
            "prop_acc": 75, 
            "target": Target.ONE_E, 
            "range": range(8, 10+1), 
        },
        {
            "name": "Cream Pie Slice",
            "prop_acc": 75, 
            "target": Target.ONE_E, 
            "range": range(14, 17+1), 
        },
        {
            "name": "Whole Fruit Pie",
            "prop_acc": 75, 
            "target": Target.ONE_E, 
            "range": range(24, 27+1), 
        },
        {
            "name": "Whole Cream Pie",
            "prop_acc": 75, 
            "target": Target.ONE_E, 
            "range": range(36, 40+1), 
        },
        {
            "name": "Birthday Cake",
            "prop_acc": 75, 
            "target": Target.ONE_E, 
            "range": range(48, 100+1), 
        },
        {
            "name": "Wedding Cake",
            "prop_acc": 75, 
            "target": Target.ALL_E, 
            "range": range(48, 100+1), 
        },
    ], 
    "Precision": [ # squirt
        {
            "name": "Squirting Flower",
            "prop_acc": 95, # used for calculating accuracy
            "target": Target.ONE_E, # who can this attack target
            "range": range(3, 4+1), # the output range
        },
        {
            "name": "Glass of Water",
            "prop_acc": 95, 
            "target": Target.ONE_E, 
            "range": range(6, 8+1), 
        },
        {
            "name": "Squirt Gun",
            "prop_acc": 95, 
            "target": Target.ONE_E, 
            "range": range(10, 12+1), 
        },
        {
            "name": "Seltzer Bottle",
            "prop_acc": 95, 
            "target": Target.ONE_E, 
            "range": range(18, 21+1), 
        },
        {
            "name": "Fire Hose",
            "prop_acc": 95, 
            "target": Target.ONE_E, 
            "range": range(27, 30+1), 
        },
        {
            "name": "Storm Cloud",
            "prop_acc": 95, 
            "target": Target.ONE_E, 
            "range": range(36, 80+1), 
        },
        {
            "name": "Geyser",
            "prop_acc": 95, 
            "target": Target.ALL_E, 
            "range": range(105, 105+1), 
        },
    ], 
    "Berserking": [ # drop
        {
            "name": "Flower Pot",
            "prop_acc": 50, 
            "target": Target.ONE_E, 
            "range": range(10, 10+1), 
        },
        {
            "name": "Sandbag",
            "prop_acc": 50, 
            "target": Target.ONE_E, 
            "range": range(18, 18+1), 
        },
        {
            "name": "Anvil",
            "prop_acc": 50, 
            "target": Target.ONE_E, 
            "range": range(30, 30+1), 
        },
        {
            "name": "Big Weight",
            "prop_acc": 50, 
            "target": Target.ONE_E, 
            "range": range(45, 45+1), 
        },
        {
            "name": "Safe",
            "prop_acc": 50, 
            "target": Target.ONE_E, 
            "range": range(60, 60+1), 
        },
        {
            "name": "Grand Piano",
            "prop_acc": 50, 
            "target": Target.ONE_E, 
            "range": range(85, 170+1), 
        },
        {
            "name": "Toontanic LMAOOOO",
            "prop_acc": 50, 
            "target": Target.ALL_E,
            "range": range(180, 180+1),
        },
    ],
}

TRACKS_META = {
    "descriptions": {
        "Healing": "heal other members of your party with medium-high accuracy",
        "Ambush": "lay a trap that deals huge damage, but the targeted enemy must be lured onto the trap.",
        "Illusion": "lure enemies with low-medium accuracy, granting a damage buff for Physicality and Precision attacks.  Lured enemies activate any traps in front of them.",
        "Hex": "cast a blanket of high accuracy, medium damage to all enemies simultanesouly.  Hexing enemies disillusions them.",
        "Physicality": "deal high damage with medium accuracy",
        "Precision": "deal medium damage with high accuracy",
        "Berserking": "unleash blind, inaccurate fury with high damage.  Lured enemies will always dodge a berserking attack.",
    },
    "xp_unlock":    [0,  20, 100, 800, 2000, 6000, 10000],
    "xp_use":       [1,  2,  4,   8,   16,   32,   64],
    "max_holdable": [20, 15, 15,  10,  7,    3,    1],
    "color":        ["purple", "khaki3", "green", "slate_blue1", "orange1", "plum1", "dark_slate_gray1"]
}

