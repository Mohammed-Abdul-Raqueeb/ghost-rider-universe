from ._h import *
from build import crumbs, related

def page():
    s = "comics"
    body = hero("COMICS", "Where to start reading, what to read next and which collections hold it all. Built for a reader who wants the good stuff without fifty years of back issues.", crumbs(s), kicker="Reading guide")

    body += shout("START<br>HERE", "Four doors into the universe",
        plate('<table class="tbl"><thead><tr><th>If you want…</th><th>Read</th><th>Collected in</th></tr></thead><tbody>'
              '<tr><td>The original horror</td><td>Marvel Spotlight #5–11, Ghost Rider (1973) #1–20</td><td>Ghost Rider Epic Collection vol. 1: Hell on Wheels</td></tr>'
              '<tr><td>The 1990s Rider</td><td>Ghost Rider (1990) #1–12</td><td>Ghost Rider: Danny Ketch Epic Collection vol. 1: Vengeance Reborn</td></tr>'
              '<tr><td>The best modern run</td><td>Ghost Rider (2006) #20–35, Heaven\'s on Fire #1–6</td><td>Ghost Rider by Jason Aaron Omnibus</td></tr>'
              '<tr><td>Robbie Reyes</td><td>All-New Ghost Rider #1–12</td><td>Ghost Rider: Robbie Reyes — The Complete Collection</td></tr>'
              '</tbody></table>', "wide"))

    body += shout("THEN<br>GO HERE", "The second wave",
        plate(p("<strong>Road to Damnation</strong> and <strong>Trail of Tears</strong> (Ennis/Crain) — two self-contained painted miniseries, both collected together in the Ghost Rider by Garth Ennis Omnibus.",
                "<strong>Hearts of Darkness</strong> and <strong>Rise of the Midnight Sons</strong> — the 1990s at full volume; the Danny Ketch Epic Collections vols. 2–6 (2025–26) cover the whole Midnight Sons era, with a Danny Ketch Omnibus vol. 3 scheduled for January 2027.",
                "<strong>Cosmic Ghost Rider</strong> (Cates/Shaw) — Thanos #13–18 and the 2018 miniseries, collected as Cosmic Ghost Rider: Baby Thanos Must Die.",
                "<strong>Ghost Rider by Benjamin Percy</strong> — the 2022–24 run plus Weapons of Vengeance, Final Vengeance and Vengeance Forever, with an Omnibus solicited for October 2026."), "right"), flip=True)

    body += drift("Fifty years, ten volumes, one road. Start anywhere the fire catches.", right=True)

    body += shout("THE FULL<br>SHELF", "Collections at a glance",
        plate('<table class="tbl"><thead><tr><th>Era</th><th>Format</th></tr></thead><tbody>'
              '<tr><td>1967 Western</td><td>Marvel Masterworks: Ghost Rider vol. 1; Essential Ghost Rider (Western) </td></tr>'
              '<tr><td>1972–83 Blaze</td><td>Ghost Rider Omnibus vols. 1–2; Epic Collections (Hell on Wheels, The Salvation Run, …); Essential Ghost Rider vols. 1–4</td></tr>'
              '<tr><td>1990–98 Ketch</td><td>Ghost Rider: Danny Ketch Omnibus vols. 1–3; Danny Ketch Epic Collections; Midnight Sons collections</td></tr>'
              '<tr><td>2001–09</td><td>Ghost Rider: Hammer Lane; Ghost Rider by Garth Ennis Omnibus; Ghost Rider by Daniel Way — The Complete Collection; Ghost Rider by Jason Aaron Omnibus</td></tr>'
              '<tr><td>2011–17 new hosts</td><td>Ghost Rider: The Complete Series by Rob Williams; Ghost Rider: Robbie Reyes — The Complete Collection; Ghost Racers</td></tr>'
              '<tr><td>2017–21</td><td>Cosmic Ghost Rider collections; Damnation; Ghost Rider: King of Hell; Avengers by Jason Aaron</td></tr>'
              '<tr><td>2022–26</td><td>Ghost Rider by Benjamin Percy vols. 1–4 and Omnibus; Spirits of Vengeance; Spirits of Violence; Hellverine</td></tr>'
              '</tbody></table>', "wide"))

    body += shout("DIGITAL", "Marvel Unlimited",
        plate(p("Almost every issue mentioned on this site is on Marvel Unlimited, including the Infinite Comics (Ghost Rider: Kushala, 2021) that never saw print. Reading-order guides such as Crushing Krisis maintain issue-by-issue listings that are updated as new collections are solicited."), "right"), flip=True)

    body += related(["comic-history", "storylines", "johnny-blaze", "danny-ketch", "robbie-reyes"])
    return dict(slug=s, title="Comics — Where to Start", desc="A Ghost Rider reading guide: where to start, essential runs by Ennis, Aaron, Mackie, Smith, Cates and Percy, and every omnibus and Epic Collection.", keywords="Ghost Rider reading order, where to start, omnibus, Epic Collection, Marvel Unlimited", body=body, vid_pos="55% 50%")
