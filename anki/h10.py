import sys,glob; sys.path.insert(0,".")
from dgh_common import *
T=lambda *x:["H10"]+[f"H10::{t}" for t in x]
I=lambda f:f'<img src="dgh_h10_e_{f}.png">'
cards=[
("b","baby_kind","Wat is het verschil tussen een baby en een kind?","<b>Baby/zuigeling</b>: &lt; 1 jaar<br><b>Kind</b>: vanaf 1 jaar tot de <b>puberteit</b>","",T("algemeen")),
("b","schema_kind","Gebruik je bij kinderen een ander benaderingsschema?","<b>Nee</b>: hetzelfde schema (3S – bcQ – ABCDE – FGHI), maar anatomie, fysiologie en communicatie verschillen","BEFAST is ook bij kinderen nodig.",T("algemeen")),
# Anatomie / fysiologie
("b","luchtweg_kind","Hoe positioneer je het hoofd om de luchtweg vrij te maken bij een baby en bij een kind?","<b>Baby</b>: <b>neutrale</b> hoofdpositie<br><b>Kind</b>: hoofd licht kantelen + kinlift","Nooit hyperstrekken. Zo nodig mayocanule (P06).",T("anatomie","luchtweg")),
("b","hyperstrekking","Waarom mag je de luchtweg van een baby niet hyperstrekken?","De luchtpijp bevat <b>week kraakbeen</b>: hyperstrekking drukt de luchtpijp dicht","",T("anatomie","luchtweg")),
("b","hoofd_verhouding",I("hoofd")+"<br>Wat is het verschil in verhouding hoofd/lichaam tussen baby en volwassene?","Baby: hoofd ± <b>25 %</b> van het lichaam; volwassene ± <b>6 %</b>","Groot hoofd + zwakke nek → bij hoofdletsel altijd aan de halswervels denken.",T("anatomie","foto")),
("b","neusademhaling","Langs welke weg ademt een baby voornamelijk en wat volgt daaruit?","Via de <b>neus</b> → <b>neushygiëne</b>! (een verstopte neus geeft ademnood)","",T("anatomie","luchtweg")),
("b","diafragma","Wat is de belangrijkste ademhalingsspier bij een kind?","Het <b>diafragma</b> (middenrif)","",T("anatomie")),
("b","alveolen_kind","Waarom raakt een kind sneller in zuurstoftekort?",ul("<b>Kleinere</b> luchtwegen en luchtreserve","Kleinere longblaasoppervlakte (pasgeborene ± 3 m² vs. volwassene ± 70 m²)"),"",T("anatomie")),
("b","ah_kind","Wat is het ademhalingsritme bij een baby, kleuter en tiener?","Tot 30 dagen: ± <b>30</b>/min<br>5 jaar: ± <b>20</b>/min<br>14 jaar: ± <b>14</b>/min","",T("anatomie","parameters")),
("b","hr_kind","Wat is de hartslag bij een baby, kleuter en tiener?","Tot 30 dagen: ± <b>130</b>/min<br>5 jaar: ± <b>100</b>/min<br>14 jaar: ± <b>70</b>/min","",T("anatomie","parameters")),
("b","pols_kind","Waar kan je bij een kind de pols voelen?",ul("Carotis","<b>Brachialis</b> (bovenarm, baby)","Radialis","Femoralis"),"",T("anatomie","parameters")),
("c","bloedvolume","Bloedvolume per kg: baby {{c1::80}} ml/kg, volwassene {{c2::60–70}} ml/kg.","Het totale volume is wel veel kleiner → klein verlies is al ernstig.",T("anatomie")),
("b","dehydratie","Waarom raken baby's en kinderen sneller uitgedroogd en wat controleer je?","<b>Minder circulerend volume</b>; braken en diarree geven snel dehydratatie → <b>check de fontanel</b>","Ingevallen = uitdroging, opgezet = verhoogde druk (bv. meningitis).",T("anatomie")),
("b","temp_kind","Waar meet je de temperatuur bij een baby?","<b>Rectaal</b> (P20)","",T("anatomie","parameters")),
("b","pijn_kind","Hoe bevraag je pijn bij een kleuter/kind?","Met <b>pictogrammen</b> (smileys)","",T("anatomie","pijn")),
("b","so2_pijn","Wat zegt O02 over pijnstilling?","Pijnscore <b>4–7</b>: immobiliseren, voorzichtig vervoer<br>Pijnscore <b>> 7</b>: <b>MUG/PIT</b>-bijstand + infuusmateriaal voorzien","",T("anatomie","pijn")),
("b","vervoer_kind",I("vervoer")+"<br>Mag je een kind vervoeren in de armen van de ouder?","<b>Nee</b>: iedereen moet goed vastzitten → autostoeltje of pediatrisch harnas op de brancard","Voorkom afkoeling (toedekken, cel verwarmen).",T("vervoer","foto")),
# Communicatie
("b","kind_angsten","Waarvoor zijn kinderen bang bij hulpverleners?",ul("Een <b>prik</b>","(Meer) <b>pijn</b>","<b>Gescheiden</b> worden van de ouders","Reactie van ouders / <b>straf</b>"),"",T("communicatie")),
("b","communicatie_kind","Hoe pas je je communicatie aan naar een kind?",ul("Rustig benaderen","Op <b>dezelfde hoogte</b> gaan zitten","Praten <b>tegen het kind</b>, niet enkel tegen de ouders","Zeggen wie je bent en wat je komt doen","<b>Vertrouwenspersoon</b> bij het kind laten"),"",T("communicatie")),
("b","wenen","Mag een kind wenen?","<b>Ja</b>: wenen is een verdedigingsmiddel","Oordeel niet, straf niet.",T("communicatie")),
("b","eerlijk","Waarom lieg je nooit tegen een kind?","Om de <b>vertrouwensband</b> niet te breken; leg uit wat je doet en <b>toon het materiaal</b> op voorhand","",T("communicatie")),
("b","ouders","Hoe ga je om met zenuwachtige ouders?",ul("Blijf <b>kalm en geduldig</b>","Reageer niet op verwijten (bewaak wel je veiligheid)","Oordeel niet","<b>Doelgerichte vragen</b>","Leg uit wat je doet","Geef hen een <b>taak</b>","<b>1 persoon</b> mag meerijden"),"",T("communicatie")),
# Ziektebeelden
("b","vreemd_voorwerp_eerst","Waar denk je eerst aan bij plotse ademnood bij een kind?","Een <b>vreemd voorwerp</b> (bv. kind speelde net nog normaal)","",T("ademhaling")),
("b","valse_kroep","Hoe herken je valse kroep en wat doe je?","Vernauwing van het <b>strottenhoofd</b>: <b>inademing</b> moeilijk, <b>stridor</b>, <b>blafhoest</b>, erger tijdens de slaap<br>Handelen: <b>vochtige, warme dampen</b> (douche, warmwaterkraan open)","",T("ademhaling")),
("b","epiglottitis","Hoe herken je epiglottitis?","<b>Bacteriële</b> ontsteking van het strotklepje: inademing moeilijk, <b>stridor</b>, <b>hoge koorts</b>, pijn bij slikken, <b>kwijlen</b>","",T("ademhaling")),
("b","astma_kind","Hoe herken je een astma-aanval?","Vernauwing van de <b>kleine</b> luchtwegen: <b>uitademen</b> bemoeilijkt en verlengd, <b>piepen</b>","Angst en emoties verhogen de kans.",T("ademhaling")),
("b","stridor_piepen","Stridor of piepen: waar zit het probleem?","<b>Stridor</b> (bij inademen): valse kroep, epiglottitis<br><b>Piepen</b> (bij uitademen): astma","",T("ademhaling")),
("b","status_astmaticus","Wat is een status astmaticus?","Een ernstige astma-aanval <b>die blijft duren</b>, met ademnood → <b>medische bijstand!</b>","",T("ademhaling")),
("b","o15","Wat doe je bij acute ademnood bij een kind (O15)?",ul("ABC, info over voorgeschiedenis/allergie","<b>Halfzittend</b>, geruststellen","<b>100 % O₂</b>","MUG/PIT","Aerosol enkel na akkoord arts","Aspiratie vermijden tenzij strikt nodig"),"",T("ademhaling","staande_orders")),
("b","bronchiolitis","Wat is bronchiolitis?","Een <b>virale</b> infectie (RSV) bij kinderen <b>&lt; 2 jaar</b>; meestal goed verloop, maar gevaarlijk voor baby's","",T("ademhaling")),
("b","meningitis","Wat zijn de symptomen van meningitis?","<b>Algemeen</b>: koorts, hoofdpijn, braken, slaperig, <b>rode/paarse puntbloedingen</b>, lichtschuw, verward, stuipen<br><b>Bij baby</b>: ander huilen, prikkelbaar bij oppakken, slecht drinken, kreunen, <b>opgezette fontanel</b>","",T("infecties")),
("b","sepsis","Wat zijn de belangrijkste symptomen van sepsis bij een kind?",ul("<b>Snelle</b> hartslag en/of ademhaling","<b>Afwijkende</b> temperatuur","<b>Onwel</b> (slaperig, verward)","<b>Pijn</b> (spieren, nek, gewrichten)"),"Aanvullend: grauwe/gemarmerde huid, minder plassen.",T("infecties")),
("b","stuipen_oorzaken","Welke oorzaken van stuipen bij kinderen ken je?",ul("Epilepsie","<b>Koortsstuipen</b>","Diabetesstuipen (hypoglycemie → glycemie meten!)"),"",T("stuipen")),
("b","koortsstuipen","Wat doe je bij koortsstuipen (na de aanval)?","Kind <b>uitkleden</b>, lauw afkoelen, licht toedekken, vitale functies opvolgen","Koortsstuipen zijn even gevaarlijk als andere stuipen. T° > 38,5 °C → uitkleden, weinig toedekken.",T("stuipen")),
("b","status_epi_kind","Wanneer spreek je bij een kind van een status epilepticus?","Een aanval <b>langer dan 3 minuten</b> → 112 + MUG","",T("stuipen","slides")),
("b","o07","Wat doe je bij convulsies bij een kind (O07)?",ul("ABC, zo nodig CPR","S-AMPLE (epilepsie, diabetes, vergiftiging, trauma)","Ademt: stabiele zijligging","<b>100 % O₂</b>","<b>Glycemie</b> meten","MUG/PIT"),"Ernstcriteria: status epilepticus, petechiën (meningokokken), schedeltrauma.",T("stuipen","staande_orders")),
("b","syncope_kind","Wat is een syncope?","Plots <b>bewustzijnsverlies</b> door verminderde bloedcirculatie in de hersenen","",T("bewustzijn")),
("b","breath_holding","Wat is een breath holding spell?","Een aanval van <b>adem inhouden</b> tijdens een <b>woedebui</b>: stopt met ademen na uitademing, blauw/bleek, kort bewustzijnsverlies, soms spiertrekkingen → <b>stopt vanzelf</b>","",T("bewustzijn")),
# Verdrinking
("b","verdrinking_types","Wat is het verschil tussen natte en droge verdrinking?","<b>Natte</b>: longen lopen vol water<br><b>Droge</b>: <b>spasme van het strottenhoofd</b> (bv. springen in koud water, ontwaken uit narcose)","",T("verdrinking")),
("b","near_drowning","Wat is near drowning en wat doe je?","Het gevaar lijkt geweken, maar water heeft de longblaasjes aangetast → tot <b>72 uur</b> later fatale gevolgen (hoesten, ademnood, lusteloos)<br>→ <b>Altijd naar het ziekenhuis</b> (beeldvorming thorax)","",T("verdrinking")),
# Trauma
("b","trauma_kind","Wat is de nummer 1 doodsoorzaak bij kinderen?","<b>Trauma</b> (verkeer zonder gordel/autostoel, fietsen zonder helm, spelen, brandwonden, klemmen)","",T("trauma")),
("b","aanrijding_kind",I("aanrijding")+"<br>Welke letsels verwacht je bij een kind dat door een auto wordt aangereden?",ul("<b>Dijbeenfractuur</b>","Stompe letsels <b>buik/borst</b>","<b>Hoofdletsel</b>"),"Een kind wordt ter hoogte van de romp geraakt.",T("trauma","foto")),
("b","nexus_kind","Gelden de NEXUS-criteria en het immobilisatieschema ook bij kinderen?","<b>Ja</b>, hetzelfde stroomschema (Q0–Q3)","",T("trauma")),
# Vergiftiging
("b","vergiftiging_kind","Wat is belangrijk bij een vergiftiging bij een kind?",ul("<b>Hoeveelheid</b> van het product inschatten","<b>Lichaamsgewicht</b> (zelfde dosis = grotere impact)","<b>Manier</b> van inname","Aard en duur van het contact"),"Neem het product mee naar het ziekenhuis.",T("vergiftiging")),
# Wiegendood
("b","wiegendood","Wat is wiegendood?","Een baby (vooral <b>0–6 maanden</b>) overlijdt aan een <b>ademhalingsstilstand</b> in het bedje, <b>zonder voorafgaande tekenen</b> van ziekte","Diagnose via voorgeschiedenis, onderzoek ter plaatse en autopsie.",T("wiegendood")),
("b","wiegendood_risico","Wat zijn risicofactoren voor wiegendood?",ul("Leeftijd <b>0–6 maanden</b>","Vroeggeboorte, laag geboortegewicht","<b>Verminderde wekbaarheid</b>","Omgeving: temperatuur, roken, drugs, slaapomgeving"),"",T("wiegendood")),
("b","wiegendood_aanpak","Wat doe je bij een vermoeden van wiegendood?","<b>Reanimatie starten</b>","Preventie: richtlijnen Kind & Gezin.",T("wiegendood")),
# Mishandeling
("b","mishandeling_vormen","Welke vormen van kindermishandeling zijn er?",ul("Slaan/<b>schudden</b>","Mutilatie (brandwonden, krassen)","Seksueel misbruik","<b>Münchhausen by proxy</b>","<b>Verwaarlozing</b> (basisbehoeften, liefde)","Psychologische mishandeling"),"",T("mishandeling")),
("b","mishandeling_signalen","Welke signalen wijzen op kindermishandeling?",ul("Letsels die <b>niet stroken met het verhaal</b>","Kind kijkt <b>eerst naar de ouder</b> voor het antwoordt","Ouders laten het kind <b>niet aan het woord</b>","<b>Oude en nieuwe</b> letsels","<b>Sigarettenbrandwonden</b>","Ouders ongeïnteresseerd (soms onder invloed)"),"",T("mishandeling")),
("b","mishandeling_houding","Hoe gedraag je je bij een vermoeden van mishandeling?",ul("Verleen de nodige hulp","Benader kind en ouders met <b>tact</b>","<b>Geen oordeel</b> (kan escaleren)","Luister en kijk naar de hele situatie","Kind indien mogelijk volledig uitkleden","Meld je bevindingen <b>onder 4 ogen aan de spoedarts</b>"),"Je kan niets bewijzen: het blijft een vermoeden.",T("mishandeling")),
("b","meldingsplicht","Mag je bij mishandeling je beroepsgeheim doorbreken?","<b>Ja</b>: er is een <b>meldingsplicht</b> om de minderjarige te beschermen (noodtoestand: fysieke/seksuele integriteit gaat boven het beroepsgeheim)","",T("mishandeling","slides")),
# REA kind (kort, rest in H4)
("b","rea_kind_verschil","Wat is het grote verschil bij de reanimatie van een kind?","<b>5 startbeademingen</b> en <b>15/2</b> (oorzaak meestal ademhaling)","Details: zie H4 (Levensbedreigende aandoeningen).",T("reanimatie")),
]
media=sorted(glob.glob("h10media/*.png"))
out,n=build(10,"Pediatrische urgenties","Pediatrische_urgenties",cards,media,"../content/Source/Anki")
print(out,n)
