import genanki
from dgh_common import BASIC
W="Alfa Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliett Kilo Lima Mike November Oscar Papa Quebec Romeo Sierra Tango Uniform Victor Whiskey X-ray Yankee Zulu".split()
deck=genanki.Deck(1739281115,"DGH::NATO-alfabet")
g=lambda k: genanki.guid_for("NATO",k)
for w in W:
    L=w[0]
    deck.add_note(genanki.Note(model=BASIC,fields=[f"NATO-alfabet: <b>{L}</b>",w,""],tags=["NATO","NATO::letter"],guid=g(f"l_{L}")))
for word in ["MUG","PIT","AED","SMUR","GCS","ABCDE"]:
    deck.add_note(genanki.Note(model=BASIC,fields=[f"Spel <b>{word}</b> in het NATO-alfabet",
        " – ".join(W[ord(c)-65] for c in word),""],tags=["NATO","NATO::spellen"],guid=g(f"s_{word}")))
if __name__=="__main__":
    genanki.Package(deck).write_to_file("../content/Source/Anki/DGH_NATO_alfabet.apkg")
    print("notes",len(deck.notes))
