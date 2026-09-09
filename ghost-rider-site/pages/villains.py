from ._h import *
from build import crumbs, related

def page():
    s = "villains"
    body = hero("VILLAINS", "The ledger of the damned. Hell-lords who wrote the contracts, demons who want the Spirit for themselves, and mortals who learned too late what the Penance Stare feels like.", crumbs(s), kicker="Enemies", align="right")

    E = []
    def entry(n, name, tag, text):
        E.append(f'<div class="entry reveal"><div class="no">{n}</div><div><h3>{name}</h3><span class="tag">{tag}</span>{plate(p(text))}</div></div>')

    entry("01", "Mephisto", "Lord of Hell · the author of the curse",
          "Marvel's principal devil (first seen in Silver Surfer #3, 1968) and the demon who bought Johnny Blaze's soul and bound Zarathos to him. He also made Noble Kale, Vengeance and Cosmic Ghost Rider. In Damnation (2018) he turned Las Vegas into a casino annex of Hell and lost his throne to Blaze. Peter Fonda played his film counterpart Mephistopheles in 2007; Ciarán Hinds took the role in 2012.")
    entry("02", "Zarathos", "The demon inside",
          "Passenger, rival and occasionally villain. When separated from Johnny, Zarathos has tried to reclaim a body and rebuild his cult; his hunger is the reason early Ghost Rider stories read as horror. See <a href='spirit-of-vengeance.html'>The Spirit of Vengeance</a>.")
    entry("03", "Blackheart", "Son of Mephisto",
          "Born from centuries of accumulated evil in a Massachusetts town (Daredevil #270, 1989), Blackheart has repeatedly tried to overthrow his father and to corrupt the Riders, most notably in Ghost Rider/Wolverine/Punisher: Hearts of Darkness (1991). Wes Bentley played him in the 2007 film as the villain who covets the Contract of San Venganza.")
    entry("04", "Lilith", "Mother of Demons",
          "Introduced in Ghost Rider vol. 3 #28 (1992), the ancient mother of the Lilin escaped her prison inside a leviathan and led an army of her children against the Midnight Sons. Rise of the Midnight Sons and Midnight Massacre are her war.")
    entry("05", "Deathwatch", "Crime lord of Brooklyn",
          "A demon in the body of a New York businessman, Stephen Lords, who can kill by touch and feeds on the pain of the dying. His pursuit of stolen bio-toxin in Cypress Hills Cemetery created the Ketch Ghost Rider (Ghost Rider vol. 3 #1, 1990).")
    entry("06", "Blackout", "The albino vampire",
          "Deathwatch's enforcer and later a free agent: a pale, fanged killer with nightvision, light-sensitive skin and a taste for cruelty. He murdered Barbara Ketch in her hospital bed and skinned Danny's face in one of the series' most notorious issues. Johnny Whitworth played a version of him in Spirit of Vengeance (2012).")
    entry("07", "Scarecrow", "Ebenezer Laughton",
          "A contortionist supervillain created in 1964 as an Iron Man foe, reworked in the 1990 Ghost Rider series into a serial-killing horror figure who became one of Ketch's most disturbing enemies.")
    entry("08", "The Orb", "Drake Shannon",
          "A former stunt rider whose face was destroyed in a race against Crash Simpson; he wears a giant hypnotic eyeball helmet. The Orb debuted in Marvel Team-Up #15 (1973) as one of Johnny Blaze's first recurring enemies and has since become a fixture of Marvel's underworld.")
    entry("09", "Centurious", "The man without a soul",
          "A warrior who sold his soul to Zarathos long ago, Centurious (Ghost Rider vol. 2 #74, 1982) is immune to the demon's power because there is nothing in him to burn. His Crystal of Souls imprisoned Zarathos at the end of the original series.")
    entry("10", "Zadkiel", "The renegade archangel",
          "The villain of Jason Aaron's run (2008–09): an archangel who had spent centuries manipulating the Spirits of Vengeance and finally used Danny Ketch to seize Heaven itself. Blaze and Ketch cast him down with an army of Riders in Heaven's on Fire.")
    entry("11", "Lucifer", "The fragmented devil",
          "Daniel Way's 2006–07 arc freed Johnny from Hell only to release Lucifer alongside him, split into 666 pieces inhabiting corpses across America. Each piece Johnny destroyed made the rest stronger.")
    entry("12", "Eli Morrow", "The ghost in the Charger",
          "Robbie Reyes's uncle: satanist, serial killer, impostor Spirit. The villain who lives inside the hero. See <a href='robbie-reyes.html'>Robbie Reyes</a>.")
    entry("13", "Mr. Hyde", "Calvin Zabo",
          "The scientist-monster whose mercenaries killed Robbie Reyes in All-New Ghost Rider, hunting the experimental pills hidden in the Charger's trunk.")
    entry("14", "Blackheart's siblings & the Hell-lords", "Satannish, Hela, Dormammu",
          "Hell in Marvel is a federation. Satannish, Hela, Dormammu and others have all claimed pieces of it, bargained with Riders or bid for their Spirits — most visibly in Damnation and the 2019–20 King of Hell storyline.")
    entry("15", "Barbara Ketch", "The Spirit of Violence",
          "The newest name in the ledger: Danny's murdered sister, resurrected in Spirits of Violence (2025–26) as a spirit that turns Riders' own rage against them.")

    body += '<section class="band"><div class="ledger">' + "".join(E) + "</div></section>"
    body += related(["hell", "spirit-of-vengeance", "storylines", "danny-ketch", "characters"])
    return dict(slug=s, title="Villains", desc="Ghost Rider's villains: Mephisto, Zarathos, Blackheart, Lilith, Deathwatch, Blackout, Scarecrow, the Orb, Centurious, Zadkiel, Lucifer, Eli Morrow and more.", keywords="Mephisto, Blackheart, Lilith, Deathwatch, Blackout, Zadkiel, Centurious, the Orb, Scarecrow", body=body, vid_pos="50% 45%")
