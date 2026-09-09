from ._h import *
from build import crumbs, related

def page():
    s = "transformations"
    body = hero("TRANS-<br>FORMATIONS", "The moment the skin goes and the fire comes. It has been written as a curse, a choice, a reflex and a possession — and each host burns differently.", crumbs(s), kicker="The change", cue=True)

    body += shout("THE TRIGGER", "What starts the burn",
        plate(p("<strong>Johnny Blaze, 1972–83:</strong> nightfall. In the earliest stories the transformation was involuntary and time-bound; Johnny changed at dusk and back at dawn, regardless of what he wanted. Later the trigger shifted to the presence of evil, then to Johnny's own will as he learned to summon or suppress Zarathos.",
                "<strong>Danny Ketch:</strong> innocent blood. Danny changed when innocent blood was spilled near him — a rule that made the 1990 Rider feel like a summoned force rather than a hero patrolling for trouble. Touching the Hell Cycle's gas cap was required at first; the dependency faded.",
                "<strong>Robbie Reyes:</strong> will, and Eli. Robbie could ignite at will, but Eli could also seize the body while Robbie slept or lost focus. His transformation is quicker and cleaner — the flame does not so much burn away his flesh as replace it.")))

    body += drift("It does not hurt him. That is the worst part. It feels like relief.", right=True)

    body += shout("THE<br>ANATOMY", "Skull, flame, leather",
        plate(p("Mike Ploog's 1972 design set the template: a bare human skull wreathed in flame, on a body in black leather. Over fifty years the details have signalled which Rider you are looking at.",
                "<strong>Blaze (classic):</strong> exposed skull, orange flame, blue-and-black leathers with a raised collar. Later designs add spikes on the shoulders and, from the 2000s, a heavier biker jacket.",
                "<strong>Ketch:</strong> a longer, more animalistic skull; spiked leather jacket and gauntlets; a chain wound around the chest; flame that streams backward from the head like hair.",
                "<strong>Reyes:</strong> a smooth, helmet-like skull with a jagged mouth and a single vertical ridge, blue-white flame, a jacket with a burning \"racing stripe\" and flames that erupt from the sleeves and collar.",
                "<strong>Cosmic Ghost Rider:</strong> Castle's skull under a spiked Punisher-styled leather jacket, flame shot through with cosmic energy."), "right"), flip=True)

    body += shout("PARTIAL<br>& FORCED", "Not every transformation is complete",
        plate(p("Writers have used incomplete transformations to show a host's state of mind. A half-burned face means the Spirit is winning; a skull that will not ignite means the host is cut off from the power. In <em>Ghost Rider: Road to Damnation</em> (2005), Johnny's changes were shown as agonising bone-by-bone burns; in the 2007 film the sequence was rendered as skin cracking and peeling from the inside.",
                "Forced transformations are a recurring horror beat. Blackout's attacks on Ketch, Lilith's rituals, and Eli Morrow's midnight hijacking of Robbie all turn the Rider's greatest asset into the thing the host fears most: waking up somewhere with blood on the chain.")))

    body += related(["powers", "spirit-of-vengeance", "johnny-blaze", "danny-ketch", "robbie-reyes"])
    return dict(slug=s, title="Transformations", desc="How each Ghost Rider transforms: the triggers, the anatomy of the burning skull, and the partial and forced transformations that drive the horror.", keywords="Ghost Rider transformation, flaming skull design, Mike Ploog", body=body, vid_pos="70% 50%")
