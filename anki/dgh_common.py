import genanki
CSS = """.card{font-family:sans-serif;font-size:20px;text-align:center;color:#222;background:#fff}
img{max-width:95%;max-height:380px;border-radius:6px}
.extra{font-size:16px;color:#666;margin-top:12px}
ul,ol{text-align:left;display:inline-block}
.cloze{font-weight:bold;color:#1565c0}
.nightMode.card,.night_mode .card{background:#1e1e1e;color:#eee}
.nightMode .cloze,.night_mode .cloze{color:#64b5f6}
.nightMode .extra,.night_mode .extra{color:#aaa}"""
BASIC = genanki.Model(1739281001,'DGH Basic',
  fields=[{'name':'Vraag'},{'name':'Antwoord'},{'name':'Extra'}],
  templates=[{'name':'Kaart 1','qfmt':'{{Vraag}}',
   'afmt':'{{FrontSide}}<hr id="answer">{{Antwoord}}{{#Extra}}<div class="extra">{{Extra}}</div>{{/Extra}}'}],css=CSS)
CLOZE = genanki.Model(1739281002,'DGH Cloze',
  fields=[{'name':'Tekst'},{'name':'Extra'}],
  templates=[{'name':'Cloze','qfmt':'{{cloze:Tekst}}',
   'afmt':'{{cloze:Tekst}}{{#Extra}}<div class="extra">{{Extra}}</div>{{/Extra}}'}],
  css=CSS, model_type=genanki.Model.CLOZE)
def ul(*items): return "<ul>"+"".join(f"<li>{i}</li>" for i in items)+"</ul>"
def build(N, title, short, cards, media, out_dir):
    deck = genanki.Deck(1739281100+N, f"DGH::H{N} {title}")
    keys=set()
    for c in cards:
        kind,key=c[0],c[1]; assert key not in keys,key; keys.add(key)
        guid=genanki.guid_for(f"H{N}",key)
        if kind=="b":
            _,_,q,a,extra,tags=c; n=genanki.Note(model=BASIC,fields=[q,a,extra],tags=tags,guid=guid)
        else:
            _,_,t,extra,tags=c; n=genanki.Note(model=CLOZE,fields=[t,extra],tags=tags,guid=guid)
        deck.add_note(n)
    p=genanki.Package(deck); p.media_files=sorted(set(media))
    out=f"{out_dir}/DGH_H{N}_{short}.apkg"; p.write_to_file(out); return out,len(cards)
