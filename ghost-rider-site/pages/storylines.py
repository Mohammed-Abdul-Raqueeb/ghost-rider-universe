from ._h import *
from build import crumbs, related

def page():
    s = "storylines"
    body = hero("MAJOR<br>STORYLINES", "The arcs that define the Rider. Open any spine for the story, the creators and why it matters.", crumbs(s), kicker="Essential reading", align="right")

    S = []
    def spine(title, meta, text):
        S.append(f'<details class="reveal"><summary><h3>{title}</h3><span class="meta">{meta}</span></summary>{plate(p(*text))}</details>')

    spine("The Origin", "Marvel Spotlight #5–11 · 1972–73 · Friedrich, Ploog",
          ["The deal, the death of Crash Simpson, Roxanne's intervention and the first nights as the Ghost Rider. Ploog's art — expressive, cartoonish, genuinely spooky — set the character's tone. Read it in Ghost Rider Epic Collection: Hell on Wheels."])
    spine("The Champions", "The Champions #1–17 · 1975–78 · Isabella, Mantlo",
          ["Johnny's odd tenure on Los Angeles's short-lived super-team with Hercules, Black Widow, Angel and Iceman. Not essential, but the first time the character was placed among mainstream heroes — and a source of endless later jokes."])
    spine("The Zarathos Revelation", "Ghost Rider vol. 2 #68–81 · 1982–83 · Stern, DeMatteis; Budiansky",
          ["The last stretch of the original series introduced Centurious, named the demon inside Johnny as Zarathos, and ended with the Spirit imprisoned in the Crystal of Souls and Johnny freed. A rare superhero ending that stuck for seven years."])
    spine("Deathwatch", "Ghost Rider vol. 3 #1–7 · 1990 · Mackie, Saltares",
          ["Danny Ketch's origin and first war. Cypress Hills Cemetery, Barbara's wounding, Blackout's arrival and Deathwatch's bio-toxin scheme, in the spiked, chain-wrapped visual language that defined the decade."])
    spine("Hearts of Darkness", "Ghost Rider/Wolverine/Punisher OGN · 1991 · Mackie; Romita Jr.",
          ["Blackheart lures the three most violent men in Marvel to a town called Christ's Crown. John Romita Jr.'s painted-looking pencils made this the era's must-own graphic novel."])
    spine("Rise of the Midnight Sons", "Crossover · 1992 · Mackie et al.",
          ["Lilith escapes, the Lilin attack, and Ghost Rider and Blaze gather Morbius, the Nightstalkers and the Darkhold Redeemers. It launched the Midnight Sons line and the Spirits of Vengeance series."])
    spine("Midnight Massacre / Siege of Darkness", "Crossovers · 1993",
          ["The two follow-ups: a possessed Blade hunting his own allies, then Lilith and Zarathos allied against the Sons in a seventeen-part siege. Both are collected in the Danny Ketch Epic Collections."])
    spine("The Noble Kale Revelation", "Ghost Rider vol. 3 #77–94 · 1996–98 · Velez Jr.; Larroca",
          ["Danny learns the Spirit's true identity, meets his ancestors and discovers his brotherhood with Johnny Blaze. The series' finale, #94, was published only in 2007."])
    spine("The Hammer Lane", "Ghost Rider vol. 4 #1–6 · 2001–02 · Grayson, Kaniuga",
          ["The Marvel Knights miniseries: a road story with Johnny hunted by a biker gang and the demon Gressil. Notable for a new, skeletal-lean look that anticipated the 2005 relaunch."])
    spine("Road to Damnation", "Ghost Rider vol. 5 #1–6 · 2005–06 · Ennis, Crain",
          ["Johnny in Hell, on an endless road, offered escape by the angel Malachi in exchange for hunting the demon Kazann. Ennis's black humour and Crain's painted, near-photographic art made it the definitive modern take."])
    spine("Trail of Tears", "6 issues · 2007 · Ennis, Crain",
          ["A Civil War-era Ghost Rider, the freed slave Caleb, hunts the Confederate irregulars who murdered his family. Ennis's finest Rider story and proof the concept works in any century."])
    spine("Vicious Cycle", "Ghost Rider vol. 6 #1–5 · 2006 · Way, Texeira",
          ["Johnny escapes Hell, dragging Lucifer's fragmented soul with him. The start of Way's run, which continued into the road-horror arcs that led to Jason Aaron."])
    spine("Hell-Bent & Heaven Bound", "Ghost Rider vol. 6 #20–25 · 2008 · Aaron, Boschi",
          ["Aaron's opening: Johnny discovers the Spirits' angelic origin and the archangel Zadkiel's betrayal, meets the Caretaker's granddaughter Sara, and goes to war with a Heaven that is no longer holy."])
    spine("Heaven's on Fire", "6 issues · 2009 · Aaron, Boschi",
          ["Zadkiel takes Heaven. Blaze and Ketch, reunited, lead an army of Riders across the multiverse to cast him down. The finale of the modern mythology."])
    spine("Ghost Rider: Danny Ketch", "5 issues · 2008–09 · Spurrier, Saltares",
          ["Danny as an addict, harvesting other Riders for Zadkiel while trying to feel the fire again. The series that gave the Ketch Rider its adult voice."])
    spine("Engines of Vengeance", "All-New Ghost Rider #1–5 · 2014 · Smith, Moore",
          ["Robbie Reyes's origin: the race, the murder, the Charger and Eli. Tradd Moore's kinetic art made it one of the decade's best-looking Marvel debuts."])
    spine("Ghost Racers", "4 issues · 2015 · Smith, Gedeon",
          ["Secret Wars tie-in: every Rider in one arena, forced to race for Arcade until Robbie leads a breakout. Pure spectacle."])
    spine("Cosmic Ghost Rider", "Thanos #13–18; Cosmic Ghost Rider #1–5 · 2017–18 · Cates, Shaw",
          ["Frank Castle, dead, damned, Rider, herald, then time-travelling babysitter of infant Thanos. The comic that turned a joke into a franchise."])
    spine("Damnation", "Doctor Strange: Damnation #1–4 and tie-ins · 2018 · Cates, Spencer; Reis",
          ["Mephisto's Las Vegas casino, the Midnight Sons reunited, and Johnny Blaze seizing the throne of Hell. The pivot for everything since."])
    spine("King of Hell", "Ghost Rider vol. 9 #1–7 · 2019–20 · Brisson, Kuder",
          ["Johnny rules Hell and Danny has to stop him, while Lilith and the other Hell-lords manoeuvre for the throne and Alejandra Jones pays the price."])
    spine("Unchained", "Ghost Rider vol. 10 #1–5 · 2022 · Percy, Smith",
          ["A small-town Johnny Blaze with a perfect life discovers it is a prison built by Hell. The road, the Spirit and Agent Warroad follow. Percy's run continued through Weapons of Vengeance (2023) and Final Vengeance (2024)."])
    spine("Spirits of Vengeance / Spirits of Violence", "6 + 5 issues · 2024–26 · Pirzada; Davidson",
          ["The Riders assembled: Blaze, Ketch, Reyes, Kushala, Hellverine and the newcomer Fantasma against the Spirit of Violence — Barbara Ketch, back from the dead. Marvel's \"Violent Era\"."])

    body += '<section class="band"><div class="spines">' + "".join(S) + "</div></section>"
    body += related(["comics", "comic-history", "timeline", "villains", "hell"])
    return dict(slug=s, title="Major Storylines", desc="The essential Ghost Rider storylines: the origin, the Zarathos revelation, Deathwatch, Hearts of Darkness, Rise of the Midnight Sons, Road to Damnation, Trail of Tears, Heaven's on Fire, Damnation, King of Hell and the Violent Era.", keywords="Ghost Rider storylines, Road to Damnation, Trail of Tears, Heaven's on Fire, Damnation, Hearts of Darkness, Siege of Darkness", body=body, vid_pos="50% 50%")
