from ._h import *
from build import crumbs, related

def page():
    s = "quotes"
    body = hero("QUOTES", "The words that ride with the Spirit. Short by design — the Rider does not make speeches — with the context that makes each one land.", crumbs(s), kicker="Words of vengeance", align="center", cue=False, short=True)
    W = []
    def q(text, src, ctx):
        W.append(f'<div class="q reveal"><p>“{text}”</p><div class="src">{src}</div><p class="ctx">{ctx}</p></div>')
    q("Look into my eyes.", "The Penance Stare · every host since 1990", "The command that precedes judgement. It is the closest thing the Rider has to a catchphrase, and it has been spoken by Ketch, Blaze and Reyes and delivered on screen by Nicolas Cage.")
    q("Your soul is stained by the blood of the innocent.", "Ghost Rider (2007)", "The film's phrasing of the Stare's verdict — the Rider names the crime before returning its weight.")
    q("Vengeance.", "The one-word answer", "When asked what he is, what he wants or why he has come, the Rider has given this answer in dozens of issues. Everything else is detail.")
    q("Innocent blood has been spilled.", "Ghost Rider vol. 3 · 1990", "The sentence that summoned the Ketch Rider. It states the rule of the character in six words: the Spirit answers blood, not prayers.")
    q("Bro, let's ride.", "Shawn Levy, San Diego Comic-Con 2026", "The director's account of how he and Ryan Gosling decided to make the 2028 film, told from the Hall H stage.")
    q("This is a character I've wanted to play for a very long time.", "Ryan Gosling, Hall H, July 2026", "Gosling's first words to the crowd after Kevin Feige introduced him as Johnny Blaze.")
    q("Eli was never a Spirit of Vengeance. He was a man who liked killing.", "Paraphrase of Robbie Reyes's realisation", "The turn that separates Robbie's story from every other Rider's: the voice offering power was lying about what it was.")
    q("Hell keeps every receipt.", "This site's summary of the curse", "Not a comic line — a description of why the Rider exists: Mephisto's bargains are always honoured and never fair.")
    body += '<section class="band"><div class="wall">' + "".join(W) + "</div></section>"
    body += related(["powers", "movies", "news", "lore"])
    return dict(slug=s, title="Quotes", desc="Ghost Rider quotes and catchphrases: the Penance Stare, 'Vengeance', 'Innocent blood has been spilled', and words from the 2028 film announcement.", keywords="Ghost Rider quotes, look into my eyes, penance stare quote, vengeance", body=body, vid_pos="50% 50%")
