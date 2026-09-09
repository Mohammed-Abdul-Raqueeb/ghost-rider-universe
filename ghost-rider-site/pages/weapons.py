from ._h import *
from build import crumbs, related

def page():
    s = "weapons"
    body = hero("WEAPONS &<br>ARTIFACTS", "The ordnance of vengeance: a chain that thinks, a shotgun that fires damnation, a medallion that carries a bloodline and the book that made Lilith's children.", crumbs(s), kicker="The armory", align="right")

    A = []
    G = {
      "chain": '<svg viewBox="0 0 24 24"><rect x="3" y="9" width="7" height="6" rx="3"/><rect x="14" y="9" width="7" height="6" rx="3"/><path d="M10 12h4"/></svg>',
      "fire": '<svg viewBox="0 0 24 24"><path d="M12 3c1 4 5 5 5 10a5 5 0 0 1-10 0c0-3 2-4 2-6 1 2 3 3 3 5"/></svg>',
      "eye": '<svg viewBox="0 0 24 24"><path d="M2 12s4-6 10-6 10 6 10 6-4 6-10 6S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
      "gun": '<svg viewBox="0 0 24 24"><path d="M3 9h16l2 2v2H9l-1 5H5l1-5H3z"/></svg>',
      "coin": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"/><path d="M12 7v10M9 10l3-3 3 3"/></svg>',
      "book": '<svg viewBox="0 0 24 24"><path d="M4 4h9a3 3 0 0 1 3 3v13H7a3 3 0 0 0-3 3z"/><path d="M20 4h-4v13h4z"/></svg>',
      "gem": '<svg viewBox="0 0 24 24"><path d="M7 4h10l4 5-9 11L3 9z"/><path d="M3 9h18M12 20 7 4M12 20l5-16"/></svg>',
      "car": '<svg viewBox="0 0 24 24"><path d="M3 14l2-6h14l2 6v4H3z"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/></svg>',
    }
    def item(g, name, tag, text):
        A.append(f'<div class="item reveal"><div class="glyph">{G[g]}</div><div class="plate"><h3>{name}</h3><span class="owner" style="font-family:var(--cond);letter-spacing:.14em;color:var(--hellfire-2);font-size:.85rem;display:block;margin-bottom:.6rem">{tag}</span>{p(text)}</div></div>')

    item("fire", "Hellfire", "All Riders",
         "The base weapon. A mystical flame that burns the soul, obeys the Rider's will and never harms its host. It can be thrown, projected in walls, poured into a vehicle or a weapon, or — in Cosmic Ghost Rider's case — mixed with the Power Cosmic.")
    item("chain", "The Mystic Chain", "Ketch, Reyes, Blaze",
         "Danny Ketch wore it wrapped around his torso; it could lengthen, ignite, split into blades and reassemble. Robbie Reyes pulls his from the Charger. The chain became the Rider's melee signature in the 1990s and has been part of every design since.")
    item("eye", "The Penance Stare", "Ketch onward",
         "Not an object, but the Rider's most feared weapon. Eye contact and a guilty conscience are all it needs. See <a href='powers.html'>Powers</a> for its rules and failures.")
    item("gun", "The Hellfire Shotgun", "Johnny Blaze; Sara",
         "A sawed-off shotgun that fires hellfire, first carried by Johnny while hunting the new Ghost Rider in 1990–92 during his powerless years. Sara, the Caretaker's granddaughter, carried a similar weapon in Jason Aaron's run. It is the reason a depowered Johnny Blaze is still dangerous.")
    item("coin", "The Medallion of Power", "The Kale bloodline",
         "A mystical artifact that once contained the Spirits of Vengeance; it was broken into shards embedded in the Kale family's souls. Fragments in Danny Ketch and Johnny Blaze explained how both brothers could carry a Spirit — a key plot device of the 1990s series.")
    item("gem", "The Crystal of Souls", "Centurious",
         "The prison Centurious used to trap Zarathos at the end of Ghost Rider vol. 2 (1983). It holds souls; the man without a soul could handle it safely.")
    item("book", "The Darkhold", "Lilith, the Darkhold Redeemers",
         "The Book of Sins, written by the Elder God Chthon. Its pages grant power at ruinous cost and created many of the Midnight Sons era's monsters. The Darkhold Redeemers spent their series hunting its stray pages.")
    item("car", "The Hell Charger", "Robbie Reyes",
         "Weapon as much as vehicle: the Charger rams, phases and teleports, and its trunk houses the chain. See <a href='vehicles.html'>Vehicles</a>.")
    item("fire", "The Contract of San Venganza", "2007 film",
         "The film's MacGuffin: a contract for a thousand corrupt souls, hidden by Carter Slade's Rider and hunted by Blackheart. Not from the comics, but now part of the wider mythology.")
    item("gem", "The Spirit Cage", "Zadkiel's war",
         "The devices used by Zadkiel's agents to strip and store the power of Ghost Riders, which Danny Ketch wielded as a Rider-hunter before turning on his master in Heaven's on Fire (2009).")

    body += '<section class="band"><div class="armory">' + "".join(A) + "</div></section>"
    body += related(["powers", "vehicles", "villains", "hell", "storylines"])
    return dict(slug=s, title="Weapons & Artifacts", desc="Ghost Rider's weapons and artifacts: hellfire, the mystic chain, the Penance Stare, the hellfire shotgun, the Medallion of Power, the Crystal of Souls, the Darkhold and the Contract of San Venganza.", keywords="hellfire chain, hellfire shotgun, Medallion of Power, Crystal of Souls, Darkhold, Contract of San Venganza", body=body, vid_pos="55% 50%")
