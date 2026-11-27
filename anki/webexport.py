import re,json,genanki,sys; sys.path.insert(0,".")
# hergebruik combine.py-logica zonder te schrijven
src=open("combine.py").read().split("p=genanki.Package(decks)")[0]
g={"__name__":"x"}; exec(compile(src,"combine.py","exec"),g)
decks=g["decks"]
IMG=re.compile(r'<img[^>]*>',re.I)
import os,glob
from PIL import Image
MEDIA={os.path.basename(p):p for p in glob.glob("h*media/*")}
used=set()
def img(m):
    t=m.group(0); src=re.search(r'src="([^"]+)"',t)
    if not src or src.group(1) not in MEDIA: return ""
    n=src.group(1); used.add(n)
    return f'<img src="media/{os.path.splitext(n)[0]}.webp" alt="">'
def clean(s): 
    s=IMG.sub(img,s or ""); s=re.sub(r'(<br\s*/?>\s*){2,}','<br>',s).strip()
    return re.sub(r'^(<br\s*/?>)+|(<br\s*/?>)+$','',s).strip()
CL=re.compile(r'\{\{c(\d+)::(.*?)(?:::(.*?))?\}\}',re.S)
out=[];skipped=0
for d in decks:
    name=d.name.split("::",1)[1]
    for n in d.notes:
        tags=n.tags
        if n.model.model_id==1739281002:
            text,extra=clean(n.fields[0]),clean(n.fields[1])
            for k in sorted({m.group(1) for m in CL.finditer(text)},key=int):
                q=CL.sub(lambda m:(f'<span class="cz">[{m.group(3) or "…"}]</span>' if m.group(1)==k else m.group(2)),text)
                a=CL.sub(lambda m:(f'<span class="cz">{m.group(2)}</span>' if m.group(1)==k else m.group(2)),text)
                out.append({"d":name,"t":tags,"q":q,"a":a,"x":extra,"id":f"{n.guid}_{k}"})
        else:
            q,a,x=(clean(f) for f in n.fields)
            if not re.sub(r'<[^>]+>','',q).strip() or not re.sub(r'<[^>]+>','',a).strip(): skipped+=1; continue
            out.append({"d":name,"t":tags,"q":q,"a":a,"x":x,"id":n.guid})
dest=sys.argv[1] if len(sys.argv)>1 else "../content/Source/Oefenen/kaartjes.json"
md=os.path.join(os.path.dirname(dest),"media"); os.makedirs(md,exist_ok=True)
keep={os.path.splitext(u)[0] for u in used}
for f in glob.glob(md+"/*.webp"):
    if os.path.basename(f)[:-5] not in keep: os.remove(f)
for u in used:
    im=Image.open(MEDIA[u]); im=im.convert("RGBA" if im.mode in ("RGBA","LA","P") else "RGB")
    im.thumbnail((1000,1000)); im.save(md+"/"+os.path.splitext(u)[0]+".webp","WEBP",quality=80)
json.dump({"decks":[d.name.split("::",1)[1] for d in decks],"cards":out},open(dest,"w"),ensure_ascii=False,separators=(",",":"))
print(len(out),"kaartjes,",len(used),"fotos, overgeslagen:",skipped)
