from ._h import *
from build import related

def page():
    body = hero("LOST ON<br>THE ROAD", "There is no page at this address. The Rider has checked; nothing here has spilled innocent blood, so there is nothing to punish. Try one of the routes below.", "", kicker="404 — not found", align="center", cue=False,
                cta='<a class="btn" href="index.html">Back to the start</a><button class="btn ghost" type="button" data-open-search>Search the universe</button>')
    body += related(["overview", "johnny-blaze", "danny-ketch", "robbie-reyes", "villains", "storylines", "movies", "news"])
    return dict(slug="404", title="Page not found", desc="The page you were looking for is not on this road.", body=body, vid_pos="50% 50%")
