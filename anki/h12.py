import sys,glob; sys.path.insert(0,".")
from dgh_common import *
T=lambda *x:["H12"]+[f"H12::{t}" for t in x]
I=lambda f:f'<img src="dgh_h12_e_{f}.png">'
cards=[
# BIOW
("c","biow","BIOW staat voor {{c1::Bescherming Interventies op de Openbare Weg}}.","",T("biow")),
("b","biow_pbm","Welke PBM let je extra op bij een ontzetting?","<b>Lange mouwen aan</b>","",T("biow")),
("b","biow_gordel","Moet je tijdens het rijden naar/van een incident de gordel dragen?","<b>Ja</b>, ook de patiënt (uitzondering enkel als het écht niet kan)","",T("biow")),
("b","fend_off","Hoe parkeer je de ambulance bij een incident op de baan?","<b>Fend-off</b>: wielen schuin, of bij meerdere rijstroken het hele voertuig schuin → bij een aanrijding wordt het voertuig <b>weg van het incident</b> geduwd",I("biow"),T("biow")),
("b","stroomopwaarts","Waar parkeer je als eerste voertuig?","± <b>50 m stroomopwaarts</b> van het incident","50 m ≈ <b>twee verlichtingspalen</b>.",T("biow")),
("b","uitstappen","Waar let je op bij het uitstappen op de openbare weg?","In beide richtingen kijken, schouder aan schouder met je collega, <b>nooit je rug naar het verkeer</b>","",T("biow")),
("b","collectieve_bescherming","Wat doe je met je lichten zodra er collectieve bescherming staat (klapborden, barrières)?","Lichten van de hulpverleningsvoertuigen <b>uit</b> (minder afleiding)","",T("biow")),
("b","multigroep","Wat is een multigroep?","Een radiogespreksgroep waarop <b>meerdere disciplines</b> samen werken","",T("biow","radio")),
# Gevaarlijke stoffen
("b","gs_herkennen","Wanneer denk je aan gevaarlijke stoffen?",ul("Ongeval met een voertuig dat mogelijk gevaarlijke stoffen vervoert","Ongeval in een <b>SEVESO-bedrijf</b>","<b>Meerdere slachtoffers</b> met dezelfde symptomen","Schoollabo, schoonmaakproducten gemengd, drugslabo"),"",T("gevaarlijke_stoffen")),
("b","seveso","Wat is een SEVESO-bedrijf?","Een bedrijf dat <b>grote hoeveelheden gevaarlijke stoffen</b> produceert, opslaat of gebruikt","",T("gevaarlijke_stoffen")),
("b","adr","Wat is ADR?","Het Europees verdrag over het <b>internationaal vervoer van gevaarlijke stoffen over de weg</b>","",T("gevaarlijke_stoffen")),
("b","gs_gevaar","Wat zijn de grootste gevaren van gevaarlijke stoffen en de meest voorkomende besmettingsweg?","Grootste gevaar: <b>brand en ontploffing</b><br>Meest voorkomende besmetting: <b>inhalatie</b>","",T("gevaarlijke_stoffen")),
("b","besmetting","Wat is het verschil tussen primaire en secundaire besmetting?","<b>Primair</b>: door direct contact met de stof<br><b>Secundair</b>: hulpverleners besmet door contact met besmette personen","",T("gevaarlijke_stoffen")),
("b","decontaminatie","Waarmee decontamineer je?","<b>In water oplosbaar</b> (bv. ammoniak, aceton): water<br><b>Niet in water oplosbaar</b> (bv. benzine): <b>water + zeep</b>","Volg de procedure van het bedrijf als die er is.",T("gevaarlijke_stoffen")),
("b","gs_stop","Wat doe je zodra je gevaarlijke stoffen herkent?","<b>STOP</b> → info vergaren en de juiste diensten aansturen; bij gevaar: <b>terugtrekken</b>","",T("gevaarlijke_stoffen")),
("b","bovenwinds","Hoe benader je een incident met gevaarlijke stoffen?","<b>Bovenwinds</b> (wind in je rug), rekening houdend met <b>hoogteverschillen</b>","Noordenwind = wind komt uit het noorden.",T("gevaarlijke_stoffen")),
("b","opstellen","Waar stel je de ziekenwagen nooit op bij gevaarlijke stoffen?",ul("<b>Nooit in gas- of dampwolken</b>","<b>Nooit in vloeistofplassen</b>"),"Ramen dicht en ventilatie uit bij het aanrijden.",T("gevaarlijke_stoffen")),
("b","afstanden","Welke veiligheidsafstanden hou je bij gevaarlijke stoffen?",ul("<b>50 m</b>: duidelijk bovenwinds, overzichtelijk, stof bekend","<b>100 m</b>: geen zekerheid over wind of stof","<b>500 m</b>: dreiging van een krachtige explosie"),"",T("gevaarlijke_stoffen","slides")),
("b","gs_brandweer_weg","De brandweer is nog niet ter plaatse. Wat doe je?",ul("<b>Afstand</b> houden, jezelf niet in gevaar brengen","<b>Alle contact</b> met het product vermijden","Geen open vuur, niet eten/drinken/roken","Slachtoffers in veiligheid brengen (indien mogelijk)","Info verzamelen (Kemlerborden, veiligheidskaarten, verpakkingen)"),"Daarna: instructies van de brandweer nauwgezet volgen.",T("gevaarlijke_stoffen","slides")),
("b","gs_fotos","Waarom maak je foto's bij een incident met gevaarlijke stoffen?","Om <b>containers, labels, kleur van vloeistof en wonden</b> door te geven (NC 112, ziekenhuis)","",T("gevaarlijke_stoffen","notas")),
("b","gs_sitrep","Waarom geef je altijd een SITREP aan de NC 112?","Om brandweer/politie te informeren en zo nodig medisch op te schalen (<b>MIP</b>)","De NC 112 heeft geen glazen bol.",T("gevaarlijke_stoffen","slides")),
("b","gevi",I("gevi")+"<br>Hoe lees je een Kemlerbord (oranje bord)?","<b>Bovenaan</b>: GEVI-nummer (gevaarsidentificatie)<br><b>Onderaan</b>: UN-nummer (stofidentificatie)","",T("gevaarlijke_stoffen","kemler","foto")),
("b","gevi_cijfers","Wat betekenen de cijfers van een GEVI-nummer?",ul("2: gas","3: brandbare vloeistof","4: brandbare vaste stof","5: oxiderend","6: giftig","7: radioactief","8: bijtend","9: diverse gevaren"),"Het eerste cijfer is het belangrijkste gevaar.",T("gevaarlijke_stoffen","kemler")),
("b","gevi_dubbel","Wat betekent een verdubbeld cijfer of een X in een GEVI-nummer?","<b>Verdubbeling</b>: versterking van het gevaar (30 brandbaar → 33 zeer brandbaar)<br><b>X</b>: reageert <b>gevaarlijk met water</b>","",T("gevaarlijke_stoffen","kemler")),
("b","kemler_leeg","Wat betekent een leeg oranje bord (zonder cijfers)?","Gevaarlijke lading van <b>diverse stoffen</b> (UN-nummer elders te vinden), of de vrachtwagen is <b>leeg en gereinigd</b>","",T("gevaarlijke_stoffen","kemler","slides")),
("b","ghs",I("ghs")+"<br>Wat is dit systeem?","<b>GHS</b>: het wereldwijd systeem van gevaarpictogrammen op verpakkingen (ontplofbaar, ontvlambaar, giftig, bijtend, …)","",T("gevaarlijke_stoffen","foto")),
("b","cbrne",I("cbrne")+"<br>Waar staat CBRN(E) voor?","<b>C</b>hemisch, <b>B</b>iologisch, <b>R</b>adiologisch, <b>N</b>ucleair (+ <b>E</b>xplosief)","Speciale diensten (leger/civiel) die deze situaties beoordelen en onschadelijk maken.",T("gevaarlijke_stoffen","foto")),
("b","hcn_h2s","Welke geur hebben blauwzuurgas (HCN) en waterstofsulfide (H₂S)?","<b>HCN</b>: <b>amandelen</b><br><b>H₂S</b>: <b>rotte eieren</b>","",T("gevaarlijke_stoffen","slides")),
# ASTRID
("b","astrid","Wat is ASTRID?","Het <b>radionetwerk</b> van de hulpdiensten (All-round Semi-cellular Trunking Radio network with Integrated Dispatching), gebaseerd op <b>TETRA</b>","",T("radio")),
("b","gssi_issi","Wat is het verschil tussen GSSI en ISSI?","<b>GSSI</b> (Group): per gespreksgroep, <b>6 cijfers</b><br><b>ISSI</b> (Individual): per toestel, <b>7 cijfers</b><br>Beide beginnen met een 6","Zichtbaar maken met <code>*#06#</code>.",T("radio")),
("b","dmo_tmo","Wat is het verschil tussen DMO en TMO?","<b>DMO</b> (direct mode): enkel rond het voertuig (max. ± 500 m), bv. binnen in gebouwen<br><b>TMO</b> (trunked mode): via het netwerk, met noodknop","",T("radio","slides")),
("b","gespreksgroep_provincie","Waarom vermeld je altijd de provincie bij een gespreksgroep?","Dezelfde naam bestaat in meerdere provincies (bv. <b>OVL</b>-OEF-06 ≠ WVL-OEF-06)","",T("radio")),
("b","statuscodes","Wat betekenen de ASTRID-statuscodes?",ul("<b>00</b> beschikbaar op standplaats","<b>01</b> gealarmeerd","<b>02</b> vertrek naar opdracht","<b>03</b> aankomst ter plaatse","<b>04</b> vertrek naar ziekenhuis","<b>05</b> aankomst ziekenhuis","<b>06</b> terug naar standplaats","<b>07</b> aankomst op standplaats","<b>08</b> oproepbaar"),"",T("radio","slides")),
("c","status_04","Status {{c1::04}} (vertrek naar ziekenhuis) geef je radiofonisch door, niet via de cijfertoets.","",T("radio","notas")),
("b","nato","Hoe geef je namen of codes door via de radio?","Met het <b>NATO-alfabet</b> en <b>cijfer per cijfer</b>","",T("radio")),
("b","methane","Waarvoor gebruik je METHANE?","Voor een gestructureerde <b>SITREP</b> (situatierapport)","",T("radio")),
("b","radiodiscipline","Wat zijn de regels van radiodiscipline?",ul("Bereid je boodschap voor","Kort en duidelijk","Kalm, traag, gearticuleerd","Beschaafd en beheerst","Microfoon 2–3 cm van je mond","Pas spreken als het <b>lichtje groen</b> is (verbinding)","Geen persoonlijke gesprekken"),"",T("radio")),
("b","noodknop","Wanneer gebruik je de noodknop op de radio?","Enkel in de <b>allerhoogste nood</b>","",T("radio","slides")),
]
media=sorted(glob.glob("h12media/*.png"))
out,n=build(12,"Veiligheid en communicatie","Veiligheid_communicatie",cards,media,"../content/Source/Anki")
print(out,n)
