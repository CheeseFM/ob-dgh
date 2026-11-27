import sys,glob,os,re,genanki; sys.path.insert(0,".")
from dgh_common import *
from mdparse import *
D="../content/Wiki/Staande Orders/"
U=lambda *x: ul(*x)
# extra kaartjes per SO: ("c",key,tekst,extra) of ("b",key,vraag,antwoord,extra)
X={
"O01":[("c","malinas","O01: Malinas-score kleiner dan {{c1::5}}: vervoer naar het ziekenhuis, patiënte op de {{c2::linkerzijde}} in stabiele zijligging.",""),
       ("c","malinas5","O01: Malinas-score {{c1::5 of meer}}: MUG/PIT, patiënte {{c2::omgekeerd op de brancard}} installeren, parameters opvolgen.",""),
       ("b","malinas_items","Welke 5 elementen scoort de Malinas-score (O01)?",U("Aantal zwangerschappen","Duur van de arbeid","Duur van de contracties","Interval tussen de contracties","Vruchtwaterverlies"),"Elk 0–2 punten."),
       ("b","specifiek","Wat zegt O01 bij een stuitligging en bij een uitzakking van de navelstreng?","<b>Stuitligging</b>: niet aankomen, 'laten doen'<br><b>Uitzakking navelstreng</b>: moeder in <b>Trendelenburg</b>",""),
       ("b","placenta","Wat doe je volgens O01 met de baarmoeder, navelstreng en placenta?","Baarmoeder <b>niet stimuleren</b>, <b>niet aan de navelstreng trekken</b>; de placenta opvangen en <b>meenemen</b> naar het ziekenhuis",""),
       ("b","kind","Zorg voor het kind volgens O01?",U("<b>Afdrogen</b> en inwikkelen (muts en deken), warm houden","ABC, zo nodig CPR (O21)","Navelstreng afklemmen","Baby op de buik van de moeder"),"")],
"O02":[("b","volgorde","O02: wanneer immobiliseer je?","<b>Immobilisatie</b>, zo nodig <b>na pijnstilling door de MUG/PIT</b>",""),
       ("c","pijnscore","O02: pijnscore {{c1::4 tot 7}}: zelf immobiliseren, voorzichtig vervoer. Pijnscore {{c2::> 7}}: MUG/PIT en infuusmateriaal voorzien.","")],
"O03":[],
"O04":[("c","tlo","O04: MUG/PIT zeker bij een TLO ≥ {{c1::15 %}} (volwassene), ≥ {{c2::10 %}} (kind of oudere), of &gt; {{c3::5 %}} derdegraads.",""),
       ("b","criteria","Welke andere criteria uit O04 vragen zeker MUG/PIT?",U("Verbranding van <b>aangezicht, hals, luchtwegen</b> (inhalatie) of <b>genitaliën</b>","<b>Shock</b>","<b>Elektrische</b> verbranding","<b>Hevige pijn</b>"),""),
       ("c","koelen","O04: koel met helder, stromend {{c1::lauw}} water op {{c2::15 cm}}, tot {{c3::de pijn weg is}}.",""),
       ("c","wallace","O04: de TLO schat je in met de regel van {{c1::Wallace}} of met {{c2::de handpalm van de patiënt}}.","Handpalm ≈ 1 %"),
       ("c","vervoer","O04 voor vervoer: bedek met brandwondenmateriaal of (natte) steriele kompressen en wikkel de patiënt in een {{c1::isothermische deken}}.","")],
"O05":[("c","hypotensie","O05: hypotensie = bovendruk &lt; {{c1::90}} mmHg.",""),
       ("b","symptomen","Welke symptomen van hypovolemische shock noemt O05?",U("Bovendruk &lt; 90 mmHg","Tachycardie, tachypneu","Bleek, cyanose, gemarmerde huid","Capillaire refill &gt; 2 s"),""),
       ("c","houding","O05: positioneer de patiënt in {{c1::ruglig}}, zo mogelijk in {{c2::Trendelenburg}}.",""),
       ("c","o2","O05: geef {{c1::100 %}} O₂.",""),
       ("c","o28","Hartfrequentie &lt; {{c1::50}}/min of &gt; {{c2::150}}/min → staande order {{c3::O28}}.","Staat in O05, O08, O25, O26.")],
"O06":[("b","ernst","Wat zijn de ernstcriteria van O06 (convulsies volwassene)?",U("Status epilepticus","Niet terugkeren van het bewustzijn","Geassocieerd schedeltrauma"),""),
       ("b","oorzaken","Welke oorzaken vraag je na bij convulsies (O06)?",U("Gekende epilepsie, behandeling","Alcoholisme","Diabetes","(CO-)vergiftiging","CVA","Trauma"),"")],
"O07":[("b","ernst","Wat zijn de ernstcriteria van O07 (convulsies kind)?",U("Status epilepticus","<b>Petechiën</b> (denk aan meningokokken-meningitis)","Geassocieerd schedeltrauma"),""),
       ("c","o2","O07: bij een kind met convulsies geef je {{c1::100 %}} O₂.",""),
       ("c","koorts","O07: bij een temperatuur &gt; {{c1::38,5 °C}}: kind {{c2::uitkleden}} en weinig toedekken tijdens transport.","")],
"O08":[("b","inuit","Wat zoek je bij elektrocutie specifiek op (O08)?","Het punt waar de elektriciteit het lichaam is <b>binnengekomen</b> en <b>buitengegaan</b>",""),
       ("b","info","Welke info vraag je na bij een elektrische schok (O08)?","<b>Wisselstroom of gelijkstroom</b>, <b>spanning / stroomsterkte</b>",""),
       ("b","aandacht","Waar let je extra op bij O08?",U("Raak de patiënt <b>niet aan</b> zolang hij gekoppeld is aan de stroombron","Zichtbare letsels zijn het <b>topje van de ijsberg</b>","Kan een polytrauma geven","Ga uit van het ergste"),"Met hartstilstand spreekt men van elektrocutie."),
       ("c","halskraag","O08: bij de eerste evaluatie: ABC en {{c1::halskraag}}, zo nodig CPR.","")],
"O09":[("b","fixatie","Wanneer mag je volgens O09 fixeren?","Fixatie <b>vermijden</b>, tenzij noodzakelijk om hulpverleners, patiënt en/of omgeving te <b>beschermen</b>",""),
       ("b","eerst","Wat doe je eerst bij agitatie (O09)?",U("<b>Veiligheid</b> (zo nodig politie)","ABC + <b>capillaire glycemie</b>","Info: trauma, medicatie/toxische stoffen, ontwenning, diabetes, temperatuur","<b>Dialoog</b> om escalatie te voorkomen"),"Blijft de agitatie: MUG/PIT.")],
"O10":[("c","temp","O10: hyperthermie met een temperatuur ≥ {{c1::40 °C}}; de huid stopt met {{c2::zweten}} en is droog.",""),
       ("b","ijs","Mag je bij hyperthermie zelf met ijs koelen (O10)?","Enkel op (mondeling) <b>voorschrift van de MUG/PIT</b>: in vochtige doeken wikkelen, ijs in hals, oksels en liesplooien",""),
       ("b","symptomen","Welke symptomen van hyperthermie noemt O10?","<b>Neurologisch</b>: geïrriteerd, agressief, gedesoriënteerd, epilepsie, coma<br><b>Circulatoir</b>: shock met tachycardie<br><b>Respiratoir</b>: hyperventilatie<br><b>Huid</b>: droog, stopt met zweten, ≥ 40 °C","")],
"O11":[("c","grens","O11: hypoglycemie bij een capillaire glycemie &lt; {{c1::60}} mg/dl.",""),
       ("b","bewust","Hypo zonder bewustzijnsstoornissen (O11): wat doe je?","<b>Snelle</b> (cola, suiker) en <b>trage</b> suikers (brood) per os, behandelende arts contacteren, zo nodig MUG/PIT",""),
       ("b","bewusteloos","Hypo met bewustzijnsstoornissen (O11): wat doe je?","<b>MUG/PIT</b>; bewusteloos: luchtwegmanagement; ademt: stabiele zijligging","")],
"O12":[("c","def","O12: hypothermie = lichaamstemperatuur &lt; {{c1::35 °C}}.",""),
       ("b","mobilisatie","Waar let je vooral op bij het verplaatsen van een onderkoelde patiënt (O12)?","<b>Uiterst voorzichtige mobilisatie</b> (glijdend, horizontaal)",""),
       ("b","opwarmen","Hoe warm je op volgens de ernst (O12)?","<b>Mild</b> (&gt; 32 °C): passief<br><b>Ernstig</b> (28–32 °C): passief, minimale mobilisatie, glijdend horizontaal vervoer<br><b>Zeer ernstig</b> (&lt; 28 °C): actief (instructies MUG/PIT)","Hartstilstand bij ernstige hypothermie: evacuatie onder CPR."),
       ("b","nat","Een onderkoelde patiënt is nat. Wat doe je (O12)?","<b>Volledig uitkleden en afdrogen</b>, warme omgeving + isothermische deken (passieve opwarming)","")],
"O13":[("c","o2","O13: geef O₂ tot SpO₂ {{c1::94 à 98 %}}; bij COPD {{c2::88 – 92 %}}.",""),
       ("c","glyc","O13: bepaal de capillaire glycemie; bij &lt; {{c1::60}} mg/dl → {{c2::O11}}.",""),
       ("b","niet","Wanneer gebruik je O13 niet (wanneer een andere staande order)?","Als de bewustzijnsverandering komt door <b>CO</b> (O16), <b>hypoglycemie</b> (O11) of <b>hypoxie</b> (O14/O15)",""),
       ("b","wapa","Wat doe je volgens O13 bij elk niveau van WAPA?","<b>W</b>: vervoer ziekenhuis<br><b>A</b>: overweeg MUG/PIT, stabiele zijligging<br><b>P</b>: MUG/PIT<br><b>A</b> (areactief): MUG, luchtwegmanagement, intubatie voorbereiden","")],
"O14":[("c","af","O14: ademnood met o.a. een ademhalingsfrequentie &gt; {{c1::30}}/min.",""),
       ("b","ernst","Wat zijn de ernstcriteria van O14 (ademnood volwassene)?",U("Tachypneu","Moeilijk zinnen afmaken","Cyanose","Agitatie"),""),
       ("b","maatregelen","Wat doe je bij acute ademnood bij een volwassene (O14)?",U("<b>Halfzittend of zittend</b>, loszittende tandprothese verwijderen","Luchtweg vrij van vreemde voorwerpen?","<b>100 % O₂</b>","Overweeg MUG/PIT","Aerosol enkel na akkoord van de arts (mondeling voorschrift)"),"")],
"O15":[("b","aspiratie","Wat zegt O15 over aspiratie bij een kind?","Aspiratie <b>vermijden</b> indien niet strikt noodzakelijk",""),
       ("b","uitputting","Kind met ademnood raakt uitgeput of stopt met ademen (O15). Wat doe je?","<b>Ventilatie met de ballon</b>, luchtwegmanagement voorbereiden",""),
       ("c","o2","O15: kind met ademnood: {{c1::halfzittend}}, geruststellen en {{c2::100 %}} O₂.","")],
"O16":[("b","mug","Wanneer vraag je zeker de MUG bij CO/brandrook (O16)?",U("<b>Agitatie</b> (mogelijke cyanide-intoxicatie)","<b>Roet</b> in gelaat/mond, verbrande neusharen","Bewustzijnsverlies","Aantasting van de vitale functies"),""),
       ("b","o2","Wanneer en hoe geef je O₂ bij CO (O16)?","Via een <b>non-rebreathing masker (15 L/min)</b> bij hoofdpijn, pijn op de borst, misselijkheid, braken, syncope of veranderd bewustzijn",""),
       ("b","veiligheid","Wat is de eerste maatregel bij een vermoeden van CO (O16)?","<b>Iedereen uit het gebouw</b>, maar zorg dat je nadien iedereen kan evalueren","")],
"O17":[("b","def","Wat is het verschil tussen immersie en submersie (O17)?","<b>Immersie</b>: hoofd bleef boven water<br><b>Submersie</b>: hoofd is onder water geweest",""),
       ("c","horizontaal","O17: evacueer een drenkeling altijd {{c1::horizontaal}}.","Bij duikongeval: as hoofd-hals-lichaam vrijwaren."),
       ("c","zh","O17: elke patiënt van (bijna-)verdrinking, zelfs {{c1::asymptomatisch}}, gaat naar het ziekenhuis.",""),
       ("b","ondiep","Wat neem je aan bij elke drenkeling in ondiep water (O17)?","Mogelijk een <b>wervelkolomtrauma</b> en <b>onderkoeld</b>, tot het tegendeel bewezen is","")],
"O18":[("c","criteria","O18 (MIP): bij {{c1::5}} zwaargewonden, {{c2::10}} gewonden met onbepaalde ernst of {{c3::20}} personen in gevaar.",""),
       ("c","uitruk","O18: standaard basisuitruk bij een MIP: {{c1::3}} MUG, {{c2::5}} ambulances en SIM.",""),
       ("b","afkondigen","Op wiens vraag kondigt het HC 112 het MIP af (O18)?",U("(Adjunct-)gezondheidsinspecteur","(Adjunct-)DIR-MED","De eerste MUG-equipe ter plaatse","Een officier van een andere discipline"),""),
       ("b","mettag","Wat betekenen T1, T2 en T3 (METTAG, O18)?","<b>T1</b>: absolute urgentie, onmiddellijke vitale handelingen<br><b>T2</b>: relatieve urgentie, stabilisatie<br><b>T3</b>: lichte zorg, zittend vervoer",""),
       ("b","onderweg","Wat doe je op weg naar een rampsituatie (O18)?",U("Aanrijroute en <b>punt eerste bestemming (PEB)</b> vragen","Orders van de DIR-MED volgen","Communicatie op de rampgespreksgroep <b>beperken</b>"),"Informatie verzamelen gaat voor op meteen in actie schieten.")],
"O19":[("b","quincke_anafylaxie","Wat is het verschil tussen Quincke-oedeem en anafylactische shock (O19)?","<b>Quincke</b>: oedeem <b>zonder jeuk</b> in aangezicht/hals, gezwollen tong, snel toenemende luchtwegobstructie<br><b>Anafylaxie</b>: warmte, <b>jeuk</b>, netelroos, tachycardie, hypotensie, gezwollen keel, bronchospasme",""),
       ("b","mayo","Mag je bij Quincke/anafylaxie een mayocanule plaatsen (O19)?","<b>Nooit</b>",""),
       ("b","autoinjector","Wat zegt O19 over de adrenaline-autoinjector?","Als de patiënt er een heeft: <b>toedienen na contact en akkoord van de arts/MUG</b> (mondeling voorschrift)","De lesslides zeggen: (voorlopig) geen toegelaten handeling voor de HVA."),
       ("c","o2","O19: geef {{c1::100 %}} O₂ en voorzie {{c2::infuusmateriaal}}.","")],
"O20":[("b","positie","Hoe positioneer je de patiënt voor CPR (O20/O21)?","In <b>ruglig op een harde, vlakke ondergrond</b>",""),
       ("b","aed","Wanneer leg je de AED aan (O20)?","<b>Zo snel mogelijk</b>, en volg de instructies","Kind (O21): zo mogelijk in pediatrische modus.")],
"O21":[("c","aed","O21: leg zo snel mogelijk de AED aan, zo mogelijk in {{c1::pediatrische modus}}.","")],
"O24":[("c","o2","O24: geef O₂ tot SpO₂ {{c1::94 à 98 %}}.",""),
       ("b","bd","Hoe meet je de bloeddruk bij pijn op de borst (O24)?","Aan <b>beide armen</b>",""),
       ("b","houding","Welke houding bij pijn op de borst (O24)?","<b>Halfzittend</b> + geruststellen",""),
       ("b","info","Met welke vraagmethodes win je info in bij pijn op de borst (O24)?","<b>S-AMPLE</b> en <b>PQRST</b>","")],
"O25":[("b","ernst","Welke indirecte ernstcriteria noemt O25 bij zwaar trauma?",U("Vitale parameters","Anatomie van de letsels","Ongevalsmechanisme","Overige criteria"),""),
       ("b","bloeding","Hoe stelp je bloedingen volgens O25/O26/O27?","<b>Directe druk</b>, <b>indirecte druk</b> en zo nodig een <b>knevel</b>",""),
       ("c","o2","O25: bij zwaar trauma geef je {{c1::100 %}} O₂.",""),
       ("b","immobilisatie","Waarmee immobiliseer je bij zwaar trauma (O25)?","Spalken, spine board, schepbrancard, vacuümmatras, zo nodig <b>na pijnstilling</b> door de MUG/PIT","")],
"O26":[("b","deel","Wat doe je met het geamputeerde lichaamsdeel (O26)?","Op gepaste wijze <b>bewaren en meenemen</b> naar het ziekenhuis","")],
"O27":[],
"O28":[("c","def","O28: ritmestoornis = hartfrequentie &lt; {{c1::50}}/min of &gt; {{c2::150}}/min, slecht verdragen (ABC instabiel).",""),
       ("c","o2","O28: geef O₂ tot SpO₂ {{c1::94 à 98 %}}.","")],
"O29":[("b","def","Voor welke patiënt gebruik je O29 (CVA)?","Elke patiënt met een <b>spraakstoornis</b> en/of <b>minder gevoel of kracht</b>, plots of bij het wakker worden",""),
       ("b","stappen","Welke specifieke stappen neemt O29 bij een CVA?",U("<b>FAST-test</b>","<b>Glycemie</b> bepalen","ABC stabiel: ziekenhuis <b>verwittigen</b> en vervoeren","ABC instabiel: MUG/PIT","<b>(Half)zittende</b> houding","O₂ tot SpO₂ 94–98 %"),""),
       ("b","info","Welke info vraag je zeker na bij een CVA (O29)?","Vooral het <b>aanvangsuur</b> en de duur, waar het merkbaar is, voorgeschiedenis, medicatie","")],
}
deck=genanki.Deck(1739281113,"DGH::Staande orders")
n=0
for f in sorted(glob.glob(D+"O*.md")):
    code=os.path.basename(f)[:3]; title=os.path.basename(f)[4:-3]
    md=open(f).read(); tags=["SO",f"SO::{code}"]
    g=lambda k: genanki.guid_for("SO",f"{code}_{k}")
    wanneer=to_html(section(md,"Voor gebruik bij"))
    deck.add_note(genanki.Note(model=BASIC,fields=[f"Voor welke patiënt gebruik je staande order <b>{code}</b>?",wanneer,f"{code} {title}"],tags=tags,guid=g("wanneer"))); n+=1
    alg=to_html(section(md,"Algemene maatregelen"))
    if alg:
        deck.add_note(genanki.Note(model=BASIC,fields=[f"Wat zijn de algemene maatregelen van <b>{code} {title}</b>?",alg,""],tags=tags,guid=g("algemeen"))); n+=1
    for c in X.get(code,[]):
        if c[0]=="c": deck.add_note(genanki.Note(model=CLOZE,fields=[c[2],c[3]],tags=tags,guid=g(c[1])))
        else: deck.add_note(genanki.Note(model=BASIC,fields=[c[2],c[3],c[4]],tags=tags,guid=g(c[1])))
        n+=1
genanki.Package(deck).write_to_file("../content/Source/Anki/DGH_Staande_orders.apkg")
print("notes",n)
