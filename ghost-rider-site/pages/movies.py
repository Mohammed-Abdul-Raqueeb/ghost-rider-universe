from ._h import *
from build import crumbs, related

def page():
    s = "movies"
    body = hero("MOVIES", "Two Sony pictures with Nicolas Cage, a television Rider, and the Marvel Studios film that finally brings the skull into the MCU.", crumbs(s), kicker="On screen", align="right")

    def slate(year, title, dir_, inner):
        return f'<article class="slate reveal"><div class="marquee"><div class="year">{year}</div><h2>{title}</h2><p class="dir">{dir_}</p></div>{plate(inner)}</article>'

    body += '<section class="band"><div class="slates">'
    body += slate("2007", "GHOST RIDER", "Directed by Mark Steven Johnson · Columbia Pictures / Sony",
        p("Nicolas Cage as Johnny Blaze, Eva Mendes as Roxanne Simpson, Wes Bentley as Blackheart, Peter Fonda as Mephistopheles and Sam Elliott as the Caretaker — a retired Rider revealed to be Carter Slade. The plot adapts the 1972 origin and adds the Contract of San Venganza, a deed for a thousand souls that Blackheart wants and Slade hid.",
          "Shot largely in Melbourne, Australia, it opened in February 2007 to poor reviews and strong business, roughly $228 million worldwide on a reported $110 million budget. Cage, a long-time fan with a Ghost Rider tattoo he had to cover for the role, played the Rider as a Southern gentleman with a jellybean habit.") +
        facts([("Rider design", "Practical leathers, CG skull and flame; the bike transforms into a stretched, skeletal chopper"), ("Villains", "Blackheart and the Hidden — Abigor, Wallow, Gressil"), ("Rating", "PG-13"), ("Extended cut", "A longer cut was released on home video")]))
    body += slate("2012", "GHOST RIDER:<br>SPIRIT OF VENGEANCE", "Directed by Mark Neveldine & Brian Taylor · Columbia / Hyde Park",
        p("A soft reboot rather than a sequel. Cage returns as a Blaze hiding in Eastern Europe, recruited by the wine-drinking warrior monk Moreau (Idris Elba) to protect a boy, Danny, from Roarke (Ciarán Hinds) — the devil in human form — who wants the child as a vessel. Johnny Whitworth plays Ray Carrigan, transformed into a version of Blackout.",
          "Shot in Romania and Turkey with the Crank directors' handheld, frenetic style, the film reworked the Rider as a charred, tar-black skull and had Cage perform the Rider himself rather than through a double. It grossed around $132 million worldwide and was rated PG-13 despite a harder tone.") +
        facts([("Rider design", "Blackened skull, smoke and charcoal texture, flame that flares with rage"), ("Vehicle", "Yamaha VMAX-based bike; the Rider also hijacks a giant Bagger 288 excavator"), ("Legacy", "Cage's final Ghost Rider; rights reverted to Marvel in 2013")]))
    body += slate("2016", "AGENTS OF<br>S.H.I.E.L.D.", "Season 4 · ABC / Marvel Television",
        p("Gabriel Luna played Robbie Reyes in the fourth season's opening arc, complete with the Hell Charger, the burning-jacket transformation and the Darkhold. It was the first live-action Ghost Rider produced by Marvel and the first time Reyes appeared outside comics. A planned Hulu spin-off with Luna was cancelled in 2019.") +
        facts([("Rider", "Robbie Reyes"), ("Uncle Eli", "José Zúñiga"), ("Status", "Continuity with the MCU is officially unclear")]))
    body += slate("2028", "GHOST RIDER", "Directed by Shawn Levy · Marvel Studios · July 28, 2028",
        p("Announced at San Diego Comic-Con on July 25–26, 2026: Ryan Gosling will play Johnny Blaze in a standalone Marvel Studios film directed by Shawn Levy (Deadpool & Wolverine) from a screenplay by Jonathan Tropper. Gosling told the Hall H crowd he had wanted the role for a very long time; Levy said the idea grew out of their downtime on Star Wars: Starfighter. Disney set the release date of July 28, 2028 in August 2026, making it one of three Marvel films that year alongside the X-Men film and Black Panther 3.") +
        facts([("Star", "Ryan Gosling as Johnny Blaze"), ("Writer", "Jonathan Tropper"), ("Studio", "Marvel Studios / Disney"), ("Release", "July 28, 2028")]) +
        '<p class="fig"><a href="news.html">Follow the news ledger for updates</a></p>')
    body += '</div></section>'

    body += drift("The skull has been on screen since 2007. It has never been in the Marvel Cinematic Universe. That changes in 2028.")
    body += related(["news", "multiverse", "johnny-blaze", "robbie-reyes", "videos"])
    return dict(slug=s, title="Movies", desc="Ghost Rider on screen: the 2007 film with Nicolas Cage, Spirit of Vengeance (2012), Robbie Reyes in Agents of S.H.I.E.L.D. and the 2028 Marvel Studios film starring Ryan Gosling and directed by Shawn Levy.", keywords="Ghost Rider movie, Nicolas Cage, Spirit of Vengeance 2012, Ryan Gosling Ghost Rider, Shawn Levy, 2028", body=body, vid_pos="50% 50%")
