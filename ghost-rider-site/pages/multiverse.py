from ._h import *
from build import crumbs, related

def page():
    s = "multiverse"
    body = hero("MULTIVERSE", "Every Earth gets the Rider it deserves. The concept travels well: change the vehicle, the century or the host, and the skull still burns.", crumbs(s), kicker="Alternate Earths", align="center", cue=False)

    B = []
    def earth(code, name, text, cls=""):
        B.append(f'<div class="plate reveal {cls}"><div class="earth">{code}</div><h3>{name}</h3>{p(text)}</div>')

    earth("Earth-616", "The main Marvel Universe", "Blaze, Ketch, Reyes, Alejandra, Kushala, the prehistoric Rider, Vengeance, Hellverine. Everything else on this site unless noted.")
    earth("Earth-928", "Ghost Rider 2099", "Zero Cochrane's chromed, AI-built Rider in Transverse City. 25 issues (1994–96) by Len Kaminski and Chris Bachalo, later Ashley Wood.", "cosmic")
    earth("Earth-TRN666", "Cosmic Ghost Rider", "The future where Thanos won and Frank Castle became Mephisto's Rider and Galactus's herald. Introduced in Thanos #13 (2017); now a recurring visitor to the main timeline.", "cosmic")
    earth("Earth-1610", "Ultimate Ghost Rider", "In Ultimate Comics Avengers 2 (2010), Johnny Blaze was a biker who made a deal with Satan for himself and his girlfriend and returned twenty years later to hunt the men who killed them — including a future Vice President.")
    earth("Earth-15513", "Ghost Racers (Battleworld)", "Secret Wars domain where Riders of every kind — Blaze, Reyes, Slade, a Rider on a dinosaur — race in Arcade's Killiseum.")
    earth("Earth-9997", "Earth X", "Alex Ross and Jim Krueger's future: Ghost Rider among the transformed heroes of a world where everyone has powers.")
    earth("Earth-2149", "Marvel Zombies", "A zombified Ghost Rider appears among the infected heroes of the Marvel Zombies universe.")
    earth("Earth-199999 / TV", "Agents of S.H.I.E.L.D.", "Gabriel Luna's Robbie Reyes (season 4, 2016–17): the Hell Charger, the Darkhold and a brief glimpse of a biker Rider who passed him the curse. Whether it stands in MCU continuity is still debated.", "blue")
    earth("Sony films", "Nicolas Cage's Johnny Blaze", "Ghost Rider (2007) and Spirit of Vengeance (2012), with Peter Fonda and Ciarán Hinds as the devil and Sam Elliott as Carter Slade. Separate from the MCU.")
    earth("Earth-199999", "Marvel Studios (2028)", "Ryan Gosling's Johnny Blaze, directed by Shawn Levy. The first Ghost Rider film inside the Marvel Cinematic Universe, scheduled for July 28, 2028.")
    earth("Midnight Suns", "Video game (2022)", "Firaxis's tactical RPG puts Robbie Reyes on a team with Blade, Magik, Nico Minoru and Wolverine against Lilith — a video-game universe with its own comic tie-ins.", "blue")
    earth("What If…?", "Alternate takes", "What If? Ghost Rider (2018) put a comics twist on the origin, and the animated What If…? season 3 (2024) gave the character his Marvel Studios animated debut.")

    body += '<section class="band"><div class="branches">' + "".join(B) + "</div></section>"
    body += drift("Different road. Same passenger.", right=True)
    body += related(["other-riders", "movies", "lore", "vehicles", "storylines"])
    return dict(slug=s, title="Multiverse", desc="Ghost Rider across the multiverse: Ghost Rider 2099, Cosmic Ghost Rider, Ultimate Ghost Rider, Ghost Racers, Earth X, Marvel Zombies, Agents of S.H.I.E.L.D., the films and Midnight Suns.", keywords="Ghost Rider 2099, Cosmic Ghost Rider, Ultimate Ghost Rider, Earth-928, Earth-TRN666, Ghost Racers", body=body, vid_pos="50% 50%")
