import re,html
def clean(t):
    t=re.sub(r'\[\[[^\]|]*\|([^\]]*)\]\]',r'\1',t)
    t=re.sub(r'\[\[([^\]]*)\]\]',r'\1',t)
    t=t.replace('\\|','|')
    t=html.escape(t,quote=False)
    t=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',t)
    t=re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?!\w)',r'<i>\1</i>',t)
    return t.strip()
def section(md,head,stop=r'^#{2,3} '):
    lines=md.split("\n"); out=[]; on=False
    for l in lines:
        if re.match(r'^## '+re.escape(head),l): on=True; continue
        if on and re.match(stop,l): break
        if on: out.append(l)
    return [l for l in out if l.strip() and not l.strip().startswith("---") and not l.startswith(">")]
def to_html(lines):
    # build nested lists by indent
    items=[]
    for l in lines:
        ind=len(l)-len(l.lstrip(" \t").replace("\t","    ")) if False else len(l.replace("\t","    "))-len(l.replace("\t","    ").lstrip())
        s=l.strip()
        m=re.match(r'^(\d+)\.\s+(.*)',s); b=re.match(r'^[-*]\s+(.*)',s)
        if m: items.append((ind//2 if ind<4 else ind//4,"ol",m.group(2)))
        elif b: items.append((ind//2 if ind<4 else ind//4,"ul",b.group(1)))
        else: items.append((None,"p",s))
    out=[];stack=[]
    for lvl,kind,txt in items:
        if kind=="p":
            while stack: out.append(f"</li></{stack.pop()[1]}>")
            out.append(f"<div>{clean(txt)}</div>"); continue
        while stack and stack[-1][0]>lvl: out.append(f"</li></{stack.pop()[1]}>")
        if stack and stack[-1][0]==lvl:
            out.append(f"</li><li>{clean(txt)}")
        else:
            stack.append((lvl,kind)); out.append(f"<{kind}><li>{clean(txt)}")
    while stack: out.append(f"</li></{stack.pop()[1]}>")
    return "".join(out)
