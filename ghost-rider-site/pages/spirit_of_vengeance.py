from ._h import *
from build import crumbs, related

def page():
    s = "spirit-of-vengeance"
    body = hero("THE SPIRIT OF<br>VENGEANCE", "The thing inside the skull. Several entities have worn the name; each has its own agenda, and none of them chose their hosts kindly.", crumbs(s), kicker="The passenger")

    body += shout("ZARATHOS", "The demon in Johnny Blaze",
        plate(p("For the first decade of stories, the transformation was simply the devil's curse. Then, in the final issues of <em>Ghost Rider</em> vol. 2 (written by J.M. DeMatteis, 1982–83), the Spirit was given a name and a biography: Zarathos, an ancient demon who once ruled a cult of worshippers on Earth and was so powerful that Mephisto — jealous of the competition for souls — tricked him, bound him and used him as a torment for Blaze.",
                "Zarathos was arrogant, cruel and interested chiefly in his own freedom. He was not a force of justice; the \"vengeance\" of the early Rider was as likely to hurt bystanders as villains. The 1983 finale separated Zarathos from Johnny, trapping the demon in the Crystal of Souls belonging to Centurious, the man without a soul. Zarathos returned in the 1990s and has resurfaced periodically as a threat rather than a passenger.")))

    body += shout("NOBLE KALE", "The ancestor in Danny Ketch",
        plate(p("The Spirit of the 1990 series was assumed to be Zarathos until writer Ivan Velez Jr. revealed him as Noble Kale: a young man in 18th-century Salem-era America whose Puritan father, Pastor Kale, made a bargain with Mephisto that turned Noble into a Spirit of Vengeance. Bound to the Kale family bloodline, Noble manifested through the firstborn of each generation — which is how he came to Danny, whose mother's family were Kales, and how Johnny Blaze, Danny's long-lost brother, carried a different piece of the same inheritance.",
                "Noble Kale was the first Spirit written as a genuine hero: reluctant, weary, capable of speech and moral judgement. Where Zarathos wanted out, Noble wanted the killing to stop. The 1998 finale of the series showed him negotiating a place among the archangels; later stories restored him to Danny."), "right"), flip=True)

    body += drift("A Spirit of Vengeance was never meant to be a punishment. Heaven built it as a verdict.", "The Zadkiel retcon, Ghost Rider (2006) #20–35")

    body += shout("HEAVEN'S<br>DESIGN", "The Jason Aaron cosmology",
        plate(p("In <em>Ghost Rider</em> vol. 6 (2008–09), Jason Aaron rewrote the Spirits' origin. They were not demons but angelic constructs — instruments of divine judgement created by God, one for each region of the Earth, riding everything from motorcycles to mammoths. The renegade archangel Zadkiel had corrupted the arrangement, lying to hosts about the source of their power so that they would believe themselves damned and serve his war on Heaven.",
                "The retcon reconciled the contradictions: a demon could be bound into a Spirit (Zarathos), a human soul could become one (Noble Kale), and a global network of Riders — Baron Skullfire in Congo, the Chinese Rider Bai Gu Jing, the mammoth-riding Ghost Rider of 1,000,000 BC introduced later in Aaron's <em>Avengers</em> — could all exist at once.",
                "It also explained Zarathos's return in Aaron's run: after Zadkiel's defeat, the demon was released back into Johnny Blaze as his Spirit of Vengeance, its hunger now at least pointed at the guilty.")))

    body += shout("THE FALSE<br>SPIRIT", "Eli Morrow and Robbie Reyes",
        plate(p("What powered Robbie Reyes from 2014 to 2019 was not a Spirit of Vengeance. It was the ghost of Eli Morrow, his maternal uncle — a machinist who had served a satanic cult, killed dozens of people, and died in prison. Bound to the Charger's frame, Eli gave Robbie a Rider's power in exchange for a share of his body.",
                "The distinction mattered: Eli's Rider had a different anatomy, a different flame and no Penance Stare. Only in later stories — after Robbie briefly became King of Hell in <em>Avengers</em> (2018–21) and expelled Eli — did an authentic Spirit of Vengeance bond to him, which is why the modern Robbie can stand alongside Blaze and Ketch as a full Rider."), "blue"), flip=True)

    body += band('<div class="plate wide center"><h2>Named Spirits and the hosts who carried them</h2><table class="tbl"><thead><tr><th>Spirit</th><th>Nature</th><th>Hosts</th><th>First named</th></tr></thead><tbody>'
        '<tr><td>Zarathos</td><td>Ancient demon, later revealed as a corrupted celestial construct</td><td>Johnny Blaze; briefly others</td><td>Ghost Rider vol. 2 #77 (1983)</td></tr>'
        '<tr><td>Noble Kale</td><td>Human soul transformed by a Hell-bargain, bound to the Kale bloodline</td><td>Danny Ketch, Kale ancestors</td><td>Ghost Rider vol. 3 (1994–96)</td></tr>'
        '<tr><td>The Spirit of Corruption / Vengeance (Badilino)</td><td>A separate infernal spirit granted by Mephisto</td><td>Michael Badilino as Vengeance</td><td>Ghost Rider vol. 3 #21 (1992)</td></tr>'
        '<tr><td>Kushala\'s Spirit</td><td>A Spirit of Vengeance summoned by a grieving Apache woman</td><td>Kushala</td><td>Doctor Strange and the Sorcerers Supreme (2016)</td></tr>'
        '<tr><td>Eli Morrow (impostor)</td><td>Ghost of a satanic serial killer</td><td>Robbie Reyes</td><td>All-New Ghost Rider (2014)</td></tr>'
        '<tr><td>Cosmic Spirit</td><td>Spirit of Vengeance fused with the Power Cosmic</td><td>Frank Castle (alternate future)</td><td>Thanos #13 (2017)</td></tr>'
        '<tr><td>Bagra-ghul</td><td>A demon in the Spirit lineage that possessed Wolverine as Hellverine</td><td>Logan / Akihiro</td><td>Weapons of Vengeance (2023)</td></tr>'
        '</tbody></table></div>')

    body += related(["lore", "hell", "johnny-blaze", "danny-ketch", "robbie-reyes", "other-riders"])
    return dict(slug=s, title="The Spirit of Vengeance", desc="Zarathos, Noble Kale, Eli Morrow, Heaven's design and every named Spirit of Vengeance in Ghost Rider lore.", keywords="Zarathos, Noble Kale, Zadkiel, Eli Morrow, Spirit of Vengeance origin", body=body, vid_pos="55% 40%")
