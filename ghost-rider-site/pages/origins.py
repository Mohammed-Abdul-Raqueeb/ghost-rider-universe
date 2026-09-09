from ._h import *
from build import crumbs, related

def page():
    s = "origins"
    body = hero("ORIGINS", "Before the skull there was a horseman. Before the horseman there was a bargain. Every Ghost Rider begins with a moment of desperation and someone willing to exploit it.", crumbs(s), kicker="How the fire starts")

    body += shout("1967:<br>THE WESTERN", "Carter Slade, Ghost Rider of the plains",
        plate(p("Marvel's first Ghost Rider had nothing to do with Hell. Created by Gary Friedrich, Roy Thomas and Dick Ayers for <em>Ghost Rider</em> #1 (February 1967), Carter Slade was a schoolteacher in the Old West who, after being nursed back from a near-fatal wound by a Comanche healer, adopted a white costume treated with phosphorescent dust and rode a white stallion named Banshee to terrify outlaws.",
                "The series ran seven issues. When Marvel handed the name to Johnny Blaze in 1972, Slade's character was retitled — first Night Rider, then, from 1980, Phantom Rider. Later stories folded the lineage back together: the Western hero's cousin Lincoln Slade and descendant Hamilton Slade carried the identity forward, and the 2007 film cast Sam Elliott as a Carter Slade who was himself a former Spirit of Vengeance.")))

    body += shout("1972:<br>THE BARGAIN", "Johnny Blaze meets Satan",
        plate(p("In <em>Marvel Spotlight</em> #5 (August 1972), writer Gary Friedrich, editor Roy Thomas and artist Mike Ploog introduced Johnny Blaze, a stunt motorcyclist raised in the Quentin Carnival by \"Crash\" Simpson after the death of his own father, Barton Blaze. When Crash was diagnosed with cancer, Johnny summoned Satan — later revealed to be the demon lord Mephisto — and traded his soul for the cure.",
                "The devil kept the letter of the bargain and broke its spirit: Crash's cancer vanished, and he died days later attempting a record-breaking jump. Mephisto came to collect, but the love of Crash's daughter Roxanne shielded Johnny's soul. As a compromise the demon bound Johnny to Zarathos, a Spirit of Vengeance imprisoned in Hell. At nightfall — and later whenever evil was near — Johnny's flesh burned away and the Ghost Rider rode.",
                "Friedrich had originally pitched the flaming-skull motorcyclist as a villain for <em>Daredevil</em>; Thomas suggested making him a lead instead. The character was popular enough to graduate to his own series, <em>Ghost Rider</em> vol. 2, in September 1973, which ran 81 issues."), "right"), flip=True)

    body += drift("He asked for one life. The devil gave him one death and a passenger.", "Marvel Spotlight #5, in short")

    body += shout("1990:<br>THE JUNKYARD", "Danny Ketch and the burning gas cap",
        plate(p("Howard Mackie and Javier Saltares relaunched the title with <em>Ghost Rider</em> vol. 3 #1 (May 1990). Brooklyn teenager Daniel Ketch and his sister Barbara were visiting Cypress Hills Cemetery on Halloween when they witnessed a firefight between the crime lord Deathwatch's ninja henchmen and a rival gang over stolen canisters of a bio-toxin. Barbara was shot with an arrow. Fleeing into a junkyard, Danny found a motorcycle whose gas cap bore a glowing sigil; touching it in his desperation transformed him into a new Ghost Rider.",
                "This Rider was different: leaner, silent at first, armed with a chain that obeyed his thoughts, and gifted with the Penance Stare. For years the Spirit inside him was assumed to be Zarathos; it was eventually revealed to be Noble Kale, a Ketch ancestor turned into a Spirit of Vengeance in the 18th century after being tricked by Mephisto and a Hell-lord's bargain. The Ketch series became one of the best-selling Marvel books of the early 1990s.")))

    body += shout("2014:<br>THE CHARGER", "Robbie Reyes, East Los Angeles",
        plate(p("Felipe Smith and Tradd Moore's <em>All-New Ghost Rider</em> #1 (March 2014) began with Roberto \"Robbie\" Reyes, a Hillrock Heights high schooler working at a body shop to support his younger brother Gabe, who uses a wheelchair. Needing money, Robbie entered an illegal street race in a 1969 Dodge Charger borrowed from the shop. Hired killers mistook him for the car's owner and shot him dead.",
                "Robbie woke as a Ghost Rider — but the presence that revived him was the ghost of Eli Morrow, his mother's brother, a satanist and serial killer whose remains were tied to the Charger. Eli offered power and protection for Gabe in exchange for the occasional murder. Robbie refused the terms, fought Eli for control and, in later stories, drew the attention of both Johnny Blaze and genuine Spirits of Vengeance. His fire burns blue-white; his skull is a smooth, almost helmet-like shape rather than exposed bone."), "blue"), flip=True)

    body += band(f'''<div class="plate wide center"><h2>The pattern under every origin</h2><div class="cols">
      {p("Each origin is a trade made under duress. Blaze offers his soul for a dying father. Ketch touches an object of power to save a bleeding sister. Reyes accepts a stranger's voice because his brother would otherwise have no one. The Spirits — or the things pretending to be Spirits — arrive precisely when a person is most willing to accept any terms.",
         "The other constant is that vengeance is never quite the host's own. Zarathos hungers for it; Noble Kale was built from it; Eli Morrow wants an excuse for it. The drama of every Ghost Rider story is a human being trying to aim a weapon that wants to fire on its own.",
         "Later writers gave the pattern a cosmology. Jason Aaron's 2008–09 run revealed that the Spirits of Vengeance were originally created by Heaven as instruments of justice, and that the corrupt archangel Zadkiel had spent centuries manipulating them. Robbie's story added another wrinkle: sometimes what rides you is not a Spirit at all, just a very determined dead man.")}
      </div></div>''')

    body += related(["johnny-blaze", "danny-ketch", "robbie-reyes", "spirit-of-vengeance", "timeline", "comic-history"])
    return dict(slug=s, title="Origins", desc="How every Ghost Rider begins: Carter Slade's Western hero, Johnny Blaze's deal with Mephisto, Danny Ketch's haunted motorcycle and Robbie Reyes's Hell Charger.", keywords="Ghost Rider origin, Marvel Spotlight 5, Crash Simpson, Carter Slade, Eli Morrow, Noble Kale", body=body, vid_pos="45% 50%")
