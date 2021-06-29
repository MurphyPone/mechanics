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
            "name": "Small Bandage",
            "prop_acc": 70, # used for calculating accuracy
            "target": Target.ONE_T, # who can this attack target
            "range": (8, 10), # the output range
            "description": "Apply a small bandage to a wound"
        },
        {
            "name": "Gauze",
            "prop_acc": 70, 
            "target": Target.ALL_T, 
            "range": (15, 18), 
            "description": "Wrap a wound in gauze"
        },
        {
            "name": "Potent Ointment",
            "prop_acc": 70, 
            "target": Target.ONE_T, 
            "range": (25, 30), 
            "description": "Apply a healing ointment to a wound"
        },
        {
            "name": "Large Bandage",
            "prop_acc": 70, 
            "target": Target.ALL_T, 
            "range": (40, 45), 
            "description": "Apply a larger bandage to a wound"
        },
        {
            "name": "Elixir of Rejuvination",
            "prop_acc": 70, 
            "target": Target.ONE_T, 
            "range": (60, 70), 
            "description": "Cure ailments with a nice beverage"
        },
        {
            "name": "Sap of Gondor",
            "prop_acc": 70, 
            "target": Target.ALL_T, 
            "range": (90, 120), 
            "description": "Illustrious medical aid"
        },
        {
            "name": "Messianic Invocation",
            "prop_acc": 100, 
            "target": Target.ALL_T, 
            "range": (210, 210), 
            "description": "Call upon Divine intervention"
        },
    ], 
    "Ambush": [ # trap 
        {
            "name": "Broken Glass",
            "prop_acc": 0, # used for calculating accuracy
            "target": Target.ONE_E, # who can this attack target
            "range": (10, 12), # the output range
            "description": "Throw a bottle at the feet of your foes"
        },
        {
            "name": "Trip Wire",
            "prop_acc": 0, 
            "target": Target.ONE_T, 
            "range": (18, 20), 
            "description": "May your foes trip"
        },
        {
            "name": "Spikes",
            "prop_acc": 0, 
            "target": Target.ONE_T, 
            "range": (30, 35), 
            "description": "Deliberately sharp"
        },
        {
            "name": "Acid Pool",
            "prop_acc": 0, 
            "target": Target.ONE_T, 
            "range": (40, 50),
            "description": "Throw a vile of acid which burns" 
        },
        {
            "name": "Pit",
            "prop_acc": 0, 
            "target": Target.ONE_T, 
            "range": (60, 70), 
            "description": "Dig a deep pit in front of an enemy"
        },
        {
           "name": "Bear Trap",
            "prop_acc": 0, 
            "target": Target.ONE_T, 
            "range": (90, 180), 
            "description": "Catch them ankles"
        },
        {
           "name": "Landmine",
            "prop_acc": 0, 
            "target": Target.ALL_T, 
            "range": (195, 195), 
            "description": "A large explosion"
        },
    ], 
    "Illusion": [ # / psychosis? # lure
        {
            "name": "Lamb Chop",
            "prop_acc": 50, # used for calculating accuracy
            "target": Target.ONE_E, # who can this attack target
            "range": 0,
            "description": "Allured a foe with a tasty treat"
        },
        {
            "name": "Distort Perception",
            "prop_acc": 50, 
            "target": Target.ALL_E, 
            "range": 0,
            "description": "Distort your enemies such that they approach"
        },
        {
            "name": "Mage Hand",
            "prop_acc": 60, 
            "target": Target.ONE_E, 
            "range": 0,
            "description": "Magically pull an enemy closer"
        },
        {
            "name": "Viscious Taunt",
            "prop_acc": 60, 
            "target": Target.ALL_E, 
            "range": 0,
            "description": "'stinky'"
        },
        {
            "name": "Whip",
            "prop_acc": 70, 
            "target": Target.ONE_E, 
            "range": 0, 
            "description": "Physically draw an an enemey closer"
        },
        {
           "name": "Spacial Rift",
            "prop_acc": 70, 
            "target": Target.ALL_E, 
            "range": 0,
            "description": "Tear the fabric of reality to shrink the distance between all enemies"
        },
        {
           "name": "Siren Song",
            "prop_acc": 90, 
            "target": Target.ALL_E, 
            "range": 0,
            "description": "Seduce all enemies"
        },
    ], 
    "Hex": [ # Sound
        {
            "name": "Daze",
            "prop_acc": 95, # used for calculating accuracy
            "target": Target.ALL_E, # who can this attack target
            "range": (3, 3), # the output range
            "description": "Concuss all enemies with a minor spell"
        },
        {
            "name": "Shrowded Stench",
            "prop_acc": 95, 
            "target": Target.ALL_E, 
            "range": (5, 7), 
            "description": "Break wind"
        },
        {
            "name": "Opressive Aura",
            "prop_acc": 95, 
            "target": Target.ALL_E, 
            "range": (9, 11), 
            "description": "Conjure a thick aura which stifles enemies"
        },
        {
            "name": "Cone of Flame",
            "prop_acc": 95, 
            "target": Target.ALL_E, 
            "range": (14, 16), 
            "description": "Torch all enemies before you"
        },
        {
            "name": "Lightning Strike",
            "prop_acc": 95, 
            "target": Target.ALL_E, 
            "range": (19, 21), 
            "description": "Smite foes with a bolt of lightning which chains between them"
        },
        {
            "name": "Ethereal Scythe",
            "prop_acc": 95, 
            "target": Target.ALL_E, 
            "range": (25, 50), 
            "description": "Summon a magical blade which cuts all enemies"
        },
        {
            "name": "Solamenta Botafumieros",
            "prop_acc": 95, 
            "target": Target.ALL_E, 
            "range": (90, 90), 
            "description": "Just throw a lil smoke at your enemies.  Divine smoke, but just a lil bit"
        },
    ], 
    "Physicality": [ # throw
        {
            "name": "Punch",
            "prop_acc": 75, # used for calculating accuracy
            "target": Target.ONE_E, # who can this attack target
            "range": (4, 6), # the output range
            "description": "Hit an enemy"

        },
        {
            "name": "Dagger",
            "prop_acc": 75, 
            "target": Target.ONE_E, 
            "range": (8, 10), 
            "description": "Slice and dice"

        },
        {
            "name": "Nuncucks",
            "prop_acc": 75, 
            "target": Target.ONE_E, 
            "range": (14, 17),
            "description": "Bangem around"
 
        },
        {
            "name": "Rapier",
            "prop_acc": 75, 
            "target": Target.ONE_E, 
            "range": (24, 27), 
            "description": "Filet"

        },
        {
            "name": "Pike",
            "prop_acc": 75, 
            "target": Target.ONE_E, 
            "range": (36, 40),
            "description": "Stab"
        },
        {
            "name": "Broadsword",
            "prop_acc": 75, 
            "target": Target.ONE_E, 
            "range": (48, 100), 
            "description": "Heave a mighty sword"
        },
        {
            "name": "Buster Sword",
            "prop_acc": 75, 
            "target": Target.ALL_E, 
            "range": (120, 120),
            "description": "it's bigger than you"
 
        },
    ], 
    "Precision": [ # squirt
        {
            "name": "Throw a rock",
            "prop_acc": 95, # used for calculating accuracy
            "target": Target.ONE_E, # who can this attack target
            "range": (3, 4), # the output range
            "description": "might as well be a tomatoe"

        },
        {
            "name": "Slingshot",
            "prop_acc": 95, 
            "target": Target.ONE_E, 
            "range": (6, 8),
            "description": "like throwing a rock, but a bit better" 
        },
        {
            "name": "Bow",
            "prop_acc": 95, 
            "target": Target.ONE_E, 
            "range": (10, 12), 
            "description": "fire an arrow at them" 
        },
        {
            "name": "Spear",
            "prop_acc": 95, 
            "target": Target.ONE_E, 
            "range": (18, 21), 
            "description": "put an eye out with that thing" 
        },
        {
            "name": "Cross Bow",
            "prop_acc": 95, 
            "target": Target.ONE_E, 
            "range": (27, 30), 
            "description": "stronger than you'll ever be" 
        },
        {
            "name": "Rifle",
            "prop_acc": 95, 
            "target": Target.ONE_E, 
            "range": (36, 80),
            "description": "let that puppy bark"  
        },
        {
            "name": "Golden Gun",
            "prop_acc": 95, 
            "target": Target.ALL_E, 
            "range": (105, 105), 
            "description": "that's what's up " 
        },
    ], 
    "Berserking": [ # drop
        {
            "name": "Red - Chevelle",
            "prop_acc": 50, 
            "target": Target.ONE_E, 
            "range": (10, 10),
            "description": "pump up music" 
        },
        {
            "name": "Hot Headed",
            "prop_acc": 50, 
            "target": Target.ONE_E, 
            "range": (18, 18), 
            "description": "channel anger through your fists" 
        },
        {
            "name": "Haymaker",
            "prop_acc": 50, 
            "target": Target.ONE_E, 
            "range": (30, 30), 
            "description": "Loose heavy punch" 
        },
        {
            "name": "Dive",
            "prop_acc": 50, 
            "target": Target.ONE_E, 
            "range": (45, 45),
            "description": "Dive at a foe" 
        },
        {
            "name": "Spinning Swing",
            "prop_acc": 50, 
            "target": Target.ONE_E, 
            "range": (60, 60), 
            "description": "angular momentum" 
        },
        {
            "name": "Seethe",
            "prop_acc": 50, 
            "target": Target.ONE_E, 
            "range": (85, 170), 
            "description": "vision goes red, strike with impunity" 
        },
        {
            "name": "Pact with the Devil",
            "prop_acc": 50, 
            "target": Target.ALL_E,
            "range": (180, 180),
            "description": "Death smiles as your attacks deliver souls to Hell" 
        },
    ],
}

