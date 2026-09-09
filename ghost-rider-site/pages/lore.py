from ._h import *
from build import crumbs, related

def page():
    s = "lore"
    body = hero("LORE &<br>MYTHOLOGY", "The rules of the world behind the skull: how Spirits are made, how souls are bought, what Heaven and Hell each want from the Riders, and why vengeance is treated as a force of nature.", crumbs(s), kicker="The mythology", wide=True)

    body += shout("VENGEANCE AS<br>A FORCE", "The founding idea",
        plate(p("Ghost Rider stories treat vengeance the way other Marvel books treat gravity: an impersonal force that flows toward the guilty. A Spirit of Vengeance is not angry; it is the thing that happens when innocent blood is spilled and nobody answers for it. That is why Ketch's Rider was summoned by blood rather than by choice, why the Penance Stare judges instead of merely hurting, and why the Rider cannot be aimed at the innocent.",
                "The idea gives the character its moral tension. Vengeance is not justice — it has no mercy, no proportion and no interest in the future — and every host spends their story trying to keep a force of nature from becoming a monster.")))

    body += shout("THE SOUL<br>ECONOMY", "How the deals work",
        plate(p("Marvel's Hell runs on contracts. A soul freely offered can be claimed; a soul protected by another's love or sacrifice cannot; a contract can be broken by a power greater than the one that wrote it. Mephisto's trick in 1972 — curing Crash Simpson and letting him die anyway — is the model: the letter honoured, the intent betrayed.",
                "Later lore extends the market. Blackheart covets contracts he did not write; Zadkiel steals the Spirits Heaven issued; Cosmic Ghost Rider took two deals and paid for both. The Riders themselves are collateral in a dispute between creditors."), "right"), flip=True)

    body += drift("Heaven built the Rider. Hell taught it to enjoy the work.", "The synthesis of Aaron's retcon")

    body += shout("HEAVEN'S<br>INSTRUMENTS", "The Spirits' true origin",
        plate(p("Jason Aaron's 2008–09 run established the mythology most modern stories use. The Spirits of Vengeance were created by God as instruments of judgement, one for each part of the world, and administered by the archangel Zadkiel. Zadkiel rebelled, convinced the hosts their power was demonic, and used their despair to fuel a war on Heaven. Demons like Zarathos were bound into Spirits along the way; human souls like Noble Kale were made into them; Mephisto and the Hell-lords bargained for the rest.",
                "Aaron also introduced the Blood — an ancient order of caretakers keeping the Spirits' records — and the global roster of Riders: Baron Skullfire in the Congo, Bai Gu Jing in China, the Ghost Rider of Turkey, and eventually, in his Avengers, the mammoth-riding Rider of the Stone Age.")))

    body += shout("THE<br>BLOODLINE", "The Kales",
        plate(p("The 1990s added a hereditary layer. Pastor Kale's bargain in 18th-century America turned his son Noble into a Spirit; the curse bound itself to the family's firstborn and to the Medallion of Power, shards of which sat in the souls of Naomi Kale's children, Johnny and Danny. Naomi's attempt to end the curse — by asking Mephisto to spare her third child, Barbara — is the reason Barbara Ketch stayed human, and the reason her death by Blackout hit the story so hard."), "right"), flip=True)

    body += shout("THE<br>THRONE", "Hell as a job",
        plate(p("Since Damnation (2018), Hell has had a succession problem. Mephisto lost his throne to Johnny Blaze; Blaze lost his humanity to the throne; Robbie Reyes held it just long enough to evict Eli Morrow; Mephisto has been clawing his way back ever since. Modern lore treats the crown of Hell as a curse in its own right — the ultimate expression of what the Rider always was: a person forced to run a machine built for punishment.")))

    body += related(["spirit-of-vengeance", "hell", "villains", "storylines", "origins"])
    return dict(slug=s, title="Lore & Mythology", desc="The mythology of Ghost Rider: vengeance as a force, the soul economy of Marvel's Hell, Heaven's creation of the Spirits, Zadkiel, the Blood, the Kale bloodline and the throne of Hell.", keywords="Ghost Rider lore, mythology, Zadkiel, the Blood, Kale bloodline, Medallion of Power, throne of Hell", body=body, vid_pos="50% 50%")
