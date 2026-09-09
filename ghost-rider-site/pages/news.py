from ._h import *
from build import crumbs, related

def page():
    s = "news"
    body = hero("NEWS &<br>UPDATES", "The ledger of what is happening to the Rider now: the Marvel Studios film, the comics line and the collections. Dates are publication dates; sources are named.", crumbs(s), kicker="Updated September 2026", wide=True)
    N = []
    def item(iso, day, mon, title, text, src):
        N.append(f'<article class="reveal"><time datetime="{iso}">{day}<small>{mon}</small></time><div><h3>{title}</h3>{plate(p(text) + f"<p class=\"src\">Source: {src}</p>")}</div></article>')
    item("2026-08-17", "17", "Aug 2026", "Ghost Rider dated: July 28, 2028",
         "Following the D23 fan event, Disney set Ryan Gosling's Ghost Rider for July 28, 2028 — the third Marvel Studios release that year, after the untitled X-Men film (May 5) and ahead of Black Panther 3 (December 15). Shawn Levy directs from a script by Jonathan Tropper.", "Variety")
    item("2026-07-27", "27", "Jul 2026", "Marvel slows down; Ghost Rider is one of two 2028 tentpoles",
         "Kevin Feige told Empire that the studio's sparser calendar — only Spider-Man: Brand New Day, Avengers: Doomsday and Avengers: Secret Wars before 2028 — is a deliberate focus on quality. Ghost Rider and Black Panther 3 headline the 2028 slate. Reports also say Gosling himself brought the pitch to Marvel.", "Variety")
    item("2026-07-26", "26", "Jul 2026", "Ryan Gosling is Johnny Blaze",
         "At Marvel Studios' Hall H panel at San Diego Comic-Con, Kevin Feige introduced Ryan Gosling as the star of a new standalone Ghost Rider film, with Deadpool & Wolverine director Shawn Levy at the helm. Gosling said he had wanted the role for a long time; Levy said the idea took shape while the two were shooting Star Wars: Starfighter (May 28, 2027).", "Marvel.com, Deadline, ABC News, CNN")
    item("2026-06-27", "27", "Jun 2026", "Collections through January 2027",
         "Updated reading guides list the Ghost Rider by Benjamin Percy Omnibus for October 2026 and Ghost Rider: Danny Ketch Omnibus vol. 3 for January 2027, alongside the continuing Danny Ketch Epic Collection programme.", "Crushing Krisis collecting guide")
    item("2026-04-01", "01", "Apr 2026", "Avengers rumours",
         "Trade reports suggested the Spirit of Vengeance would appear in one of the two upcoming Avengers films — Doomsday (December 18, 2026) or Secret Wars (December 17, 2027) — though which Rider, and whether Gabriel Luna's Robbie Reyes would return, remained unconfirmed. The July Comic-Con announcement answered the casting question.", "Yahoo Entertainment")
    item("2026-02-05", "05", "Feb 2026", "Marvel Legends Johnny Blaze with motorcycle",
         "Hasbro opened pre-orders for a Marvel Legends Ghost Rider Johnny Blaze figure with a motorcycle, priced around $56, for a spring 2026 release.", "Marvelous News")
    item("2025-10-01", "01", "Oct 2025", "Spirits of Violence #1 — the Violent Era begins",
         "Sabir Pirzada and Paul Davidson's five-issue series brings every major Rider — Blaze, Ketch, Kushala, Hellverine, Robbie Reyes and newcomer Fantasma — against the Spirit of Violence, revealed as Danny's resurrected sister Barbara Ketch. The story opens with the death of Linda Littletrees.", "AIPT, Comic Watch")
    item("2025-06-04", "04", "Jun 2025", "Ghost Rider vs. Galactus",
         "A one-shot pitting the Rider against the World-Devourer arrived in June 2025, part of Marvel's run of 'versus' specials.", "Marvel.com")
    item("2024-10-02", "02", "Oct 2024", "Robbie Reyes Special",
         "Robbie's return in a one-shot, ahead of his role in Spirits of Vengeance and Spirits of Violence.", "Marvel.com")
    item("2024-03-06", "06", "Mar 2024", "Final Vengeance",
         "Benjamin Percy's six-issue coda to his run began in March 2024, handing Johnny Blaze's Spirit to Frank Castle before the Vengeance Forever one-shot closed the era.", "Marvel.com")
    body += '<section class="band"><div class="news">' + "".join(N) + "</div></section>"
    body += band(plate(p("This page is a static snapshot compiled in September 2026. It is not a live feed; check the named sources for developments after that date. Corrections and additions belong in <code>pages/news.py</code> in the site source."), "center"))
    body += related(["movies", "comics", "timeline", "trivia"])
    return dict(slug=s, title="News & Updates", desc="Ghost Rider news: Ryan Gosling cast as Johnny Blaze, Shawn Levy directing, the July 28, 2028 release date, Spirits of Violence, Final Vengeance and new collections.", keywords="Ghost Rider news, Ryan Gosling Ghost Rider, 2028 release date, Spirits of Violence, Marvel Studios", body=body, vid_pos="55% 50%")
