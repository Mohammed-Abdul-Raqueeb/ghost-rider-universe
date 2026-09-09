from ._h import *
from build import crumbs, related

def page():
    s = "other-riders"
    body = hero("OTHER<br>GHOST RIDERS", "The name has been worn by a horseman, a Nicaraguan teenager, an Apache sorcerer, a 21st-century hacker, a caveman on a mammoth and the Punisher. Here is the rest of the roster.", crumbs(s), kicker="The wider lineage", wide=True)

    R = []
    def rider(era, name, alias, text, cls=""):
        R.append(f'<div class="rider reveal"><div class="who"><p class="era">{era}</p><h2>{name}</h2><p class="alias {cls}">{alias}</p></div>{plate(text, cls)}</div>')

    rider("1967", "CARTER<br>SLADE", "The Western Ghost Rider · later Phantom Rider",
          p("A Texas schoolteacher who fought outlaws in a glowing white costume on the stallion Banshee. Created by Gary Friedrich, Roy Thomas and Dick Ayers, he held the Ghost Rider name for seven issues in 1967 before Marvel gave it to Johnny Blaze. He was renamed Night Rider and then Phantom Rider; Sam Elliott played a version of him in the 2007 film as a retired Spirit of Vengeance.") + '<p class="fig"><a href="origins.html">Full origin</a></p>')
    rider("1992", "MICHAEL<br>BADILINO", "Vengeance",
          p("An NYPD lieutenant whose family had been cursed by Zarathos, Badilino was granted a Spirit of Vengeance by Mephisto to hunt the Ghost Rider (Ghost Rider vol. 3 #21, 1992). His Rider had a purple flame, bone spurs and a bike bristling with blades. He became an uneasy ally, joined the Midnight Sons and later sacrificed himself. Vengeance is the archetype for a Rider whose power comes with a leash held in Hell."))
    rider("1994", "ZERO<br>COCHRANE", "Ghost Rider 2099",
          p("Len Kaminski and Chris Bachalo's cyberpunk Rider: Kenshiro \"Zero\" Cochrane, a hacker in Transverse City who uploaded his consciousness to escape death and was downloaded into a chromed robotic body with a flaming skull by a group of artificial intelligences. No demons, no Spirit — pure Marvel 2099 — but the same silhouette and the same appetite for punishing the powerful. 25 issues, 1994–96."), "cosmic")
    rider("2011", "ALEJANDRA<br>JONES", "The Nicaraguan Ghost Rider",
          p("Created by Rob Williams and Matthew Clark for Ghost Rider vol. 7 #1 (2011). Alejandra was raised by the angel Adam, who stripped Johnny Blaze of his Spirit of Vengeance and gave it to her as part of a scheme to purge humanity of sin. Her Rider could fly and wielded hellfire tinged with angelic light. When Adam's plan collapsed, Johnny reclaimed most of the power, leaving her with a fragment; she later fought alongside the Riders and died in the 2019–20 series."))
    rider("2016", "KUSHALA", "The Spirit Rider · Demon Rider",
          p("An Apache woman of the 1800s who bound a Spirit of Vengeance to herself to avenge her people, then trained in sorcery until she became the Sorcerer Supreme of her era. Introduced by Robbie Thompson and Javier Rodríguez in Doctor Strange and the Sorcerers Supreme (2016), she has since appeared in Midnight Suns (2022), Ghost Rider: Kushala (2021, Infinite Comic) and Spirits of Violence (2025–26). Her Rider can use magic and hellfire together, and she is one of the few hosts to have chosen the bond deliberately."))
    rider("2017", "FRANK<br>CASTLE", "Cosmic Ghost Rider",
          p("In an alternate future where Thanos won, the Punisher died, went to Hell, took Mephisto's deal to become a Ghost Rider, then took Galactus's deal to become his herald. The result — introduced by Donny Cates and Geoff Shaw in Thanos #13 (2017) — was a laughing, insane, cosmically powered Rider who served Thanos before turning on him. Cosmic Ghost Rider has since headlined three miniseries and drifted into the main timeline.") + '<p class="fig"><a href="multiverse.html">More in the Multiverse</a></p>', "cosmic")
    rider("2017", "THE FIRST<br>RIDER", "Ghost Rider, 1,000,000 BC",
          p("Introduced in Marvel Legacy #1 (2017) by Jason Aaron and Esad Ribić, the Stone Age Ghost Rider was a caveman whose tribe was slaughtered and who accepted a Spirit of Vengeance to punish the killers. He rides a flaming woolly mammoth and served on the prehistoric Avengers alongside Odin, Agamotto and the first Black Panther. He represents the Spirits as an ancient, global institution rather than a modern curse."))
    rider("2023", "HELLVERINE", "Bagra-ghul in Wolverine",
          p("Benjamin Percy's Weapons of Vengeance crossover (2023) introduced Bagra-ghul, a demon in the Spirit of Vengeance lineage, which possessed Wolverine and later his son Akihiro to create Hellverine — a Rider with claws. The character headlined two Hellverine miniseries (2024–25) and appears in Spirits of Violence."))
    rider("2024–25", "THE NEW<br>GENERATION", "Fantasma and the Violent Era",
          p("Sabir Pirzada's Spirits of Vengeance (2024–25) and Spirits of Violence (2025–26) widened the roster again: the newcomer Fantasma, Barbara Ketch resurrected as the Spirit of Violence, and the assembled Riders — Blaze, Ketch, Reyes, Kushala, Hellverine — facing her together. Marvel has called it the \"Violent Era\" of the character."))

    body += '<section class="band"><div class="roster">' + "".join(R) + "</div></section>"
    body += related(["johnny-blaze", "danny-ketch", "robbie-reyes", "multiverse", "spirit-of-vengeance"])
    return dict(slug=s, title="Other Ghost Riders", desc="Every other Ghost Rider: Carter Slade, Vengeance, Ghost Rider 2099, Alejandra Jones, Kushala, Cosmic Ghost Rider, the prehistoric Rider, Hellverine and the Violent Era.", keywords="Carter Slade, Alejandra Jones, Kushala, Cosmic Ghost Rider, Ghost Rider 2099, Vengeance, Hellverine, Fantasma", body=body, vid_pos="50% 50%")
