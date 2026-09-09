from ._h import *
from build import crumbs, related

def page():
    s = "relationships"
    body = hero("RELATION-<br>SHIPS", "Ghost Rider stories are about what the fire costs the people nearby. The bonds below are the load-bearing ones.", crumbs(s), kicker="Ties that survive Hell", align="right")

    body += shout("BLAZE &<br>KETCH", "Brothers by blood and curse",
        plate(p("They met as enemies in 1990, when Johnny tried to shoot the new Rider dead. They became partners in Spirits of Vengeance, learned they shared a mother, and have spent thirty years alternately saving and threatening each other — Johnny pulling Danny out of Zadkiel's service, Danny pulling Johnny off the throne of Hell. It is the spine of the franchise.")))

    body += shout("JOHNNY &<br>ROXANNE", "The love that held the devil off",
        plate(p("Roxanne's love is the reason Johnny has a soul at all; Mephisto could not collect through it. Their marriage in the 1980s is the closest the character has come to a happy ending, and her murder is the wound Percy's 2022 series still reopens: Johnny's false life in that story includes a wife who looks a great deal like her."), "right"), flip=True)

    body += shout("ROBBIE &<br>GABE", "The deal was for him",
        plate(p("Every choice Robbie makes is downstream of Gabe: the race, the acceptance of Eli, the refusal to kill for him, the fight for Hell's throne. The relationship turned literal when Eli tried to take Gabe as a host instead, and Robbie found himself fighting the thing he had become inside his brother's body."), "blue"))

    body += drift("The Spirit takes the host. The story takes everyone else.", right=True)

    body += shout("RIDER &<br>MEPHISTO", "The oldest contract",
        plate(p("Mephisto made Johnny, made Noble Kale, made Vengeance and made Cosmic Ghost Rider. He is not the Rider's nemesis so much as his author. Every attempt to break free — Zarathos's removal, the Kale bloodline's end, Johnny's coup in Damnation — is a renegotiation with the same landlord."), "right"), flip=True)

    body += shout("RIDER &<br>MIDNIGHT SONS", "The team that fits",
        plate(p("Ghost Rider does not sit comfortably on the Avengers (though both Johnny and Robbie have served). He fits with Blade, Morbius, Doctor Strange, Magik and the other characters who live at the border of Hell — the Midnight Sons of 1992, the Midnight Suns of 2022 and the Blood Hunt reunion of 2024.")))

    body += shout("RIDER &<br>PUNISHER", "Two verdicts, no appeal",
        plate(p("Castle and the Riders keep colliding because they are the same idea run through different machinery. The Penance Stare failed on him; Cosmic Ghost Rider is him; Final Vengeance briefly made him Johnny's replacement. Neither has ever been able to reform the other."), "right"), flip=True)

    body += related(["characters", "johnny-blaze", "danny-ketch", "robbie-reyes", "villains"])
    return dict(slug=s, title="Relationships", desc="The key relationships in Ghost Rider: Blaze and Ketch, Johnny and Roxanne, Robbie and Gabe, the Rider and Mephisto, the Midnight Sons and the Punisher.", keywords="Ghost Rider relationships, Blaze Ketch brothers, Roxanne, Gabe Reyes, Mephisto", body=body, vid_pos="45% 50%")
