from ._h import *
from build import crumbs, related

def page():
    s = "trivia"
    body = hero("TRIVIA", "Facts from five decades of hellfire: creator arguments, near-misses, cameos and the small print of the curse.", crumbs(s), kicker="Did you know", align="right", short=True)
    T = [
        "Ghost Rider was originally pitched by Gary Friedrich as a villain for Daredevil. Roy Thomas thought the flaming-skull biker was too good to waste on one issue and made him a lead instead.",
        "Friedrich later sued Marvel over ownership of the character; the case was settled in 2013, shortly before the second film's rights reverted to Marvel.",
        "Nicolas Cage had a Ghost Rider tattoo on his arm before he was cast. It had to be covered with make-up on set, since Johnny Blaze wasn't supposed to have one.",
        "Danny Ketch's Ghost Rider could not speak for his first several issues, which is why the 1990 series reads so much like a slasher film.",
        "The Ketch series' final issue, #94, was written and drawn in 1998 but not published until Ghost Rider Finale in 2007, nine years later.",
        "The Penance Stare famously failed on the Punisher, who had already accepted every death on his conscience; in a lighter register it has also bounced off Deadpool.",
        "Robbie Reyes's Charger is a 1969 model — the same model year as the Dukes of Hazzard's General Lee.",
        "The 2012 film's Rider does not walk — he twitches, rolls and lurches, because Nicolas Cage played the character himself, in black face paint and contact lenses, rather than leaving it to a stunt double.",
        "Cosmic Ghost Rider began as a single-issue gag in Thanos #13 and ended up with three miniseries and a place in the main Marvel Universe.",
        "Zarathos and Mephisto's rivalry is essentially a business dispute: Mephisto tricked Zarathos into a losing war for market share of souls before imprisoning him.",
        "The 1967 Ghost Rider was renamed twice — Night Rider in the 1970s (a name Marvel dropped because of its associations) and then Phantom Rider in 1980.",
        "Sam Elliott's Caretaker in the 2007 film was revealed to be Carter Slade, making the movie the only adaptation to feature two Ghost Riders from different centuries riding together.",
        "In the Marvel vs. Capcom fighting games the Ghost Rider is Johnny Blaze; in Marvel's Midnight Suns (2022) the playable Rider is Robbie Reyes.",
        "Jason Aaron's run gave Ghost Riders to Congo, China and Turkey, and his Avengers introduced a mammoth-riding Rider from 1,000,000 BC — making the Spirit of Vengeance older than the wheel.",
        "The July 2026 Comic-Con announcement made Ryan Gosling the second actor to headline as Johnny Blaze in live action, after Nicolas Cage's two films.",
        "Marvel Studios' Ghost Rider is dated July 28, 2028 — fifty-six years, almost to the month, after Marvel Spotlight #5 hit newsstands in August 1972.",
        "The background footage on this site was supplied as a vertical phone video. It was rotated, re-encoded and trimmed to 28 seconds to run as a landscape loop; the gallery stills are frames from the same clip.",
    ]
    body += '<section class="band"><div class="trivia">' + "".join(f'<div class="plate reveal"><div class="n">{i+1:02d}</div>{p(t)}</div>' for i, t in enumerate(T)) + "</div></section>"
    body += related(["quotes", "news", "comic-history", "movies", "about"])
    return dict(slug=s, title="Trivia", desc="Ghost Rider trivia: creator disputes, Nicolas Cage's tattoo, the unpublished issue #94, Penance Stare failures, the 1969 Charger and the 2028 film.", keywords="Ghost Rider trivia, facts, Nicolas Cage tattoo, Gary Friedrich lawsuit, Penance Stare Punisher", body=body, vid_pos="45% 50%")
