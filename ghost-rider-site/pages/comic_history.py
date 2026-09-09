from ._h import *
from build import crumbs, related

def page():
    s = "comic-history"
    body = hero("COMIC BOOK<br>HISTORY", "Ten volumes of the main title, a dozen spin-offs and a publishing life that mirrors every fashion in American comics from the 1970s horror boom to the 2020s event machine.", crumbs(s), kicker="Publication history", wide=True)

    body += band('<div class="plate wide center"><h2>The main title, volume by volume</h2><table class="tbl"><thead><tr><th>Vol.</th><th>Dates</th><th>Issues</th><th>Lead</th><th>Notable creators</th></tr></thead><tbody>'
        '<tr><td>1</td><td>Feb–Nov 1967</td><td>7</td><td>Carter Slade (Western)</td><td>Gary Friedrich, Roy Thomas, Dick Ayers</td></tr>'
        '<tr><td>—</td><td>Aug 1972–1973</td><td>Marvel Spotlight #5–11</td><td>Johnny Blaze</td><td>Friedrich, Mike Ploog, Jim Mooney</td></tr>'
        '<tr><td>2</td><td>Sep 1973–Jun 1983</td><td>81</td><td>Johnny Blaze</td><td>Friedrich, Tony Isabella, Jim Shooter, Michael Fleisher, Roger Stern, J.M. DeMatteis; Gil Kane, Don Perlin, Bob Budiansky</td></tr>'
        '<tr><td>3</td><td>May 1990–Feb 1998</td><td>93 (+#94, 2007)</td><td>Danny Ketch</td><td>Howard Mackie, Ivan Velez Jr.; Javier Saltares, Mark Texeira, Ron Garney, Salvador Larroca</td></tr>'
        '<tr><td>4</td><td>Jul 2001–Jan 2002</td><td>6</td><td>Johnny Blaze</td><td>Devin Grayson, Trent Kaniuga (Marvel Knights)</td></tr>'
        '<tr><td>5</td><td>Nov 2005–Apr 2006</td><td>6</td><td>Johnny Blaze — "Road to Damnation"</td><td>Garth Ennis, Clayton Crain</td></tr>'
        '<tr><td>6</td><td>Sep 2006–Jul 2009</td><td>35</td><td>Johnny Blaze; Danny Ketch</td><td>Daniel Way, Jason Aaron; Mark Texeira, Javier Saltares, Roland Boschi, Tan Eng Huat</td></tr>'
        '<tr><td>7</td><td>Aug 2011–May 2012</td><td>9 (+0.1)</td><td>Alejandra Jones</td><td>Rob Williams, Matthew Clark</td></tr>'
        '<tr><td>8</td><td>Jan–May 2017</td><td>5</td><td>Robbie Reyes</td><td>Felipe Smith, Danilo Beyruth</td></tr>'
        '<tr><td>9</td><td>Dec 2019–Sep 2020</td><td>7</td><td>Johnny Blaze & Danny Ketch — King of Hell</td><td>Ed Brisson, Aaron Kuder, Juan Frigeri</td></tr>'
        '<tr><td>10</td><td>Apr 2022–Feb 2024</td><td>21 (+Annual)</td><td>Johnny Blaze</td><td>Benjamin Percy, Cory Smith</td></tr>'
        '</tbody></table></div>')

    body += shout("THE 1970s", "Horror comes to Marvel",
        plate(p("The 1971 revision of the Comics Code re-admitted vampires, ghouls and werewolves, and Marvel built a horror line overnight. Ghost Rider debuted in <em>Marvel Spotlight</em> #5, moved to his own book in 1973 and stayed there for a decade — through the Champions (1975–78), team-ups with Spider-Man, Daredevil and the Thing, and a steady drift from monster-of-the-month stories toward the character study that ended the run.",
                "J.M. DeMatteis's closing issues (#77–81, 1983) named and expelled Zarathos and gave Johnny Blaze a rare thing in superhero comics: a real ending.")))

    body += shout("THE 1990s", "Ketch, Midnight Sons and the boom",
        plate(p("The 1990 relaunch by Mackie and Saltares hit at the peak of the speculator market. <em>Ghost Rider</em> vol. 3 was a top-selling book; it spawned <em>Ghost Rider/Blaze: Spirits of Vengeance</em> (1992–94), <em>Blaze</em> (1994–95), <em>Ghost Rider 2099</em> (1994–96), <em>Midnight Sons Unlimited</em>, and the whole Midnight Sons imprint of supernatural titles. The 1992 <em>Rise of the Midnight Sons</em> crossover and 1993's <em>Siege of Darkness</em> were line-wide events.",
                "By the late 1990s the market had collapsed; the series ended in 1998 with its final issue unpublished for nearly a decade."), "right"), flip=True)

    body += shout("THE 2000s", "Marvel Knights and the Ennis reset",
        plate(p("A six-issue Marvel Knights series in 2001 (Devin Grayson, Trent Kaniuga) and Garth Ennis's painted <em>Road to Damnation</em> (2005) and <em>Trail of Tears</em> (2007) with Clayton Crain restored the character's horror credentials just as the first film arrived. Daniel Way's 2006 ongoing and Jason Aaron's run from #20 (2008) rebuilt the mythology — Zadkiel, Heaven's design, an army of Riders — and remain the most acclaimed modern stretch.")))

    body += shout("THE 2010s", "New hosts",
        plate(p("Marvel tried a new host twice in three years: Alejandra Jones (2011) and Robbie Reyes (2014). <em>All-New Ghost Rider</em> ran twelve issues; Robbie returned for a 2016–17 series, then joined Jason Aaron's <em>Avengers</em> in 2018. Cosmic Ghost Rider (2017) became an unexpected hit, headlining three miniseries. <em>Damnation</em> (2018) put Johnny Blaze on the throne of Hell, and the 2019–20 series dealt with the consequences."), "right"), flip=True)

    body += shout("THE 2020s", "Percy, Pirzada and the Violent Era",
        plate(p("Benjamin Percy's <em>Ghost Rider</em> (2022–24) was the longest Blaze-led run since the 1970s, extended by the <em>Weapons of Vengeance</em> crossover with <em>Wolverine</em>, <em>Final Vengeance</em> (2024) and <em>Vengeance Forever</em>. Sabir Pirzada's <em>Spirits of Vengeance</em> (2024–25) and <em>Spirits of Violence</em> (2025–26) gathered every Rider into one story. Marvel's collected-edition programme — Omnibuses, Epic Collections and a Percy Omnibus scheduled for 2026 — has meanwhile put the whole history back in print.")))

    body += related(["comics", "storylines", "timeline", "danny-ketch", "johnny-blaze"])
    return dict(slug=s, title="Comic Book History", desc="Ghost Rider's publication history from the 1967 Western to the 2020s: every volume of the main title, key creators, the Midnight Sons era, the Ennis and Aaron runs and the Violent Era.", keywords="Ghost Rider comics history, Marvel Spotlight 5, Ghost Rider volumes, Midnight Sons, Jason Aaron, Benjamin Percy", body=body, vid_pos="50% 50%")
