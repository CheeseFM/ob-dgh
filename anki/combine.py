import sys,glob,genanki; sys.path.insert(0,".")
import dgh_common
decks=[];media=[]
def capture(N,title,short,cards,med,out_dir):
    deck=genanki.Deck(1739281100+N,f"DGH::H{N} {title}")
    for c in cards:
        g=genanki.guid_for(f"H{N}",c[1])
        if c[0]=="b": deck.add_note(genanki.Note(model=dgh_common.BASIC,fields=[c[2],c[3],c[4]],tags=c[5],guid=g))
        else: deck.add_note(genanki.Note(model=dgh_common.CLOZE,fields=[c[2],c[3]],tags=c[4],guid=g))
    decks.append(deck); media.extend(med); return None,len(cards)
dgh_common.build=capture
for n in range(1,13):
    src=open(f"h{n}.py").read().replace("from dgh_common import *","from dgh_common import *\nbuild=__CAP__")
    src=src.replace("print(out,n)","")
    exec(compile(src,f"h{n}.py","exec"),{"__CAP__":capture,"__name__":"x"})
for extra in ["so.py","proc.py","nato.py"]:
    gl={"__name__":"x"}
    src=open(extra).read().replace("genanki.Package(deck).write_to_file","(lambda *a,**k:None)(deck) or (lambda p: None)")
    exec(compile(src,extra,"exec"),gl)
    decks.append(gl["deck"])
p=genanki.Package(decks); p.media_files=sorted(set(media))
p.write_to_file("../content/Source/Anki/DGH_Alle_hoofdstukken.apkg")
print(len(decks),"decks",sum(len(d.notes) for d in decks),"notes",len(set(media)),"media")
