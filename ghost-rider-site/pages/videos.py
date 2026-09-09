from ._h import *
from build import crumbs, related

def page():
    s = "videos"
    body = hero("VIDEOS", "Watch the ride in full, with chapter markers for each beat. The same footage runs behind every page; here it gets a screen of its own.", crumbs(s), kicker="Theater", short=True, cue=False)
    ch = [(0, 3.5, "Walk-up", "The rider approaches the burning bike"), (3.5, 7.5, "Ignition", "Flame takes the body"), (7.5, 12, "Mount", "Onto the machine"), (12, 17.5, "Highway", "Full speed on the desert road"), (17.5, 23, "The skull", "Close on the Spirit"), (23, 28.5, "Afterburn", "Flame and ember to the last frame")]
    chapters = "".join(f'<button type="button" data-t="{a}" data-end="{b}"><span class="t">{int(a//60)}:{int(a%60):02d}</span><span class="l"><strong>{t}</strong><br>{d}</span></button>' for a, b, t, d in ch)
    body += f'''<section class="band tight"><div class="theater reveal">
      <video id="theaterVideo" controls playsinline preload="metadata" poster="assets/img/poster.jpg" muted>
        <source src="assets/video/ghost-rider-theater.mp4" type="video/mp4">
        Your browser does not support HTML video. <a href="assets/video/ghost-rider-theater.mp4">Download the clip</a>.
      </video>
      <div class="bar"><button class="btn ghost" id="theaterFs" type="button">Fullscreen</button><button class="btn ghost" id="theaterMute" type="button">Unmute</button><a class="btn ghost" href="assets/video/ghost-rider-theater.mp4" download>Download</a></div>
      <div class="chapters">{chapters}</div>
    </div></section>'''
    body += band(plate(p("The clip runs 28 seconds, encoded at 1280×720 for desktop and 854×480 for mobile and data-saver connections. The background version on every page is muted and looped; the theater version above carries the original audio track."), "center"))
    body += related(["gallery", "movies", "transformations", "vehicles"])
    return dict(slug=s, title="Videos", desc="Watch the Ghost Rider ride in full with chapter markers: walk-up, ignition, mount, highway, the skull and afterburn.", keywords="Ghost Rider video, watch, clip, chapters", body=body, vid_pos="50% 50%")
