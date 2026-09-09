"""Small markup helpers shared by page modules."""

def hero(title, lede, crumbs_html, kicker="", align="", short=False, cta="", cue=True, wide=False):
    cls = "hero" + (" short" if short else "") + (f" align-{align}" if align else "")
    k = f'<p class="kicker">{kicker}</p>' if kicker else ""
    c = f'<div class="hero-cta">{cta}</div>' if cta else ""
    q = '<div class="scroll-cue" aria-hidden="true">Scroll</div>' if cue else ""
    return f'<section class="{cls}">{crumbs_html}{k}<h1>{title}</h1><p class="lede{" wide" if wide else ""}">{lede}</p>{c}{q}</section>'

def plate(inner, cls=""):
    return f'<div class="plate {cls}">{inner}</div>'

def shout(headline, sub, plate_html, flip=False):
    return f'<section class="band"><div class="shout{" flip" if flip else ""} reveal"><div><h2>{headline}</h2><p class="sub">{sub}</p></div>{plate_html}</div></section>'

def band(inner, cls=""):
    return f'<section class="band {cls}"><div class="reveal">{inner}</div></section>'

def drift(text, cite="", right=False):
    return f'<section class="band"><blockquote class="drift{" right" if right else ""} reveal">{text}{f"<cite>{cite}</cite>" if cite else ""}</blockquote></section>'

def stats(items):
    return '<section class="band"><div class="stats reveal">' + "".join(f"<div><b>{b}</b><span>{s}</span></div>" for b, s in items) + "</div></section>"

def facts(pairs):
    return '<dl class="facts">' + "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in pairs) + "</dl>"

def p(*paras):
    return "".join(f"<p>{x}</p>" for x in paras)
