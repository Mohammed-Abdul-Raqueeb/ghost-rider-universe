from ._h import *
from build import crumbs, related

def page():
    s = "hell"
    body = hero("HELL &<br>THE SUPERNATURAL<br>REALM", "Where the contracts are filed. Marvel's Hell is not one place but a federation of infernal realms, each with a lord, a legal system and a grudge against the Spirits of Vengeance.", crumbs(s), kicker="Descend", wide=True)

    L = []
    def layer(title, text, cls=""):
        L.append(f'<div class="layer reveal"><h3>{title}</h3>{plate(p(text), cls)}</div>')

    layer("The Splinter Realms", "In Marvel cosmology there is no single Hell. Mephisto's realm, Satannish's domain, Hela's Hel, Dormammu's Dark Dimension and others are separate \"Hells\" whose lords compete for souls and periodically go to war. The rules are consistent: a soul freely given cannot be taken back; a contract signed under duress still binds; love, sacrifice and faith can void a claim.")
    layer("Mephisto's Realm", "The Hell that made the Rider. A landscape of fire, ice and bureaucracy where the damned are tormented and demons trade in souls. Mephisto is not Satan — Marvel has been careful about that since the 1970s — but he plays the part, and Ghost Rider stories from 1972 onward treat his domain as the default afterlife for the guilty.")
    layer("The Road to Damnation", "Garth Ennis's 2005 miniseries imagined Hell as an endless highway on which Johnny Blaze rides forever, chased by demons and offered a way out by an angel with his own war to fight. It is the version of Hell most readers picture when they think of the character.")
    layer("Hotel Inferno, Las Vegas", "In Damnation (2018), Mephisto raised a casino in the ruins of Las Vegas and turned the city's dead into its guests. Doctor Strange, Wong, Blade, the Midnight Sons and Johnny Blaze fought their way through the tables; Blaze ended the story on the throne.")
    layer("The Throne of Hell", "From 2018 to 2020 Johnny Blaze ruled Mephisto's realm, using the damned as an army and slowly becoming what he had fought. Ed Brisson's Ghost Rider (2019–20) is the story of that reign and of Danny Ketch dragging him off the throne. Robbie Reyes later held the same seat briefly to evict Eli Morrow.")
    layer("Heaven's Side of the Ledger", "Jason Aaron's run established that the Spirits were Heaven's creation, that the archangel Zadkiel had corrupted their purpose, and that Heaven could be invaded. It also introduced the Blood and their Caretaker as the mortal order that keeps the records. The Riders exist because both sides of the afterlife keep filing claims on the same souls.")
    layer("The Darkhold and the Lilin", "Lilith's children, the Lilin, and the Darkhold — the Book of Sins written by the Elder God Chthon — are the supernatural machinery of the 1992–94 Midnight Sons era. Lilith wanted Earth as a nursery; the Darkhold turned ordinary people into monsters. Both remain live threats in modern Marvel.")

    body += '<section class="band"><div class="strata">' + "".join(L) + "</div></section>"
    body += drift("Hell keeps every receipt. The Rider is what happens when one comes due.", "On the logic of the curse")
    body += related(["villains", "spirit-of-vengeance", "lore", "storylines", "johnny-blaze"])
    return dict(slug=s, title="Hell & the Supernatural Realm", desc="Marvel's Hell in Ghost Rider: Mephisto's realm, the Splinter Realms, the Road to Damnation, Hotel Inferno, the throne of Hell, Heaven's role, the Darkhold and the Lilin.", keywords="Marvel Hell, Mephisto realm, Damnation, Hotel Inferno, Darkhold, Lilin, King of Hell", body=body, vid_pos="50% 60%")
