from ._h import *
from build import crumbs, related

def page():
    s = "johnny-blaze"
    body = hero("JOHNNY<br>BLAZE", "The first Spirit of Vengeance of the modern age. A carnival stunt rider from Waukegan, Illinois, who made the deal that every later Rider is still paying for.", crumbs(s), kicker="Host · 1972 — present",
                cta='<a class="btn ghost" href="origins.html">The deal in detail</a>')

    body += band(plate('<h2>Profile</h2>' + facts([
        ("Real name", "Johnathon \"Johnny\" Blaze"),
        ("First appearance", "Marvel Spotlight #5 (August 1972)"),
        ("Created by", "Roy Thomas, Gary Friedrich, Mike Ploog"),
        ("Spirit", "Zarathos; briefly none (1983–90); later re-bonded"),
        ("Base", "Quentin Carnival; later nomadic across the American South-West"),
        ("Family", "Barton and Naomi Blaze (parents); Crash and Mona Simpson (adoptive); Roxanne Simpson (wife); Danny and Barbara Ketch (half-siblings); Craig and Emma (children)"),
        ("Signatures", "Hellfire motorcycle, hellfire shotgun, chain, Penance Stare (later)"),
        ("Portrayed by", "Nicolas Cage (2007, 2012); Ryan Gosling (2028, announced)"),
    ]), "wide"))

    body += shout("THE CARNIVAL YEARS", "1972–1983",
        plate(p("Johnny's mother Naomi left the family when he was small; his father Barton, a stunt rider, died in a crash. The Simpson family took the boy in and taught him the trade. When Crash Simpson revealed he was dying, Johnny turned to the occult books his mother had left behind and summoned Satan. The bargain cured the cancer; a jump killed Crash anyway, and only Roxanne's love kept Mephisto from taking Johnny's soul outright.",
                "Bound to Zarathos, Johnny spent the next decade as a reluctant nocturnal monster. The 1973–83 series took him from the carnival to Hollywood stunt work, to the Champions (a short-lived Los Angeles super-team with Hercules, Black Widow, Angel and Iceman), and finally into a war with Centurious that ended with Zarathos imprisoned in the Crystal of Souls and Johnny free.")))

    body += shout("THE QUIET YEARS", "1983–1990",
        plate(p("Freed of the curse, Johnny married Roxanne, had two children and ran the Quentin Carnival. When Danny Ketch's Ghost Rider appeared in 1990, Johnny assumed it was Zarathos returned, tracked the new Rider down and tried to kill him with a shotgun that fired hellfire — a weapon he had acquired while hunting the demon. The confrontation became a partnership; Johnny co-starred in <em>Ghost Rider/Blaze: Spirits of Vengeance</em> (1992–94) and led his own short-lived series, <em>Blaze</em> (1994–95).",
                "The 1990s revealed that Johnny and Danny were brothers — both sons of Naomi Kale — and that the Kale bloodline carried the Spirit of Vengeance. Roxanne's murder in this period and Johnny's descent into grief set the tone for the darker versions of the character that followed."), "right"), flip=True)

    body += drift("Every night he lost. Every morning he had to live with what won.")

    body += shout("THE DAMNED YEARS", "2005–2012",
        plate(p("Garth Ennis and Clayton Crain's <em>Ghost Rider: Road to Damnation</em> (2005–06) found Johnny literally in Hell, riding a road with no end, offered escape by an angel with an agenda. Daniel Way's 2006 relaunch had him escape to Earth pursued by Lucifer's fragmented soul; Jason Aaron's run (2008–09) sent him against the archangel Zadkiel, teamed him with Danny Ketch again and rebuilt the mythology of the Spirits.",
                "In 2011 the angel Adam removed Johnny's Spirit and gave it to Alejandra Jones. Johnny, powerless, became the story's conscience — and, when Alejandra's power was misused, took it back."), "right"))

    body += shout("KING OF HELL", "2018 — present",
        plate(p("In <em>Damnation</em> (2018), Mephisto's Las Vegas casino-Hell was overthrown and Johnny Blaze claimed the throne, ruling as King of Hell through Ed Brisson's <em>Ghost Rider</em> (2019–20) — a job that steadily corrupted him until Danny Ketch had to intervene. Benjamin Percy's <em>Ghost Rider</em> (2022–24) reset him again: a small-town mechanic with a wife and children whose life is revealed to be a construct of Hell, sent back on the road with an FBI agent, Talia Warroad, on his trail. Percy's <em>Final Vengeance</em> (2024) passed the Spirit to Frank Castle before Johnny reclaimed it.",
                "Across every version the constants hold: a man who did one desperate thing, a demon that will not leave, a motorcycle, and a road that never ends.")))

    body += related(["danny-ketch", "spirit-of-vengeance", "storylines", "movies", "vehicles", "weapons"])
    return dict(slug=s, title="Johnny Blaze", desc="Johnny Blaze, the original Ghost Rider: his deal with Mephisto, the Zarathos years, the Champions, the 1990s partnership with Danny Ketch, Damnation and his reign as King of Hell.", keywords="Johnny Blaze, Roxanne Simpson, Crash Simpson, King of Hell, Quentin Carnival", body=body, vid_pos="60% 50%")
