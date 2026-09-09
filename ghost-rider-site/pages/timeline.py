from ._h import *
from build import crumbs, related

def page():
    s = "timeline"
    body = hero("TIMELINE", "The road in order — publication milestones and the in-universe events they introduced. Larger marks are turning points.", crumbs(s), kicker="1967 → 2028")

    T = []
    def tick(year, title, text, major=False):
        T.append(f'<div class="tick{" major" if major else ""} reveal"><div class="year">{year}</div><h3>{title}</h3>{plate(p(text))}</div>')

    tick("1967", "The Western Ghost Rider", "Ghost Rider #1 introduces Carter Slade, the glowing horseman of the Texas frontier. Seven issues.", True)
    tick("1972", "Johnny Blaze", "Marvel Spotlight #5 (August): stunt rider Johnny Blaze sells his soul to save Crash Simpson and becomes the flaming-skulled Ghost Rider.", True)
    tick("1973", "The first ongoing", "Ghost Rider vol. 2 #1 (September). The Orb debuts in Marvel Team-Up #15 the same year.")
    tick("1975", "The Champions", "Johnny joins Hercules, Black Widow, Angel and Iceman in Los Angeles.")
    tick("1982", "Centurious", "Ghost Rider #74 introduces the man without a soul; Zarathos is named soon after.")
    tick("1983", "Freedom", "Ghost Rider #81 ends the series with Zarathos trapped in the Crystal of Souls and Johnny Blaze human again.", True)
    tick("1989", "Blackheart", "Mephisto's son debuts in Daredevil #270.")
    tick("1990", "Danny Ketch", "Ghost Rider vol. 3 #1 (May): a new Rider, the Penance Stare, the Hell Cycle, Deathwatch and Blackout.", True)
    tick("1991", "Hearts of Darkness", "Ghost Rider, Wolverine and the Punisher versus Blackheart in Christ's Crown.")
    tick("1992", "Midnight Sons", "Lilith debuts (#28); Rise of the Midnight Sons; Vengeance (Badilino) debuts (#21); Spirits of Vengeance launches.", True)
    tick("1993", "Siege of Darkness", "Lilith and Zarathos assault the Midnight Sons across seventeen chapters.")
    tick("1994", "Ghost Rider 2099 · Blaze", "Zero Cochrane's cyberpunk Rider and Johnny's solo Blaze series both launch.")
    tick("1996", "Noble Kale", "Danny's Spirit is revealed as his ancestor; Blaze and Ketch are revealed as brothers.")
    tick("1998", "The Ketch series ends", "Ghost Rider vol. 3 #93 is the last published issue; #94 waits until 2007.")
    tick("2001", "The Hammer Lane", "Marvel Knights miniseries by Grayson and Kaniuga.")
    tick("2005", "Road to Damnation", "Ennis and Crain put Johnny on the endless highway of Hell.", True)
    tick("2006", "Lucifer", "Daniel Way's ongoing: Johnny escapes Hell with Lucifer's soul in 666 pieces.")
    tick("2007", "The film · Trail of Tears", "Ghost Rider (Mark Steven Johnson) opens in February with Nicolas Cage; Ennis's Civil War Rider debuts; Ghost Rider Finale publishes the lost #94.", True)
    tick("2008", "Zadkiel", "Jason Aaron's run begins at #20: the Spirits are Heaven's creations and the archangel is a traitor.", True)
    tick("2009", "Heaven's on Fire", "Blaze and Ketch lead the Riders against Zadkiel. The 2006 series ends at #35.")
    tick("2011", "Alejandra Jones", "The angel Adam gives Johnny's Spirit to a new host (Ghost Rider vol. 7).")
    tick("2012", "Spirit of Vengeance", "The second film (Neveldine/Taylor) opens in February; Cage's last ride.")
    tick("2014", "Robbie Reyes", "All-New Ghost Rider #1 (March): the Hell Charger arrives.", True)
    tick("2015", "Ghost Racers", "Secret Wars puts every Rider in Arcade's arena.")
    tick("2016", "Agents of S.H.I.E.L.D. · Kushala", "Gabriel Luna's Robbie Reyes joins the MCU on television; Kushala debuts in Doctor Strange and the Sorcerers Supreme.")
    tick("2017", "Cosmic Ghost Rider · the First Rider", "Thanos #13 introduces Frank Castle's cosmic Rider; Marvel Legacy #1 introduces the mammoth-riding Ghost Rider of 1,000,000 BC.", True)
    tick("2018", "Damnation · Avengers", "Johnny Blaze takes the throne of Hell; Robbie Reyes joins Aaron's Avengers.", True)
    tick("2019", "King of Hell", "Ed Brisson's Ghost Rider: Danny versus King Johnny.")
    tick("2021", "Robbie in Hell", "Robbie briefly claims the throne to expel Eli; Ghost Rider: Kushala Infinite Comic.")
    tick("2022", "Percy · Midnight Suns", "Benjamin Percy's Ghost Rider (April); Marvel's Midnight Suns video game with Robbie as playable Rider (December).")
    tick("2023", "Weapons of Vengeance", "Ghost Rider/Wolverine crossover introduces Bagra-ghul; Danny Ketch: Ghost Rider miniseries.")
    tick("2024", "Final Vengeance", "Frank Castle takes the Spirit; Spirits of Vengeance begins; Robbie Reyes Special.")
    tick("2025", "Spirits of Violence", "Ghost Rider vs. Galactus one-shot (June); Spirits of Violence #1 (October) opens the Violent Era.")
    tick("2026", "Ryan Gosling", "San Diego Comic-Con, July: Marvel Studios announces Ghost Rider with Ryan Gosling, directed by Shawn Levy; dated July 28, 2028 in August.", True)
    tick("2028", "The Marvel Studios film", "Scheduled for July 28, 2028.", True)

    body += '<section class="band"><div class="rail">' + "".join(T) + "</div></section>"
    body += related(["comic-history", "storylines", "news", "movies", "origins"])
    return dict(slug=s, title="Timeline", desc="A complete Ghost Rider timeline from 1967 to 2028: every host's debut, the Midnight Sons era, the films, Damnation, the Violent Era and the Marvel Studios movie.", keywords="Ghost Rider timeline, history, dates, 1972, 1990, 2014, 2028", body=body, vid_pos="65% 50%")
