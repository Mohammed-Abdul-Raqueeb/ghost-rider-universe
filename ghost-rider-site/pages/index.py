from ._h import *
from build import FLAT, NAV, crumbs, related

def page():
    body = hero(
        '<span class="ignite-wrap"><span class="ignite">GHOST<br>RIDER</span></span>',
        "A stunt rider sold his soul to save his father and came back with a skull of fire. Fifty years on, the Spirit of Vengeance has burned through five hosts, two Hells, one Charger and a multiverse. This is the whole road.",
        "", kicker="Marvel's Spirit of Vengeance", 
        cta='<a class="btn" href="origins.html">Begin with the origin</a><a class="btn ghost" href="johnny-blaze.html">Meet the riders</a>')

    body += stats([("1972", "First appearance, Marvel Spotlight #5"), ("5+", "Human hosts of the Spirit"), ("10", "Volumes of the main title"), ("2028", "Marvel Studios film")])

    body += shout("THE NAME OUTLIVES THE MAN", "One title, many riders",
        plate(p("<span class=\"lead\">Ghost Rider is not a person. It is a sentence.</span>",
                "Whoever carries the Spirit of Vengeance inherits the same terms: a body that burns without being consumed, a stare that returns every cruelty a soul has ever dealt, and a hunger to punish the guilty that never quite belongs to the host. Johnny Blaze took the deal for his father. Danny Ketch touched the wrong motorcycle. Robbie Reyes was murdered in a stolen car and came back with his uncle in the passenger seat.",
                "This site follows all of them — the hosts, the demons that ride them, the lords of Hell who bargain for them, the machines they drive and the fifty-year publishing history that keeps rebuilding the myth.") +
              '<p class="fig"><a href="overview.html">Read the overview</a> or jump straight to <a href="spirit-of-vengeance.html">the Spirit itself</a>.</p>'))

    riders = f'''<section class="band"><div class="roster">
      <div class="rider reveal"><div class="who"><p class="era">1972 — present</p><h2>JOHNNY BLAZE</h2><p class="alias">Host of Zarathos · King of Hell (briefly)</p></div>
        {plate(p("Carnival stunt cyclist who traded his soul to Mephisto to cure his adoptive father's cancer, then watched Crash Simpson die in a jump anyway. The devil kept the receipt: every night the demon Zarathos took over his body.") + '<p class="fig"><a href="johnny-blaze.html">Johnny Blaze in full</a></p>')}</div>
      <div class="rider reveal"><div class="who"><p class="era">1990 — present</p><h2>DANNY KETCH</h2><p class="alias">The Brooklyn Rider · Noble Kale's heir</p></div>
        {plate(p("A teenager from Cypress Hills who found a glowing motorcycle in a junkyard while his sister bled from a gangster's bullet. The gas cap bore a burning sigil; when he touched it he became a taller, leaner, chain-wielding Ghost Rider who could look a killer in the eye and make him feel every wound he had ever inflicted.") + '<p class="fig"><a href="danny-ketch.html">Danny Ketch in full</a></p>')}</div>
      <div class="rider reveal"><div class="who"><p class="era">2014 — present</p><h2>ROBBIE REYES</h2><p class="alias blue">East Los Angeles · The Hell Charger</p></div>
        {plate(p("A high-school mechanic raising his disabled younger brother, shot dead during a street race in a borrowed 1969 Dodge Charger. What brought him back was not a Spirit of Vengeance at all but the ghost of his uncle Eli Morrow, a satanic serial killer with plans for the boy's body.") + '<p class="fig"><a href="robbie-reyes.html">Robbie Reyes in full</a></p>', "blue")}</div>
    </div></section>'''
    body += riders

    body += drift("Vengeance does not forgive. It only balances the ledger.", "The Rider's creed, paraphrased across fifty years of writers")

    dests = ""
    for section, pages in NAV:
        for slug, label, desc in pages:
            dests += f'<a class="dest" href="{slug}.html"><span class="dn">{section}</span><span class="dt">{label}</span><span class="dd">{desc}</span></a>'
    body += f'<section class="band"><div class="shout reveal" style="align-items:start"><div><h2>THE WHOLE ROAD</h2><p class="sub">27 pages, one universe</p></div>{plate(p("Every page is built to stand alone, so start wherever the fire catches. New to the character? Take <a href=\'overview.html\'>Overview</a>, then <a href=\'origins.html\'>Origins</a>, then <a href=\'powers.html\'>Powers</a>. Here for the comics? Go to <a href=\'comics.html\'>Where to start reading</a>. Here because of the movie news? <a href=\'news.html\'>News</a> has the 2028 film.") )}</div></section>'
    body += f'<section class="band tight"><div class="destinations reveal">{dests}</div></section>'

    body += shout("HELL HAS A RELEASE DATE", "Latest",
        plate(p("At San Diego Comic-Con 2026, Marvel Studios announced a new Ghost Rider feature with Ryan Gosling as Johnny Blaze and Shawn Levy directing, from a script by Jonathan Tropper. Disney later dated it for July 28, 2028 — the first Marvel Studios Ghost Rider film, sixteen years after the second Sony picture.") + '<p class="fig"><a href="news.html">Full news ledger</a> · <a href="movies.html">All films</a></p>'), flip=True)

    return dict(slug="index", title="Ghost Rider — Spirit of Vengeance | The Complete Universe",
                desc="The complete Ghost Rider universe: Johnny Blaze, Danny Ketch, Robbie Reyes, the Spirit of Vengeance, villains, vehicles, weapons, storylines, timeline, movies and news.",
                keywords="Zarathos, Mephisto, Hell Cycle, Hell Charger, Penance Stare, Marvel Studios Ghost Rider 2028",
                body=body, vid_pos="50% 50%",
                jsonld={"@context":"https://schema.org","@type":"WebSite","name":"Ghost Rider — Spirit of Vengeance","url":"https://ghostrider.example/","potentialAction":{"@type":"SearchAction","target":"https://ghostrider.example/?q={search_term_string}","query-input":"required name=search_term_string"}})
