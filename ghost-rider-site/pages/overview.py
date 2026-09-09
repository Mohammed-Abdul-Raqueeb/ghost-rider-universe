from ._h import *
from build import crumbs, related

def page():
    s = "overview"
    body = hero("WHAT IS<br>GHOST RIDER?", "A title, a curse and a job description. The Ghost Rider is what a human being becomes when a Spirit of Vengeance rides inside them — and the name has passed between hosts, eras and even genres since 1967.", crumbs(s), kicker="Overview")

    body += shout("A CURSE<br>WITH A NAME", "The short version",
        plate(p("<span class=\"lead\">A Ghost Rider is a human bonded to a demonic or celestial Spirit of Vengeance.</span>",
                "The bond gives the host a body of living flame around bare bone, control of hellfire, superhuman strength and endurance, and the Penance Stare — a gaze that forces a guilty soul to relive every pain it has caused. The price is loss of control: the Spirit wants to punish, and it does not always care who is in front of it.",
                "The term first belonged to a Western hero, Carter Slade, a Texas schoolteacher who fought outlaws on a white horse in a phosphorescent costume (1967). When Marvel reused the name in 1972 for stunt rider Johnny Blaze, Slade's character was retitled Night Rider and then Phantom Rider. Since then the flaming skull has been the definition.")))

    body += band(f'''<div class="plate wide center">
      <h2>The hosts at a glance</h2>
      <table class="tbl"><thead><tr><th>Host</th><th>Debut</th><th>Creators</th><th>Spirit / power source</th><th>Signature</th></tr></thead><tbody>
      <tr><td><a href="johnny-blaze.html">Johnny Blaze</a></td><td>Marvel Spotlight #5 (Aug 1972)</td><td>Roy Thomas, Gary Friedrich, Mike Ploog</td><td>Zarathos (bonded through Mephisto's deal)</td><td>Hellfire motorcycle, later hellfire shotgun</td></tr>
      <tr><td><a href="danny-ketch.html">Danny Ketch</a></td><td>Ghost Rider vol. 3 #1 (May 1990)</td><td>Howard Mackie, Javier Saltares</td><td>Noble Kale, an ancestral Spirit of Vengeance</td><td>Mystic chain, Penance Stare, self-manifesting Hell Cycle</td></tr>
      <tr><td><a href="robbie-reyes.html">Robbie Reyes</a></td><td>All-New Ghost Rider #1 (Mar 2014)</td><td>Felipe Smith, Tradd Moore</td><td>Ghost of Eli Morrow, later a true Spirit of Vengeance</td><td>The Hell Charger, blue-white flame, hellfire chain</td></tr>
      <tr><td><a href="other-riders.html">Alejandra Jones</a></td><td>Ghost Rider vol. 7 #1 (Jul 2011)</td><td>Rob Williams, Matthew Clark</td><td>The Spirit of Vengeance taken from Blaze by Adam</td><td>Angelic hellfire, flight</td></tr>
      <tr><td><a href="other-riders.html">Kushala</a></td><td>Doctor Strange and the Sorcerers Supreme #1 (2016)</td><td>Robbie Thompson, Javier Rodríguez</td><td>A Spirit of Vengeance bound in the 1800s</td><td>Sorcery plus hellfire; Sorcerer Supreme of her era</td></tr>
      <tr><td><a href="multiverse.html">Cosmic Ghost Rider</a></td><td>Thanos #13 (Nov 2017)</td><td>Donny Cates, Geoff Shaw</td><td>Frank Castle's Spirit of Vengeance plus the Power Cosmic</td><td>Cosmic hellfire, chains, Galactus-scale power</td></tr>
      </tbody></table></div>''')

    body += drift("The skull is not a mask. It is what is left when the Spirit burns the lie away.", right=True)

    body += shout("WHY IT<br>ENDURES", "Fifty-four years of hellfire",
        plate(p("Ghost Rider arrived in 1972, when the Comics Code Authority had just loosened its rules on vampires, werewolves and the occult. Marvel answered with a wave of horror leads — Werewolf by Night, Tomb of Dracula, Morbius, Man-Thing — and a stunt cyclist with a burning skull turned out to be the one with the most staying power.",
                "The concept refreshes itself because the title is transferable. When a host's story runs dry, a new one can inherit the curse: Danny Ketch in 1990 turned the character into a chain-swinging urban vigilante at the height of the grim-and-gritty era; Robbie Reyes in 2014 moved the fire from a motorcycle to a muscle car and from Texas highways to East Los Angeles. Each one carries the same core bargain — vengeance in exchange for your control — into a different decade.",
                "The character has also been adapted twice on film (2007, 2012), on television in Agents of S.H.I.E.L.D. (2016–17), in Marvel's Midnight Suns (2022), and is now slated for a Marvel Studios feature starring Ryan Gosling in 2028."), "right"), flip=True)

    body += related(["origins", "powers", "spirit-of-vengeance", "johnny-blaze", "comic-history", "movies"])
    return dict(slug=s, title="Ghost Rider Overview", desc="What Ghost Rider is: the Spirit of Vengeance, its hosts from Johnny Blaze to Robbie Reyes, its powers, and why the character has endured since 1972.", keywords="Ghost Rider explained, what is Ghost Rider, hosts, Carter Slade", body=body, vid_pos="60% 50%")
