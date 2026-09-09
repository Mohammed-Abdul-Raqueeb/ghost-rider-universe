from ._h import *
from build import crumbs, related

def page():
    s = "gallery"
    body = hero("GALLERY", "Stills from the ride, pulled from the film footage that burns behind every page of this site. Tap any frame to open it.", crumbs(s), kicker="Frames", short=True, cue=False)
    caps = {
        "00": ("Before the change", "The rider walks toward the burning machine.", ""),
        "02": ("Ignition", "Flame takes the tyres first.", "wide"),
        "04": ("The burn", "Skin gives way to fire and smoke.", ""),
        "06": ("Mounting up", "Hellfire on the rear wheel, road ahead.", ""),
        "08": ("Full ride", "Flame streams off the bike at speed.", ""),
        "10": ("Down the highway", "A straight road and a wall of smoke.", "wide"),
        "12": ("Pursuit", "Low angle on the flaming skull.", ""),
        "14": ("Open sky", "The desert road, cloud and fire.", ""),
        "16": ("The turn", "Weight over the front wheel.", ""),
        "18": ("The skull", "The Spirit, face to face.", "wide"),
        "20": ("Hellfire close", "Detail of the flame around bone.", ""),
        "22": ("Ember light", "The head wreathed in sparks.", ""),
        "24": ("The stare", "Eye contact with the Rider.", ""),
        "26": ("Afterburn", "Flame climbing from the jacket.", ""),
        "27": ("Last frame", "The ride ends in fire.", ""),
    }
    figs = "".join(f'<figure class="{cls}"><img src="assets/img/stills/still-{k}.jpg" alt="{alt}" loading="lazy" width="960" height="540"><figcaption>{t}</figcaption></figure>' for k, (t, alt, cls) in caps.items())
    body += f'<section class="band tight"><div class="gallery reveal">{figs}</div></section>'
    body += band(plate(p("These frames are taken from the source footage supplied for this site and rendered as the background video on every page. Use the arrow keys inside the viewer to move between frames; press Esc to close."), "center"))
    body += related(["videos", "transformations", "vehicles", "movies"])
    return dict(slug=s, title="Gallery", desc="A Ghost Rider gallery of stills from the ride: ignition, the burning skull, the hellfire motorcycle and the desert highway.", keywords="Ghost Rider gallery, stills, images, flaming skull, hellfire motorcycle", body=body, vid_pos="50% 50%")
