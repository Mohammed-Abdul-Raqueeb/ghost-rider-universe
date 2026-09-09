from ._h import *
from build import crumbs, related

def page():
    s = "vehicles"
    body = hero("GHOST RIDER<br>VEHICLES", "The ride is part of the curse. Motorcycles that summon themselves, a Charger that drives through walls, a mammoth, a horse, a chromed 2099 chopper and one very fast Hell-Harley.", crumbs(s), kicker="The garage", wide=True)

    G = []
    def bay(name, owner, text, fl, cls=""):
        G.append(f'<div class="plate reveal {cls}"><h3>{name}</h3><span class="owner">{owner}</span>{p(text)}{facts(fl)}</div>')

    bay("Johnny Blaze's Hellfire Cycle", "Johnny Blaze · 1972–present",
        "Johnny's earliest bikes were ordinary stunt machines that transformed with him: flame from the wheels, no engine sound, and the ability to ride across water, up walls and along beams of hellfire. In the original series the bike was often a Harley-Davidson-styled chopper; the 2007 film made it a heavily modified Panhead-style custom that became a stretched, flaming skeleton on transformation.",
        [("Powers", "Hellfire wheels, wall and water riding, hellfire-beam travel"), ("Origin", "Mundane bike mystically altered by Zarathos"), ("Film version", "Custom chopper built for the 2007 production")])
    bay("The Hell Cycle", "Danny Ketch · 1990–present",
        "The motorcycle Danny found in the Cypress Hills junkyard. Its gas cap bore the sigil that triggered his first transformation; the bike could appear wherever he was, ride on walls and ceilings, and reshape itself into a spiked, flame-wheeled machine. It is the most iconic of the Rider bikes and the source of the term \"Hell Cycle\".",
        [("Powers", "Self-summoning, vertical riding, hellfire trail, bonded to the Spirit"), ("Origin", "Mystic vehicle tied to Noble Kale's power"), ("Design", "Javier Saltares; spiked fairing, skull motifs")])
    bay("The Hell Charger", "Robbie Reyes · 2014–present",
        "A matte-black 1969 Dodge Charger borrowed from Canelo's Auto and Body, bound to Eli Morrow's ghost. Flame vents from the wheel wells; it can drive through solid walls, teleport Robbie into the driver's seat from anywhere, and let him see through its windshield remotely. It is as much a character as its driver.",
        [("Powers", "Teleportation, phasing through walls, remote sight, hellfire chain from the trunk"), ("Origin", "Eli's remains bound to the frame"), ("Model", "1969 Dodge Charger")], "blue")
    bay("Banshee", "Carter Slade · 1967",
        "The white stallion of the Western Ghost Rider. Slade dusted horse and rider in phosphorescent powder so that both glowed in the dark, and rode Banshee against outlaws across the Texas frontier.",
        [("Powers", "None — speed, training and stagecraft"), ("Origin", "A gift after Slade's recovery"), ("Legacy", "Later Phantom Riders kept the tradition")])
    bay("Vengeance's Bike", "Michael Badilino · 1992",
        "A motorcycle covered in bone spurs and blades that matched its rider's spiked skull. Like the Hell Cycle it was summoned rather than parked, and it burned with Vengeance's purple flame.",
        [("Powers", "Summoning, blade-edged bodywork, hellfire"), ("Origin", "Granted by Mephisto with the Spirit")])
    bay("The 2099 Cycle", "Zero Cochrane · 1994",
        "A chromed, transforming machine in a cyberpunk city. Ghost Rider 2099's bike was as much a piece of hardware as its rider, capable of reconfiguring and interfacing with the Ghostworks network.",
        [("Powers", "Transformation, network interface"), ("Origin", "Built by the Ghostworks AIs")], "cosmic")
    bay("The Hell-Harley", "Cosmic Ghost Rider · 2017",
        "Frank Castle's cosmic motorcycle: a bike that rides through space, time and across the surface of Galactus. It laughs at physics because its rider is a herald of the World-Devourer.",
        [("Powers", "Space flight, time travel, cosmic hellfire"), ("Origin", "Mephisto's bike, upgraded by the Power Cosmic")], "cosmic")
    bay("The Mammoth", "Ghost Rider, 1,000,000 BC",
        "A woolly mammoth wreathed in hellfire, ridden by the first Spirit of Vengeance against the tribe that slaughtered his people. It set the rule that every Rider rides something appropriate to its era — and that the era does not need to have invented the wheel.",
        [("Powers", "Hellfire, size, prehistoric intimidation"), ("Origin", "Marvel Legacy #1 (2017)")])
    bay("Ghost Racers", "Secret Wars · 2015",
        "In the Killiseum arena on Battleworld, Riders from across the multiverse — Blaze on a bike, Reyes in the Charger, Slade on a horse, a Rider on a dinosaur — raced for the entertainment of Arcade. Ghost Racers (Felipe Smith, Juan Gedeon) is the fullest catalogue of Rider vehicles ever drawn.",
        [("Powers", "Every kind"), ("Origin", "Secret Wars (2015) tie-in, 4 issues")])

    body += '<section class="band"><div class="garage">' + "".join(G) + "</div></section>"
    body += drift("A Ghost Rider does not need a key. The ride is already listening.", right=True)
    body += related(["weapons", "powers", "robbie-reyes", "danny-ketch", "multiverse"])
    return dict(slug=s, title="Ghost Rider Vehicles", desc="Every Ghost Rider vehicle: Johnny Blaze's hellfire cycle, Danny Ketch's Hell Cycle, Robbie Reyes's 1969 Dodge Charger, Banshee, the 2099 cycle, the Hell-Harley, the mammoth and Ghost Racers.", keywords="Hell Cycle, Hell Charger, 1969 Dodge Charger, Ghost Rider motorcycle, Ghost Racers, Banshee", body=body, vid_pos="50% 55%")
