from ._h import *
from build import crumbs, related

def page():
    s = "robbie-reyes"
    body = hero("ROBBIE<br>REYES", "The Rider from Hillrock Heights. No motorcycle, no deal with the devil — just a kid, a car, a brother to protect and a dead uncle who would not stay quiet.", crumbs(s), kicker="Host · 2014 — present", cta='<a class="btn ghost" href="vehicles.html">The Hell Charger</a>')

    body += band(plate('<h2>Profile</h2>' + facts([
        ("Real name", "Roberto \"Robbie\" Reyes"),
        ("First appearance", "All-New Ghost Rider #1 (March 2014)"),
        ("Created by", "Felipe Smith, Tradd Moore"),
        ("Spirit", "Eli Morrow (ghost); later a genuine Spirit of Vengeance"),
        ("Base", "Hillrock Heights, East Los Angeles"),
        ("Family", "Gabe Reyes (brother); Eli Morrow (uncle, deceased)"),
        ("Vehicle", "1969 Dodge Charger — the Hell Charger"),
        ("Portrayed by", "Gabriel Luna, Agents of S.H.I.E.L.D. season 4 (2016–17)"),
    ]), "wide blue"))

    body += shout("THE RACE", "Death on the 101",
        plate(p("Robbie worked at Canelo's Auto and Body to keep himself and his younger brother Gabe housed. Gabe uses a wheelchair; their parents are gone. Robbie borrowed a Charger from the shop for a street race with a cash prize — and Mr. Hyde's mercenaries, hunting the car's real owner, shot him dead in the driver's seat.",
                "He stood up burning. The voice in his head introduced itself as a Spirit of Vengeance and offered a deal: power, and safety for Gabe, in exchange for a little help now and then. It was lying about the first part. Eli Morrow was Robbie's uncle, a satanist who had killed for a cult and died in prison, and the only thing he wanted was a body."), "blue"))

    body += shout("THE DESIGN", "Why he looks different",
        plate(p("Tradd Moore's Rider is built for a car, not a bike: a smooth skull like a crash helmet with a jagged mouth, blue-white flame, a jacket whose racing stripe burns, and flames venting from the collar and cuffs like exhaust. The Charger itself is the other half of the design — matte black, flame pouring from the wheel wells, capable of driving through walls and teleporting Robbie across the city.",
                "Felipe Smith's writing grounded the horror in a working-class Latino neighbourhood, with a teenage host whose main worry was making rent. It was the first Ghost Rider series in decades not to feature Blaze or Ketch as its lead, and its look became the character's most widely seen: Gabriel Luna wore it in <em>Agents of S.H.I.E.L.D.</em>, and Robbie is the Rider in <em>Marvel's Midnight Suns</em> (2022)."), "blue right"), flip=True)

    body += drift("The car was the deal. Everything Eli wanted came with the keys.", right=True)

    body += shout("AVENGER,<br>KING, RIDER", "2017 — present",
        plate(p("Robbie joined the Avengers in Jason Aaron's 2018 relaunch, where he met the prehistoric Ghost Rider, drove the Hell Charger through a Celestial's body and briefly seized the throne of Hell in <em>Avengers</em> (2020–21) to expel Eli for good. A genuine Spirit of Vengeance bonded to him afterward.",
                "He led <em>Ghost Racers</em> (2015) during <em>Secret Wars</em>, starred in his own 2016–17 series, returned in the <em>Ghost Rider: Robbie Reyes Special</em> (2024) and rejoined the wider Rider line in <em>Spirits of Violence</em> (2025–26). Where Blaze is regret and Ketch is grief, Robbie is responsibility: he took the power because someone else needed him to have it."), "blue"))

    body += related(["vehicles", "other-riders", "multiverse", "characters", "storylines"])
    return dict(slug=s, title="Robbie Reyes", desc="Robbie Reyes, the East L.A. Ghost Rider: his death in a street race, the ghost of Eli Morrow, the Hell Charger, the Avengers years and his time as King of Hell.", keywords="Robbie Reyes, Hell Charger, Eli Morrow, Gabe Reyes, All-New Ghost Rider, Agents of SHIELD, Gabriel Luna", body=body, vid_pos="50% 55%")
