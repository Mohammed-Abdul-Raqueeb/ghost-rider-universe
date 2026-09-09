from ._h import *
from build import crumbs, related

def page():
    s = "powers"
    body = hero("POWERS &<br>ABILITIES", "What the Spirit gives, what it takes, and where the fire stops. Read as a spec sheet: every power below is drawn from how the comics actually use it, not from a top-ten list.", crumbs(s), kicker="Spec sheet")

    def row(name, v, label, text):
        return f'<div class="row"><div><h3>{name}</h3><div class="gauge"><i style="--v:{v}%"></i></div><span class="gauge-label">{label}</span></div><p>{text}</p></div>'

    body += band('<div class="plate wide" style="max-width:52rem"><h2>Core powers</h2><div class="spec">' +
        row("Hellfire", 92, "Offense · all hosts",
            "Mystical flame that burns the soul rather than the flesh. A Rider can project it as bolts, coat weapons and vehicles in it, or unleash it as a wide area blast. It can be directed to harm only the guilty, and it does not consume the host. Robbie Reyes's flame runs blue-white; Cosmic Ghost Rider's is laced with the Power Cosmic.") +
        row("Penance Stare", 100, "Signature · Ketch onward",
            "Eye contact plus an intent to judge. The target relives every pain they have inflicted on others, all at once. It leaves the guilty catatonic or broken and does nothing to the innocent. Introduced with Danny Ketch in 1990 and later adopted by Johnny Blaze. Known failures: beings without souls (Centurious), those who feel no remorse or have already accepted their guilt, and, famously, the Punisher, who was unmoved.") +
        row("Superhuman strength", 78, "Physical · scales with the Spirit",
            "Riders routinely lift tens of tons, wrestle demons and shrug off gunfire. Strength rises when the Spirit takes more control, which is exactly when the host wants it least.") +
        row("Invulnerability & regeneration", 85, "Defence",
            "A Ghost Rider is a skeleton wrapped in fire; conventional weapons pass through or are shrugged off, and damage to the bones regenerates rapidly. Weapons forged in Heaven or Hell, and the hellfire of another Rider, can still hurt them.") +
        row("The chain", 88, "Weapon · Ketch, Reyes, later Blaze",
            "A length of chain that answers the Rider's will: it lengthens, ignites, whips, binds and can shatter into shrapnel then reform. Ketch wore it around his torso; Reyes pulled it from the Charger; Blaze's is often summoned from nowhere.") +
        row("Hell Cycle / Hell Charger", 90, "Mobility",
            "The vehicle is part of the power set. Ketch's Hell Cycle appeared on its own and rode up walls; Blaze's bike could cross water and ride on hellfire; Reyes can teleport through the Charger and see through it from any distance.") +
        row("Soul sense", 70, "Detection",
            "Riders can sense evil intent and innocent blood on a person, sometimes at a distance, and can track the guilty across a city. It is the reason the Spirit appears where and when it does.") +
        row("Interdimensional travel", 60, "Utility · situational",
            "Riding hellfire, a Rider can open portals to Hell or travel between realms. Johnny Blaze used this extensively as King of Hell; Cosmic Ghost Rider does it at will across time.") +
        '</div></div>')

    body += drift("It doesn't burn you. It burns what you did.", "On the Penance Stare")

    body += shout("THE LIMITS", "What stops a Ghost Rider",
        plate(p("<strong>Control.</strong> The single hardest problem. Zarathos wanted freedom, Noble Kale wanted rest, Eli Morrow wanted murder. Every host spends part of their story losing.",
                "<strong>Innocents.</strong> Hellfire aimed at the innocent will usually refuse. The Penance Stare does nothing to a clean soul, which makes it useless against many of the Rider's most powerful enemies — Mephisto, for one, enjoys it.",
                "<strong>Holy and infernal weapons.</strong> Enchanted blades, Heaven-forged guns and other Riders' hellfire all cut through the flame. Blackheart, Lilith and Zadkiel have each beaten a Rider in a straight fight.",
                "<strong>The host's own body.</strong> When the Spirit withdraws, the human is left with the consequences — exhaustion, injuries in the transition, and in Johnny Blaze's case decades of trauma from what Zarathos did with his hands.",
                "<strong>Separation.</strong> A Spirit can be forcibly removed. Zarathos was trapped by Centurious's Crystal of Souls; the angel Adam pulled Blaze's Spirit out and gave it to Alejandra Jones; Zadkiel drained Riders wholesale. The power is never entirely the host's.")))

    body += shout("POWER BY<br>HOST", "Same curse, different tuning",
        plate('<table class="tbl"><thead><tr><th>Host</th><th>Distinct traits</th></tr></thead><tbody>'
              '<tr><td>Johnny Blaze</td><td>Originally hellfire and a bike only; gained the Penance Stare and chain in the 1990s; hellfire shotgun; as King of Hell, command over the damned</td></tr>'
              '<tr><td>Danny Ketch</td><td>Penance Stare at full strength, self-summoning Hell Cycle, chain mastery; later able to absorb and redistribute the power of other Spirits</td></tr>'
              '<tr><td>Robbie Reyes</td><td>Blue-white flame, vehicle teleportation, possession-resistant will; his power grew enormously when a real Spirit of Vengeance replaced Eli</td></tr>'
              '<tr><td>Alejandra Jones</td><td>Angelic-tinged hellfire, flight, reality-scale power while under Adam\'s influence; later reduced</td></tr>'
              '<tr><td>Kushala</td><td>Full sorcery plus hellfire; can bind and command spirits; Sorcerer Supreme of the 19th century</td></tr>'
              '<tr><td>Cosmic Ghost Rider</td><td>Everything above, plus the Power Cosmic: energy manipulation, time travel, survival in space</td></tr>'
              '</tbody></table>', "right"), flip=True)

    body += related(["spirit-of-vengeance", "weapons", "vehicles", "transformations", "villains"])
    return dict(slug=s, title="Powers & Abilities", desc="Ghost Rider's powers explained: hellfire, the Penance Stare, the mystic chain, the Hell Cycle, strength, regeneration — and the limits that bind every host.", keywords="Penance Stare, hellfire, Ghost Rider powers, weaknesses, chain", body=body, vid_pos="65% 50%")
