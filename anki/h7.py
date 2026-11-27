import sys,glob; sys.path.insert(0,".")
from dgh_common import *
T=lambda *x:["H7"]+[f"H7::{t}" for t in x]
I=lambda f:f'<img src="dgh_h7_e_{f}.png">'
cards=[
# Noodplannen
("b","nip","Wat zijn NIP's en welke twee soorten zijn er?","<b>Nood- en interventieplannen</b>: multidisciplinaire plannen<br><b>ANIP</b>: algemeen, voor elke noodsituatie<br><b>BNIP</b>: bijzonder, voor een specifiek risico (bv. chemisch bedrijf, evenement)","",T("noodplannen")),
("b","mono_intern","Wat zijn monodisciplinaire en interne noodplannen?","<b>Monodisciplinair</b>: plan per discipline (bv. het MIP), in lijn met het NIP<br><b>Intern</b>: opgemaakt door een bedrijf/instelling voor eigen incidenten","",T("noodplannen")),
("b","fasen","Welke fasen kan een noodplan hebben en wie is bevoegd?",ul("<b>Gemeentelijk</b>: burgemeester","<b>Provinciaal</b>: gouverneur","<b>Federaal</b>: minister van Binnenlandse Zaken"),"",T("fasen")),
("b","fasen_volgorde","Moet je altijd eerst de gemeentelijke fase afkondigen?","<b>Nee</b>: aard en ernst bepalen het niveau; je kan meteen provinciaal of federaal gaan","",T("fasen")),
("b","fase_parameters","Welke parameters bepalen welke fase wordt afgekondigd?",ul("Geografische <b>reikwijdte</b>","Aan te wenden <b>middelen</b>","Aantal (potentiële) <b>getroffenen</b>","Nood aan <b>coördinatie</b>","Omvang / maatschappelijke impact","<b>Technische complexiteit</b>","<b>Evolutie</b> van de gebeurtenissen"),"",T("fasen")),
("b","afkondigen_wie","Wie kondigt een fase af?","Steeds een <b>beleidsbeslissing</b> van het bevoegde echelon (niet delegeerbaar), op advies van de leider van <b>discipline 1</b>","Hulpverleners kondigen zelf niets af.",T("fasen","slides")),
("b","afkondiging_gevolg","Wat gebeurt er bij het afkondigen van een fase?",ul("Het <b>hogere echelon</b> wordt geïnformeerd","De <b>coördinatiestructuur</b> wordt ontplooid (CP-OPS en CC)"),"",T("fasen")),
("b","opheffen","Wie heft een fase op?","De <b>bevoegde overheid</b>, in overleg met de operationele verantwoordelijken","",T("fasen")),
# Disciplines
("b","d1","Wat is discipline 1 en wie heeft de leiding?","<b>Hulpverleningsoperaties</b>: brandweer + civiele bescherming<br>Leiding: <b>DIR-BW</b>","",T("disciplines")),
("b","d2","Wat is discipline 2 en wie heeft de leiding?","<b>Medische, sanitaire en psychosociale hulp</b> (HVA, MUG, …)<br>Leiding: <b>DIR-MED</b> (onder verantwoordelijkheid van de federale gezondheidsinspecteur)","",T("disciplines")),
("b","d3","Wat is discipline 3 en wie heeft de leiding?","<b>Politie</b> (lokaal en/of federaal)<br>Leiding: <b>DIR-POL</b>","",T("disciplines")),
("b","d4","Wat is discipline 4 en wie heeft de leiding?","<b>Logistieke steun</b>: civiele bescherming, brandweer, Rode Kruis, gespecialiseerde diensten<br>Leiding: <b>DIR-LOG</b>","",T("disciplines")),
("b","d5","Wat is discipline 5 en wie heeft de leiding?","<b>Informatie</b> aan bevolking en media<br>Leiding: <b>DIR-INFO</b>","",T("disciplines")),
("b","veiligheidscel","Wat doet de veiligheidscel?","Een <b>permanente</b> structuur die de noodplannen (ANIP/BNIP) actueel houdt en <b>oefeningen</b> organiseert","Leden: burgemeester/gouverneur, ambtenaar noodplanning, vertegenwoordiger van elke discipline.",T("coordinatie")),
("b","cp_ops","Wat is het CP-OPS en wie leidt het?","De <b>operationele coördinatie</b> op het terrein (commandopost operaties), geleid door de <b>DIR-CP-OPS</b> (meestal hoogste brandweerofficier die niet DIR-BW is)","Leden: DIR-BW, DIR-MED, DIR-POL, DIR-LOG, DIR-INFO.",T("coordinatie")),
("b","cp_ops_taken","Wat zijn de taken van het CP-OPS?",ul("<b>Uitvoeren</b> van de beslissingen van het CC","<b>Coördineren</b> van de bestrijding (o.a. interventiezone bepalen)","<b>Inlichtingen</b> terugkoppelen naar het CC","<b>Overleg</b> bij problemen"),"",T("coordinatie")),
("b","motorkap","Hoe start het CP-OPS bij het begin van een ramp?","Als een 'embryo CP-OPS' via een <b>motorkapoverleg</b> van de eerst aangekomen diensten","Herkenbaar aan een fluogele vlag met 'CP-OPS'.",T("coordinatie")),
("b","cc","Wat is het CC (coördinatiecomité) en wie leidt het?","De <b>beleidscoördinatie</b>, geleid door de <b>burgemeester of gouverneur</b>; zetelt in het gemeentelijk/provinciaal crisiscentrum","Taken: beslissen (evacuatie, opeisingen) en communiceren naar bevolking en pers.",T("coordinatie")),
# Discipline 2
("b","mip_onderdelen","Uit welke luiken bestaat het monodisciplinaire plan van discipline 2?",ul("<b>MIP</b>: Medisch Interventieplan","<b>PSIP</b>: Psychosociaal Interventieplan","<b>SIP</b>: Sanitair Interventieplan","<b>PRIMA</b>: Plan Risico's en Manifestaties"),"",T("d2","mip")),
("b","mip_leiding","Wie heeft de globale leiding over het MIP?","De <b>federale gezondheidsinspecteur</b> (zetelt in het CC), bijgestaan door de <b>DIR-MED</b> op het terrein","",T("d2","mip")),
("b","zones","Hoe is de interventiezone ingedeeld?",ul("<b>Rode zone</b> (uitsluitingsperimeter): direct gevaar","<b>Oranje zone</b> (isolatieperimeter)","<b>Gele zone</b> (ontradingsperimeter): logistiek, vervoer"),"",T("d2","zones")),
("b","noodplanningszone","Wat is het verschil tussen een noodplanningszone en een interventiezone?","<b>Noodplanningszone</b>: vooraf vastgelegd voor een bijzonder risico<br><b>Interventiezone</b>: ter plaatse bepaald door het CP-OPS","",T("d2","zones")),
("b","vmp","Wat is een VMP?","<b>Vooruitgeschoven Medische Post</b>: triage- en behandelzone voor de eerste medische zorg, <b>buiten de rode zone</b> maar dicht bij het rampterrein","",T("d2","vmp")),
("b","noria","Wat is de kleine en de grote NORIA?","<b>Kleine NORIA</b>: vervoer van de rode zone naar de <b>VMP</b><br><b>Grote NORIA</b>: vervoer van de VMP naar het <b>ziekenhuis</b>",I("flow"),T("d2","vmp")),
("b","pretriage","Wat is het doel van de preliminaire triage?","<b>Prioriteit bepalen</b> voor evacuatie naar de VMP (geen medische behandeling), met gekleurde schijven <b>rood / geel / zwart</b>","",T("d2","triage")),
("b","pretriage_flow",I("pretriage")+"<br>Overloop de preliminaire triage.","<ol><li>Kan stappen? → <b>geel</b></li><li>Geen ademhaling → <b>zwart</b></li><li>Ademhaling > 30/min → <b>rood</b></li><li>Geen circulatie → <b>rood</b></li><li>Niet bewust → <b>rood</b>; anders <b>geel</b></li></ol>","",T("d2","triage","foto")),
("b","triage_t","Welke triagecategorieën gebruikt men in de VMP?",ul("<b>T1</b>: onmiddellijke behandeling","<b>T2</b>: uitgestelde behandeling","<b>T3</b>: minimale behandeling","<b>T4</b>: afwachtende behandeling"),"Daarnaast: overledenen en betrokkenen zonder letsel. Triage door de TRI-arts (+ TRI-vpk) aan de ingang.",T("d2","triage")),
("b","mettag",I("mettag")+"<br>Wat is dit en waarvoor dient het?","De <b>triagekaart (METTAG)</b> met kleurcode: zwart = overleden, rood = zeer dringend, geel = dringend, groen = niet dringend","",T("d2","triage","foto")),
("b","polsbandje",I("polsbandje")+"<br>Waarvoor dient het polsbandje bij een ramp?","<b>Registratie</b>: de sticker gaat op de triagekaart, bij elke IN/OUT wordt een barcode geplakt → volledige route van het slachtoffer","",T("d2","triage","foto")),
("b","vmp_vakken","Welke vakken heeft de VMP?",ul("<b>Rood</b>: levensbedreigend, onmiddellijke behandeling","<b>Geel</b>: ernstig maar kan wachten","<b>Groen</b>: licht gekwetst","<b>Zwart</b>: overledenen"),"",T("d2","vmp")),
("b","sit","Wat is SIM / SIT en welke twee soorten SIT zijn er?","<b>Snel Inzetbare Middelen</b> = SIT Rode Kruis<br><b>SIT MED</b>: medisch materiaal (O₂, medicatie, verband)<br><b>SIT LOG</b>: logistiek materiaal (brancards, tenten, dekens)","",T("d2","vmp")),
("b","regulatie","Wat is regulatie en waarop baseert de regulator zich?","Het beheren van de <b>uitstroom</b> naar ziekenhuizen, op basis van:"+ul("Ziekenhuisverdeelschema","Passend transportmiddel","Passend ziekenhuis voor de pathologie"),"",T("d2","regulatie")),
# Alarmering
("b","mip_criteria","Wanneer wordt het MIP opgestart (kwantitatief)?",ul("<b>5</b> zwaargewonden","<b>10</b> gewonden met ongekende ernst","<b>> 20</b> personen potentieel in gevaar"),"Kwalitatief: terreur, NRBC (na overleg).",T("d2","alarmering")),
("b","mip_middelen","Welke middelen worden standaard gestuurd bij een MIP?",ul("<b>3</b> MUG-teams","<b>5</b> ambulances","SIM","GI, DIR-MED, PSM"),"",T("d2","alarmering")),
("b","uitgebreid_mip","Wanneer een uitgebreid MIP en welke middelen?","<b>20</b> zwaargewonden of <b>40</b> gewonden met ongekende ernst → <b>10</b> MUG's, <b>20</b> ambulances","",T("d2","alarmering")),
("b","maxi_mip","Wanneer een Maxi-MIP en welke middelen?","<b>50</b> zwaargewonden of <b>100</b> gewonden met ongekende ernst → <b>20</b> MUG's, <b>40</b> ambulances, alle PSM","",T("d2","alarmering")),
("b","mip_wie","Wie mag het MIP afkondigen?",ul("<b>DIR-MED</b> of adjunct","De <b>eerste MUG-arts</b> ter plaatse (DIR-MED a.i.)","<b>FGI</b> of adjunct","Diensthoofd DH van de FOD of adjunct"),"Op vraag van de eerste 'leider' ter plaatse; formele afkondiging door het HC 112/100.",T("d2","alarmering")),
("b","vooralarm","Wat is een vooralarm?","Bij een <b>potentieel</b> gevaarlijke situatie worden enkel de coördinerende verantwoordelijken (FGI, DIR-MED, PSM) verwittigd om de situatie op te volgen","",T("d2","alarmering")),
("b","fase_mip","Zijn de fase van het noodplan en de opstart van het MIP aan elkaar gekoppeld?","<b>Nee</b>","",T("d2","alarmering","slides")),
("b","aflossing","Na hoeveel tijd voorzie je aflossing bij een ramp?","Bij <b>> 8 uur</b>","Bij langere duur sowieso: rust, sanitair, eten/drinken.",T("d2")),
("b","rapport","Wat moet er na een MIP gebeuren?","<b>Binnen de maand een rapport</b> naar de FGI: ingezette middelen, acties, timing, aantal slachtoffers, bestemmingen","",T("d2")),
# Noodcentrale (slides)
("b","middelen_samenstelling","Wie bemant een ziekenwagen, een PIT en een MUG?","<b>Ziekenwagen</b>: 2 HVA's<br><b>PIT</b>: HVA + urgentieverpleegkundige<br><b>MUG</b>: urgentieverpleegkundige + urgentiearts","",T("noodcentrale","slides")),
("b","mug_transport","Is de MUG een transportmiddel? En de PIT?","<b>MUG</b>: <b>geen</b> transportmiddel<br><b>PIT</b>: <b>wel</b> een transportmiddel","",T("noodcentrale","slides")),
("b","opvordering_vrijheid","Welke vrijheid verliest een slachtoffer door de opvordering van de NC 112?","De vrijheid om <b>zelf zijn arts/ziekenhuis te kiezen</b>","De opvordering moet onverwijld uitgevoerd worden.",T("noodcentrale","slides")),
("b","afwijking_tabel","Hoeveel minuten mag je afwijken van het dichtstbijzijnde ziekenhuis?",ul("Ziekenwagen <b>zonder attest</b>: <b>4 min</b>","Ziekenwagen <b>met doktersattest</b>: <b>10 min</b>","Ziekenwagen begeleid door een <b>(huis)arts</b>: max. <b>30 min</b>","<b>PIT</b>: <b>10 min</b>","<b>MUG</b>: <b>30 min</b>"),"Altijd na overleg met de bevoegde NC 112. Attest max. 1 jaar oud.",T("noodcentrale","afwijkingen","slides")),
("c","afwijking_voorbeeld","Dichtstbijzijnde spoed op 7 min, ziekenwagen zonder attest: je mag maximaal {{c1::11}} min rijden.","7 + 4 = 11",T("noodcentrale","afwijkingen","slides")),
("b","1733","Wat is 1733?","Het nummer voor <b>niet-dringende</b> medische hulp (huisartsenwachtpost)","1722: brandweer bij storm/wateroverlast zonder noodsituatie.",T("noodcentrale","slides")),
]
media=sorted(glob.glob("h7media/*.png"))
out,n=build(7,"Noodplanning","Noodplanning",cards,media,"../content/Source/Anki")
print(out,n)
