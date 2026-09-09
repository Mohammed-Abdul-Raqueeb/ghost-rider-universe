from ._h import *
from build import crumbs, related

def page():
    s = "characters"
    body = hero("CHARACTERS", "The people who stand near the fire: family, partners, mentors and the handful who survive knowing a Ghost Rider.", crumbs(s), kicker="Supporting cast")

    E = []
    def entry(n, name, tag, text):
        E.append(f'<div class="entry reveal"><div class="no">{n}</div><div><h3>{name}</h3><span class="tag">{tag}</span>{plate(p(text))}</div></div>')

    entry("01", "Roxanne Simpson", "Johnny Blaze's wife · Crash Simpson's daughter",
          "The stunt rider's daughter whose love shielded Johnny's soul from Mephisto in 1972. She married Johnny after Zarathos was removed, had two children with him, and was murdered in the 1990s — the loss that pushed Johnny into his darkest years. Eva Mendes played her in the 2007 film.")
    entry("02", "Crash & Mona Simpson", "Adoptive parents",
          "Carnival stunt riders who took Johnny in after his father's death. Crash's cancer prompted the deal with Mephisto; his death during a jump — cancer-free — was the devil's fine print.")
    entry("03", "Barton & Naomi Blaze", "Birth parents",
          "Barton was a stunt rider killed in a crash. Naomi, born a Kale, left the family to spare her children the family curse; the attempt failed, and both of her sons became Ghost Riders.")
    entry("04", "Barbara Ketch", "Danny's sister",
          "Wounded in the cemetery fight that created the Ketch Ghost Rider, then murdered in hospital by Blackout. Her death drove Danny's early stories; in Spirits of Violence (2025–26) she returns as the Spirit of Violence.")
    entry("05", "Jack D'Auria", "Danny's best friend",
          "One of the few people who knew Danny's secret from the start. Jack served as confidant and comic relief through the 1990 series and was later possessed and abused by its villains.")
    entry("06", "Stacy Dolan", "NYPD detective",
          "A police officer who first hunted the Ghost Rider as a murder suspect before learning the truth and becoming Danny's ally and, for a time, love interest.")
    entry("07", "The Caretaker", "Keeper of the Spirits' history",
          "A mysterious old man of the Blood, an order guarding the secrets of the Spirits of Vengeance, who lived in Cypress Hills Cemetery and guided Danny. His granddaughter Sara — a nun with a hellfire shotgun — inherited the role in Jason Aaron's run.")
    entry("08", "Gabe Reyes", "Robbie's brother",
          "The reason Robbie took the deal. Gabe uses a wheelchair, adores his brother, and when Eli grew tired of Robbie's resistance he reached for Gabe as an alternative host — making the boy both a target and a mirror for Robbie's fears.")
    entry("09", "Eli Morrow", "Robbie's uncle · the false Spirit",
          "A satanic serial killer, dead before the story begins, who rides Robbie's body. He is a supporting character only in the sense that he never leaves; see <a href='spirit-of-vengeance.html'>The Spirit of Vengeance</a>.")
    entry("10", "Talia Warroad", "FBI agent",
          "Introduced in Benjamin Percy's 2022 series, Warroad hunts the supernatural for the Bureau and pursues Johnny Blaze across the American West, becoming a reluctant partner.")
    entry("11", "Michael Badilino", "Vengeance",
          "The NYPD lieutenant turned Rider. Enemy, then ally, then Midnight Son. See <a href='other-riders.html'>Other Ghost Riders</a>.")
    entry("12", "The Midnight Sons", "Marvel's supernatural line",
          "The 1992–94 alliance of Ghost Rider, Blaze, Morbius, the Nightstalkers (Blade, Hannibal King, Frank Drake) and the Darkhold Redeemers, formed to fight Lilith. The name was revived in 2024's Midnight Sons: Blood Hunt.")
    entry("13", "Doctor Strange", "Ally in extremity",
          "Ghost Riders and the Sorcerer Supreme cross paths whenever Hell becomes everyone's problem: Siege of Darkness, Damnation, and the 2016 series in which Kushala served on Strange's team of Sorcerers Supreme.")
    entry("14", "The Punisher", "The man who felt nothing",
          "Frank Castle's immunity to the Penance Stare — he had already accepted everything he had done — is one of the character's most famous beats. Cosmic Ghost Rider made him a Rider outright; Final Vengeance (2024) briefly handed him Johnny's Spirit.")

    body += '<section class="band"><div class="ledger">' + "".join(E) + "</div></section>"
    body += related(["relationships", "villains", "johnny-blaze", "danny-ketch", "robbie-reyes"])
    return dict(slug=s, title="Characters", desc="The Ghost Rider supporting cast: Roxanne Simpson, the Simpsons, Barbara Ketch, Jack D'Auria, Stacy Dolan, the Caretaker, Gabe Reyes, Talia Warroad, the Midnight Sons and more.", keywords="Roxanne Simpson, Caretaker, Sara, Gabe Reyes, Stacy Dolan, Jack D'Auria, Midnight Sons", body=body, vid_pos="50% 50%")
