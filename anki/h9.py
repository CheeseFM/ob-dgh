import sys,glob; sys.path.insert(0,".")
from dgh_common import *
T=lambda *x:["H9"]+[f"H9::{t}" for t in x]
I=lambda f:f'<img src="dgh_h9_e_{f}.png">'
cards=[
# Brandwonden
("b","bw_wie","Wie zijn de meest getroffen slachtoffers van brandwonden?","<b>Jonge kinderen</b> (0–4 jaar, vaak vloeistoffen) en <b>ouderen</b> (> 60 jaar, vaak woningbrand)","70 % gebeurt in en om het huis.",T("brandwonden")),
("b","bwc","Wat is een BWC en hoe wordt de capaciteit verdeeld?","<b>Brandwondencentrum</b>; capaciteit via het <b>BABI-plan</b>","",T("brandwonden")),
("b","huid_functies","Wat zijn de functies van de huid?",ul("Bescherming","Gevoel / pijn","Temperatuurregeling"),"",T("brandwonden")),
("b","bw_ernst","Welke factoren bepalen de ernst van een brandwonde?",ul("<b>Oorzaak</b>","<b>Diepte</b> (graad)","<b>Oppervlakte</b>","<b>Plaats</b> op het lichaam","<b>Leeftijd</b>"),"Slides noemen ook: contactduur, toestand SO, andere letsels, tijd tot hulp.",T("brandwonden","ernst")),
("b","bw_oorzaken","Welke 4 soorten oorzaken van brandwonden zijn er?",ul("<b>Thermisch</b> (vuur, heet water, explosie)","<b>Chemisch</b>","<b>Radiogeen</b> (zon, straling)","<b>Elektrisch</b>"),"",T("brandwonden","ernst")),
("b","graad1","Hoe herken je een 1e graadsbrandwonde?","<b>Rood</b>, pijn, zwelling (vochtverlies)","Doel: pijn bestrijden.",T("brandwonden","graden")),
("b","graad2","Hoe herken je een 2e graadsbrandwonde?","Pijn, zwelling, <b>blaren</b>, vochtverlies","Doel: pijn bestrijden, uitbreiding en besmetting voorkomen.",T("brandwonden","graden")),
("b","graad3","Hoe herken je een 3e graadsbrandwonde?","<b>Zwart, wit of perkamentachtig</b>, stug; <b>geen pijn</b> (zenuwen weg), rondom 1e en 2e graad","",T("brandwonden","graden")),
("b","wallace_volw",I("wallace_volw")+"<br>Hoe schat je de verbrande oppervlakte bij een volwassene?","<b>Regel van Wallace (regel van 9)</b>: hoofd 9 %, elke arm 9 %, romp voor 18 %, romp achter 18 %, elk been 18 %, genitaliën 1 %","Klein of verspreid: <b>handpalm van de patiënt ≈ 1 %</b>.",T("brandwonden","oppervlakte","foto")),
("b","wallace_kind",I("wallace_kind")+"<br>Wat is anders aan de regel van 9 bij een baby?","Het <b>hoofd</b> telt zwaarder (<b>18 %</b>), de benen minder (± 14 %)","",T("brandwonden","oppervlakte","foto")),
("b","bw_licht_ernstig","Wanneer is een brandwonde licht en wanneer ernstig?","<b>Licht</b>: 1e graad en kleine 2e graad<br><b>Ernstig</b>: 2e graad groter dan een 2-euromunt, tot 10–15 %","",T("brandwonden","ernst")),
("b","bw_levensbedreigend","Wanneer is een brandwonde levensbedreigend (MUG/PIT)?",ul("TLO <b>≥ 15 %</b> (volwassene) of <b>≥ 10 %</b> (kind, oudere)","<b>> 5 %</b> derdegraads","Aangezicht, hals, <b>luchtwegen</b> (verschroeide neusharen), genitaliën","3e graad aan handen, voeten, gelaat","CO-vergiftiging, letsels door drukgolf","<b>Chemische of elektrische</b> verbranding","Shock, hevige pijn"),"Staande order O04",T("brandwonden","ernst")),
("b","bw_eerst","Wat is de eerste regel bij het handelen bij brandwonden (na veiligheid)?","<b>Eerst water, de rest komt later</b>","Doof de vlammen; laat het SO liggen (vlammen en rook niet naar het gezicht).",T("brandwonden","handelen")),
("b","bw_koelen","Hoe koel je een brandwonde?","<b>Praktijk</b>: 20/20/20 → <b>20 min</b>, water van <b>20 °C</b>, op <b>20 cm</b><br><b>Staande order O04</b>: helder, stromend <b>lauw</b> water op <b>15 cm</b>, tot de pijn weg is","Let op hypothermie. Bescherm jezelf bij chemische brandwonden.",T("brandwonden","handelen","notas")),
("b","bw_juwelen","Wat doe je met kledij en juwelen bij brandwonden?","<b>Verwijderen</b>, tenzij ze <b>vastkleven</b> aan de wonde","",T("brandwonden","handelen")),
("b","bw_vervoer","Hoe bereid je een brandwondenpatiënt voor op vervoer?",ul("<b>Vochtige steriele kompressen</b> of brandwondenverband — <b>geen ijs</b>","Wikkelen in een <b>isothermische deken</b>","Sanitaire cel <b>verwarmen</b> (onderkoeling!)","Halfzittend; bij shock: liggend met benen omhoog"),"",T("brandwonden","handelen")),
("b","bw_o2","Hoeveel zuurstof geef je bij brandwonden?","Volgens de <b>saturatie</b>; luchtweg vrijhouden (zeker bij inhalatie en brandwonden in het gelaat)","",T("brandwonden","handelen")),
("b","bw_briefing","Welke extra info geef je door bij brandwonden?",ul("Soort brand en materiaal","Ontploffing?","In een <b>gesloten ruimte</b>?","Hoe lang in de brand?","Tijd tussen bevrijding en aankomst ziekenhuis"),"",T("brandwonden")),
("b","alu_deken","Hoe leg je een aluminium deken aan?","<ol><li>Knoop in een hoek</li><li>Patiënt rechtzetten (of deken eronder via logroll)</li><li>Door de achterkant van de kledij</li><li>Door de voorkant</li><li>Soort 'pamper' maken</li></ol>","",T("brandwonden","notas")),
("b","bevriezing","Hoe herken je bevriezing en wat doe je?","Vooral aan de <b>extremiteiten</b>: eerst rood, dan <b>wit/wasachtig</b> → gangreen<br>Handelen: steriel afdekken, <b>geen snelle opwarming</b>, naar spoed","",T("koude","slides")),
# Elektriciteit
("b","elektrocutie","Wat is het verschil tussen elektrisering en elektrocutie?","<b>Elektrisering</b>: overleefd elektriciteitsongeval<br><b>Elektrocutie</b>: met <b>hartstilstand</b> / overlijden","",T("elektriciteit")),
("b","elek_impact","Waarvan hangt de ernst van een elektriciteitsongeval af?",ul("<b>Afgelegde weg</b> (door het hart? hand-hand, hand-voet)","<b>Stroomsterkte</b>","<b>Duurtijd</b>"),"",T("elektriciteit")),
("b","stroomsterkte",I("stroom")+"<br>Wat gebeurt er bij welke stroomsterkte?",ul("<b>0,5 mA</b>: voelbaar","<b>10 mA</b>: spierverkramping","<b>40 mA</b>: brandwonden, ademhalingsproblemen","<b>80 mA</b>: ernstige brandwonden, ritmestoornis","<b>1 A</b>: hartstilstand"),"",T("elektriciteit","foto")),
("c","verliesstroom","Een verliesstroomschakelaar staat op {{c1::30 mA}} per kring en {{c2::300 mA}} voor de installatie.","Jaarlijks testen.",T("elektriciteit","slides")),
("b","elek_veiligheid","Wat is de eerste regel bij een elektriciteitsongeval?","<b>Raak de patiënt niet aan</b> zolang hij aan de stroombron 'gekoppeld' is → eerst de stroom uitschakelen","",T("elektriciteit")),
("b","elek_letsels","Waarom ga je bij een elektriciteitsongeval 'uit van het ergste'?","Zichtbare letsels zijn het <b>topje van de ijsberg</b>: inwendige letsels, breuken, wegslingeren (polytrauma), letsels kunnen later optreden","",T("elektriciteit")),
("b","elek_handelen","Wat doe je bij een elektriciteitsongeval (O08)?",ul("Veiligheid, ABC, zo nodig CPR","Ademhaling aanwezig: stabiele zijligging","<b>MUG/PIT</b>","Zoek het <b>in- en uitgangspunt</b>","Brandwonden: O04; convulsies: O06/O07"),"Hartfrequentie &lt; 50 of &gt; 150 → O28.",T("elektriciteit")),
("b","elek_radio","Wanneer update je de noodcentrale over de medische bijstand?",ul("Slachtoffer <b>verliest het bewustzijn</b>","Er wordt een <b>reanimatie</b> opgestart","(Actieve bevalling)"),"",T("elektriciteit","notas")),
# Verdrinking
("b","verdrinking_kern","Wat is het kernprobleem bij verdrinking?","Een <b>respiratoir</b> probleem: de circulatiestilstand is meestal een gevolg van <b>hypoxie</b>","",T("verdrinking")),
("b","verdrinking_evacuatie","Hoe haal je een drenkeling uit het water?","<b>Horizontaal</b> (rechtop: bloeddrukval en collaps); vermoeden duikongeval → as hoofd-hals-lichaam vrijwaren","",T("verdrinking","slides")),
("b","verdrinking_rea","Hoe reanimeer je een drenkeling?",ul("Start met <b>5 beademingen</b>","Wees bedacht op <b>braken</b> (aspiratie klaar)","<b>Langdurige</b> reanimatie (onderkoeld)","Natte kledij weg, toedekken"),"Geen verschil in aanpak tussen nat/droog of zout/zoet water.",T("verdrinking")),
("b","verdrinking_zh","Moet een drenkeling zonder klachten naar het ziekenhuis?","<b>Ja, altijd</b> (ook asymptomatisch)","O17",T("verdrinking","slides")),
("b","ondiep_water","Wat neem je aan bij een drenkeling in ondiep water?","Mogelijk <b>wervelkolomtrauma</b> en <b>onderkoeld</b>, tot het tegendeel bewezen is","",T("verdrinking","slides")),
("b","secundaire_verdrinking","Wat is secundaire verdrinking en wat zijn de symptomen?","Na een bijna-verdrinking lopen de longblaasjes <b>later</b> vol vocht<br>Symptomen: <b>vermoeidheid, hoesten, ademnood, braken met wit/roze schuim</b>, gedragsverandering","",T("verdrinking")),
# Koude
("b","afkoeling_reactie","Hoe reageert het lichaam op afkoeling?","Meer warmte maken: <b>rillen</b>, minder bloed naar de huid (bleek, koude extremiteiten), kippenvel","",T("koude")),
("b","hypothermie_def","Vanaf welke temperatuur spreek je van hypothermie?","<b>&lt; 35 °C</b>","",T("koude")),
("b","temp_veilig","Welke symptomen bij 37–35 °C ('veilig')?","Bleek, <b>beven</b>, koud, uitgeput, verward, gestoorde spraak, ademhaling en hart versneld","",T("koude")),
("b","temp_gevaar","Welke symptomen bij 34–30 °C ('gevaar')?","<b>Beven neemt af</b>, trage pols, ritmestoornissen, cyanose, stijve spieren, somnolent, <b>geen pijn</b>","",T("koude")),
("b","temp_levensgevaar","Welke symptomen bij 30–27 °C ('levensgevaar')?","<b>Bewusteloos</b>, wijde (reagerende) pupillen, trage ademhaling, ritmestoornissen tot hartstilstand, beeld van klinische dood","",T("koude")),
("b","afkoeling_handelen","Wat doe je bij onderkoeling?",ul("Stappenplan (eventueel langdurige reanimatie)","Natte kledij uit, <b>afdrogen</b>, isothermische deken (armen apart)","Sanitaire cel verwarmen (<b>passieve</b> opwarming)","<b>Uiterst voorzichtig</b> verplaatsen: glijdend, horizontaal, zonder schokken"),"",T("koude")),
("b","hypothermie_so","Hoe warm je op volgens de ernst van de hypothermie (O12)?","<b>> 32 °C</b>: passieve opwarming<br><b>28–32 °C</b>: passief, minimale mobilisatie, glijdend horizontaal vervoer<br><b>&lt; 28 °C</b>: actieve opwarming (op instructie MUG/PIT)","",T("koude","staande_orders")),
# Warmte
("b","warmte_risico","Wie loopt extra risico bij hitte?",ul("Bejaarden","Chronisch zieken","Mindervaliden","Kinderen en zuigelingen"),"",T("warmte")),
("b","zonnebrand","Wat doe je bij zonnebrand (met flauwte/hoofdpijn)?","<b>Schaduw</b>, flauwte en brandwonde behandelen, naar het ziekenhuis","",T("warmte")),
("b","warmtekrampen","Waardoor ontstaan warmtekrampen en wat doe je?","<b>Vocht- en zoutverlies</b> door zweten → schaduw, rust, naar het ziekenhuis","",T("warmte")),
("b","hitteberoerte","Hoe herken je een hitteberoerte?",ul("Hoge pols, snelle ademhaling, <b>wijde pupillen</b>","Misselijk, hoofdpijn, duizelig, spierkrampen","<b>Warme, droge, rode huid</b> (stopt met zweten)","Temperatuur ≥ 40 °C, verward/agressief, convulsies"),"",T("warmte")),
("b","hitteberoerte_handelen","Wat doe je bij een hitteberoerte?",ul("Stappenplan, MUG","O₂ zo nodig","<b>Koelte, schaduw, rust</b>","Afsponzen met water / vochtige doeken","Naar het ziekenhuis"),"Koelen met ijs enkel op (mondeling) voorschrift van de MUG/PIT (O10).",T("warmte","staande_orders")),
("b","hitte_uitputting","Wat is het verschil tussen hitte-uitputting en hitteberoerte?","<b>Uitputting</b>: 37–40 °C, hoofdpijn, braken, dorst, spierpijn → stop inspanning, drinken, koelen<br><b>Beroerte</b>: <b>> 40 °C</b> met <b>neurologische uitval</b> (insult, bewustzijnsverlies)","",T("warmte")),
# Straling
("b","straling","Waarvan hangt het effect van straling af?",ul("<b>Soort</b> straling (alfa, bèta, gamma)","<b>Duur</b> van blootstelling","<b>Sterkte</b>"),"Beschadigt vooral delende cellen; effect pas later merkbaar.",T("straling")),
("b","straling_handelen","Wat doe je bij een stralingsongeval in een ongecontroleerde omgeving?",ul("<b>Afstand</b> houden, blootstelling beperken","Benaderen <b>bovenwinds</b>, via de instructies van D1 en D4 (civiele bescherming, CBRN)","Beschermende kledij + handschoenen","ABC pas in een <b>veilige zone</b>","Besmette kledij in een plastic zak, SO in veiligheidsdeken","Ziekenhuis verwittigen"),"Gecontroleerde omgeving: aanwijzingen van de deskundigen volgen.",T("straling")),
("b","zones_straling",I("zones")+"<br>Wat stellen hot, warm en cold zone voor?","<b>Hot</b>: getroffen gebied<br><b>Warm</b>: verzamelpunt + decontaminatie (CBRN-zorg)<br><b>Cold</b>: overname door D2, veilig","",T("straling","foto")),
]
media=sorted(glob.glob("h9media/*.png"))
out,n=build(9,"Urgenties door omgevingsfactoren","Omgevingsfactoren",cards,media,"../content/Source/Anki")
print(out,n)
