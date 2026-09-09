from ._h import *
from build import crumbs, related

def page():
    s = "about"
    body = hero("ABOUT THE<br>UNIVERSE", "What this site is, how it was built and where the facts come from.", crumbs(s), kicker="About", short=True, cue=False)

    body += shout("WHAT<br>THIS IS", "A reference, not a wiki",
        plate(p("An unofficial, fan-built reference to Marvel's Ghost Rider — the Spirits of Vengeance, their hosts, enemies, machines, stories and adaptations — written as a set of readable pages rather than a database. Every page stands alone, links onward, and is meant to be read top to bottom.",
                "Ghost Rider, Johnny Blaze, Danny Ketch, Robbie Reyes and all related names and likenesses are trademarks of Marvel Characters, Inc. This site is not affiliated with, endorsed by or connected to Marvel, Disney or Sony.")))

    body += shout("SOURCES", "Where the facts come from",
        plate(p("Publication dates, issue numbers and creator credits follow the comics themselves and Marvel's own series listings. Film and television facts come from the productions' credits and contemporary trade reporting. The 2026 film news on this site is drawn from Marvel.com, Variety, Deadline, ABC News and CNN coverage of the San Diego Comic-Con and D23 announcements.",
                "Where a plot point has been retconned — the identity of Danny Ketch's Spirit, the origin of the Spirits themselves — the page says which story changed it. Where a detail could not be verified, it was left out rather than guessed."), "right"), flip=True)

    body += shout("HOW IT'S<br>BUILT", "The technical notes",
        plate(p("<strong>Static HTML.</strong> Every page is a real file generated from a small Python build script, so direct links, search engines and browsers without JavaScript all work. Pages share one layout, one navigation tree, a sitemap, a JSON search index and structured data.",
                "<strong>The video.</strong> The background is the supplied footage, rotated from a vertical phone capture to landscape, trimmed to 28 seconds and encoded twice (720p and 480p). It plays muted, looped and inline at full opacity behind every page; content sits on bounded iron plates rather than a page-wide overlay so the ride stays visible while you scroll. Navigation swaps page content in place so the video never restarts, and the playback position is remembered if a page does reload.",
                "<strong>No dependencies.</strong> One stylesheet, one script, two self-hosted typefaces (Big Shoulders Display and Barlow, both under the SIL Open Font License) and an ember canvas. Motion respects the reduced-motion preference; the layout runs from phones to wide desktops.",
                "<strong>Performance.</strong> Fonts are subset and preloaded, images are lazy-loaded, the ember effect pauses when the tab is hidden, and smaller connections receive the SD video automatically.")))

    body += related(["index", "news", "overview", "comics"])
    return dict(slug=s, title="About the Universe", desc="About this Ghost Rider reference site: what it covers, where its facts come from, how it is built and its relationship to Marvel.", keywords="about, sources, credits, how the site is built", body=body, vid_pos="50% 50%")