TRACKS_META = {
    "descriptions": {
        "Healing":      "Heal other members of your party with medium-high accuracy",
        "Ambush":       "Lay a trap that deals huge damage, but the targeted enemy must be lured onto the trap.",
        "Illusion":     "Lure enemies with low-medium accuracy, granting a damage buff for Physicality and Precision attacks.  Lured enemies activate any traps in front of them.",
        "Hex":          "Cast a blanket of high accuracy, medium damage to all enemies simultanesouly.  Hexing enemies disillusions them.",
        "Physicality":  "Deal high damage with medium accuracy",
        "Precision":    "Deal medium damage with high accuracy",
        "Berserking":   "Unleash blind, inaccurate fury with high damage.  Lured enemies will always dodge a berserking attack.",
    },
    "xp_unlock":    [0,  20, 100, 800, 2000, 6000, 10000],
    "xp_use":       [1,  2,  4,   8,   16,   32,   64],
    "max_holdable": [20, 15, 15,  10,  7,    3,    1],
    # https://rich.readthedocs.io/en/stable/appendix/colors.html#appendix-colors
    "color":        ["purple", "khaki3", "green", "slate_blue1", "orange1", "plum1", "dark_slate_gray1"]
}

def get_track_color(track):
    i = 0
    for t in TRACKS.keys():
        if track.lower() == t.lower():
            return TRACKS_META["color"][i]
        i += 1
    return "white" 
