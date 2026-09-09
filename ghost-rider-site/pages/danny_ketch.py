from ._h import *
from build import crumbs, related

def page():
    s = "danny-ketch"
    body = hero("DANNY<br>KETCH", "The Rider who made the 1990s. A Brooklyn teenager whose Ghost Rider was silent, spectral and merciless — and who turned out to carry the family curse of the Kales.", crumbs(s), kicker="Host · 1990 — present", align="right")

    body += band(plate('<h2>Profile</h2>' + facts([
        ("Real name", "Daniel \"Danny\" Ketch"),
        ("First appearance", "Ghost Rider vol. 3 #1 (May 1990)"),
        ("Created by", "Howard Mackie, Javier Saltares"),
        ("Spirit", "Noble Kale (assumed to be Zarathos until 1996)"),
        ("Base", "Cypress Hills, Brooklyn, New York"),
        ("Family", "Francis Ketch (adoptive mother); Barbara Ketch (sister, deceased, later resurrected as the Spirit of Violence); Johnny Blaze (brother); Naomi Kale (birth mother)"),
        ("Allies", "Jack D'Auria, Stacy Dolan, the Caretaker, Michael Badilino/Vengeance, the Midnight Sons"),
        ("Signatures", "Penance Stare, mystic chain, self-manifesting Hell Cycle"),
    ]), "wide right"))

    body += shout("THE CEMETERY", "Halloween, 1990",
        plate(p("Danny and his sister Barbara went to Cypress Hills Cemetery to test a rumour about ghosts and instead walked into a fight between the crime lord Deathwatch's ninjas and rival gunmen over stolen bio-toxin canisters. Barbara was struck by an arrow. Fleeing with her through a junkyard, Danny found a motorcycle with a glowing gas cap; when he touched it, he became a new Ghost Rider and tore through Deathwatch's men.",
                "The Rider that emerged could not speak at first, wore a spiked jacket wrapped in chain, and possessed a power no previous version had: the Penance Stare. Barbara survived the arrow only to be murdered in her hospital bed by the vampiric assassin Blackout — the wound that defined Danny's early years.")))

    body += shout("THE BESTSELLER", "1990–1998",
        plate(p("Mackie and Saltares — followed by artists including Mark Texeira, Ron Garney and Salvador Larroca — turned <em>Ghost Rider</em> vol. 3 into one of Marvel's biggest books. The series' rogues' gallery was built almost from scratch: Deathwatch, Blackout, Snowblind, the Scarecrow reimagined as a serial killer, and, from <em>Ghost Rider</em> #28 (1992), Lilith, mother of demons, whose \"Lilin\" spawned the <em>Rise of the Midnight Sons</em> crossover.",
                "Danny's Ghost Rider anchored the Midnight Sons line — with Blaze, Morbius, the Nightstalkers and the Darkhold Redeemers — through <em>Midnight Massacre</em> and <em>Siege of Darkness</em>. He fought alongside the X-Men, Spider-Man, Wolverine and the Punisher, and the Rider's stare on the Punisher, who felt nothing, became one of the era's most quoted moments."), "right"), flip=True)

    body += drift("He was told the fire was a demon. It was family.", "On the Noble Kale revelation, 1996")

    body += shout("THE REVEAL", "Noble Kale and the bloodline",
        plate(p("Writer Ivan Velez Jr. revealed that Danny's Spirit was Noble Kale, an ancestor transformed into a Spirit of Vengeance by Mephisto's manipulation of the Kale family in the 1700s. Danny and Johnny Blaze were brothers through their mother Naomi, who had tried to break the curse and failed. The series ended in 1998 with Noble Kale ascending as an archangel and Danny apparently free.",
                "The book's true final issue, #94, went unpublished until 2007, when Marvel released it alongside a new Danny Ketch miniseries.")))

    body += shout("THE RETURN", "2007 — present",
        plate(p("Danny came back in Jason Aaron's run as a broken, addicted man harvesting other Riders' power for the archangel Zadkiel, before turning on his master. The 2008 <em>Ghost Rider: Danny Ketch</em> miniseries (Simon Spurrier, Javier Saltares) explored his addiction to the Spirit. He co-starred in the 2019–20 series, where he had to pull Johnny back from the throne of Hell, and in <em>Danny Ketch: Ghost Rider</em> (2023) and <em>Spirits of Vengeance</em> (2024–25).",
                "In <em>Spirits of Violence</em> (2025–26), his murdered sister Barbara returned as the Spirit of Violence — turning the loss that made him a Rider into the threat that could unmake him."), "right"), flip=True)

    body += related(["johnny-blaze", "villains", "storylines", "vehicles", "characters"])
    return dict(slug=s, title="Danny Ketch", desc="Danny Ketch, the 1990 Ghost Rider: the cemetery origin, the Penance Stare, the Midnight Sons era, the Noble Kale revelation and his modern return.", keywords="Danny Ketch, Noble Kale, Barbara Ketch, Blackout, Deathwatch, Midnight Sons, Cypress Hills", body=body, vid_pos="40% 50%")
