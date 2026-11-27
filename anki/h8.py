import sys,glob; sys.path.insert(0,".")
from dgh_common import *
T=lambda *x:["H8"]+[f"H8::{t}" for t in x]
I=lambda f:f'<img src="{f}">'
cards=[
("b","organen","Noem de inwendige vrouwelijke geslachtsorganen (met vaktermen).",ul("Eierstokken (<b>ovaria</b>)","Eileiders (<b>tubae</b>)","Baarmoeder (<b>uterus</b>)","Baarmoederhals (<b>cervix</b>)","Schede / vagina"),I("dgh_h8_e_organen.png"),T("anatomie")),
("c","cyclus","Een natuurlijke menstruele cyclus duurt {{c1::28 dagen}}.","1e deel: slijmvlies verdikt + eicel rijpt; 2e deel: eisprong + eventueel innesteling. Geen innesteling → menstruatie.",T("anatomie")),
("b","trimesters","Hoe is een zwangerschap ingedeeld?","3 trimesters, <b>± 37–40 (41) weken</b>"+ul("1e trimester: <b>0–12</b> weken","2e trimester: <b>13–24</b> weken","3e trimester: <b>25–37 (41)</b> weken"),"",T("zwangerschap")),
("b","eerste_trimester","Waarom is het eerste trimester een gevoelige periode?","Het embryo (tot ± 8 weken, daarna foetus) is zeer <b>gevoelig voor straling en vergiftiging</b> (alcohol, CO, sigarettenrook)","",T("zwangerschap")),
("c","beweging","Bewegingen van de foetus zijn voelbaar vanaf ± {{c1::16}} weken.","",T("zwangerschap")),
("c","levensvatbaar","Een foetus is levensvatbaar vanaf ± {{c1::24}} weken.","Daarvoor ligt de focus op de zorg voor de moeder.",T("zwangerschap")),
("b","geboorte_waarden","Wat zijn de gemiddelde geboortewaarden van een voldragen baby?","Geboorte na <b>37–41 weken</b>, ± <b>3,5 kg</b>, ± <b>50 cm</b>","",T("zwangerschap")),
("b","prematuur","Wanneer is een baby prematuur en waar let je dan vooral op?","Geboren <b>vóór 37 weken</b> → vooral <b>afkoeling</b> voorkomen","&lt; 30 weken: extra risico.",T("zwangerschap")),
("b","placenta","Wat doet de placenta?","De <b>moederkoek</b>: voert O₂ en voedingsstoffen aan, voert CO₂ en afvalstoffen af → werkt als een <b>filter</b>","",T("geboorte")),
("b","navelstreng_bouw","Hoe is de navelstreng opgebouwd?","<b>2 arteriën en 1 vene</b>, omgeven door een geleiachtige stof","",T("geboorte")),
("b","vliezen","Is het breken van de vliezen altijd de start van de bevalling?","<b>Nee, niet altijd</b>: dat hangt af van de positie van de foetus","",T("geboorte")),
("b","fasen","Wat zijn de 3 fasen van een bevalling?","<ol><li><b>Ontsluitingsfase</b></li><li><b>Uitdrijvingsfase</b></li><li><b>Nageboorte</b></li></ol>","",T("fasen")),
("b","ontsluiting","Hoe verloopt de ontsluitingsfase?","Duurt ± <b>12 uur</b> (soms veel langer); weeën eerst om de <b>10–15 min</b>, daarna om de <b>2–3 min</b>; de baarmoederhals verstrijkt tot <b>volledige ontsluiting</b>","",T("fasen")),
("b","uitdrijving","Hoe verloopt de uitdrijvingsfase?","Duurt ± <b>10–20 min</b>, bij <b>10 cm</b> ontsluiting: indaling hoofdje, <b>persweeën</b>, geboorte hoofdje + uitwendige spildraai, schouders, rest van het lichaam","Risico op inscheuren van het perineum.<br>"+I("dgh_h8_s14_1.png"),T("fasen")),
("b","nageboorte","Wat gebeurt er bij de nageboorte?","± <b>30 min</b> na de bevalling wordt de <b>placenta</b> geboren → nakijken of ze volledig is","<b>Nooit aan de navelstreng trekken</b> (hevig bloedverlies).",T("fasen")),
("b","navelstreng_trekken","Mag je aan de navelstreng trekken om de placenta te laten komen?","<b>Nooit</b>: kan hevig bloedverlies geven","",T("fasen")),
# Spoedbevalling
("b","vragen","Welke vragen stel je om een spoedbevalling in te schatten?",ul("Hoever in de zwangerschap?","De hoeveelste zwangerschap?","Hoe lang duren de weeën en om de hoeveel minuten?","Vruchtwaterverlies?","Persweeën?","Hoofdje zichtbaar?"),"",T("spoedbevalling")),
("b","multipara","Waarom vraag je naar het aantal zwangerschappen?","Bij <b>meerdere zwangerschappen</b> (multipara) verloopt de bevalling <b>sneller</b>","",T("spoedbevalling")),
("b","weeen_voorbeeld","Weeën van 55 seconden, om de 3 minuten. Wat betekent dit?","<b>Nakende bevalling</b>","",T("spoedbevalling")),
("b","niet_vertrekken","Er zijn aanwijzingen voor een nakende bevalling. Wat doe je?",ul("<b>Ter plaatse blijven</b> (niet vertrekken!)","<b>MUG</b>-bijstand vragen","Geen MUG: <b>huisarts</b> verwittigen"),"Toch vervoer: linker veiligheidshouding.",T("spoedbevalling")),
("b","malinas","Wat zijn de 5 elementen van de Malinas-score?",ul("Aantal zwangerschappen","Duur van de arbeid","Duur van de contracties","Interval tussen de contracties","Vruchtwaterverlies"),"Elk 0–2 punten.",T("malinas")),
("b","malinas_laag","Malinas-score kleiner dan 5: wat doe je?",ul("Vervoer naar het <b>ziekenhuis</b>","Patiënte op de <b>linkerzijde</b> in stabiele zijligging","Zo nodig MUG/PIT"),"",T("malinas")),
("b","malinas_hoog","Malinas-score 5 of meer: wat doe je?",ul("<b>MUG/PIT</b> vragen","Patiënte installeren voor de bevalling, <b>omgekeerd op de brancard</b>","Vitale parameters opvolgen","Komst MUG voorbereiden (infuus)"),"",T("malinas","slides")),
("b","lt24","Zwangere &lt; 24 weken met problemen: waar let je op?","ABC, medische info (pariteit, bevallingsdatum, hoge bloeddruk, bloedverlies, convulsies), <b>tekenen van shock</b>; MUG/PIT zeker bij <b>convulsies</b>","",T("spoedbevalling")),
("b","voorbereiden","Hoe bereid je een spoedbevalling voor?",ul("Steriele/propere doeken + warm water","Bevallingsset klaarleggen","Comfortabele houding (lenden steunen)","Weeën laten <b>wegblazen</b>","O₂, <b>alu-deken</b>, pediatrische koffer klaar"),"",T("begeleiden")),
("b","hoofdje","Hoe ondersteun je de geboorte van het hoofdje?","<b>Damsteun</b> en het hoofdje ondersteunen; <b>nooit op het hoofdje duwen</b>","",T("begeleiden","slides")),
("b","na_geboorte","Wat doe je meteen na de geboorte?",ul("Baby goed vasthouden (glibberig!)","Nakijken of de navelstreng niet rond de hals zit","Baby op de <b>buik van de moeder</b>","Inpakken met doek + alu-deken"),"",T("begeleiden")),
("b","navelstreng_klem",I("dgh_h8_s26_1.png")+"<br>Hoe klem je de navelstreng af?","Op <b>± 10 cm</b> van de buik met <b>2 kochers</b> of een <b>navelklem</b>; <b>niet doorknippen</b>","",T("begeleiden","slides","foto")),
("b","navelstreng_hals","De navelstreng zit rond de hals van de baby. Wat doe je?","<b>Los</b>: over het hoofdje trekken<br><b>Strak</b>: afklemmen en doorknippen → <b>MUG</b>","",T("complicaties")),
("b","prolaps",I("dgh_h8_s28_1.png")+"<br>Wat zie je hier en wat doe je?","<b>Uitzakking van de navelstreng</b>: vrouw vragen <b>niet te persen</b>, zo snel mogelijk naar spoed/verloskwartier","Urgentie: kind in gevaar.",T("complicaties","foto")),
("b","stuit",I("dgh_h8_s29_1.png")+"<br>Wat doe je bij een stuitligging?","<b>Nooit aan de uitstekende ledematen trekken</b>; <b>Trendelenburghouding</b>; naar het verloskwartier","",T("complicaties","foto")),
("b","bloedverlies","Veel bloedverlies bij de bevalling: wat doe je?","ABC, 15 L O₂, <b>Trendelenburghouding</b> en <b>MUG</b> (hypovolemische shock)","",T("complicaties")),
# Zwangerschapscomplicaties
("b","miskraam","Hoe herken je een miskraam (1e trimester)?","<b>Hevig bloedverlies</b> en <b>hevige buikkrampen</b> → gevaar voor hypovolemische shock","",T("zwangerschapscomplicaties")),
("b","clandestien","Welke gevaren heeft een clandestiene abortus?","Ernstige <b>bloedingen</b> (hypovolemische shock) en <b>infecties</b> (septische shock)","",T("zwangerschapscomplicaties")),
("b","ectopisch",I("dgh_h8_s32_1.png")+"<br>Wat is dit en waarom is het gevaarlijk?","<b>Buitenbaarmoederlijke (ectopische) zwangerschap</b>: innesteling in de eileider of buikholte → <b>ernstige inwendige bloedingen</b>","",T("zwangerschapscomplicaties","foto")),
("b","trauma_zwanger","Hoe beschouw je een trauma bij een zwangere vrouw?","<b>Altijd als ernstig</b> → altijd naar spoed, hoe banaal ook","15 L O₂, shockpreventie, linker veiligheidshouding, immobilisatie bij vermoeden wervelletsel.",T("zwangerschapscomplicaties")),
("b","derde_trimester_bloeding","Bloeding in het 3e trimester: waaraan denk je en wat doe je?","Meestal van de <b>placenta</b> → shock → <b>MUG</b> en shockbehandeling starten","",T("zwangerschapscomplicaties")),
("b","eclampsie","Wat is eclampsie en hoe herken je ze?","<b>Zwangerschapsstuipen</b>; alarmteken: <b>hoge bloeddruk</b> (zwelling van de hersenen)","",T("zwangerschapscomplicaties")),
("b","eclampsie_handelen","Wat doe je bij eclampsie?",ul("<b>15 L O₂</b> (masker + reservoir)","<b>Linker veiligheidshouding</b>","<b>MUG</b>"),"",T("zwangerschapscomplicaties","slides")),
("b","linkerzijde","Waarom leg je een zwangere vrouw op haar linkerzijde?","De baby drukt in ruglig op de grote ader → minder bloed terug naar het hart","Daarom: linker veiligheidshouding bij vervoer.",T("spoedbevalling")),
]
media=sorted(glob.glob("h8media/*.png"))
out,n=build(8,"Spoedbevalling","Spoedbevalling",cards,media,"../content/Source/Anki")
print(out,n)
