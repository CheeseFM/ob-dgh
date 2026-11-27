import sys,glob; sys.path.insert(0,".")
from dgh_common import *
T=lambda *x:["H3"]+[f"H3::{t}" for t in x]
I=lambda f,e="png":f'<img src="dgh_h3_e_{f}.{e}">'
cards=[
# Oriëntatie
("b","anatomie_fysiologie","Wat is het verschil tussen anatomie en fysiologie?","<b>Anatomie</b>: de <b>bouw</b> van het lichaam<br><b>Fysiologie</b>: de <b>werking</b> van de stelsels","",T("orientatie")),
("b","links_rechts","Als je 'links' zegt bij een patiënt, welke kant bedoel je?","De <b>linkerkant van de patiënt</b> (dus rechts voor jou als je ervoor staat)","",T("orientatie")),
("b","proximaal_distaal","Wat betekenen proximaal en distaal?","<b>Proximaal</b>: dichter bij de romp<br><b>Distaal</b>: verder van de romp",I("orientatie"),T("orientatie")),
("b","mediaal_lateraal","Wat betekenen mediaal en lateraal?","<b>Mediaal</b>: naar het midden toe<br><b>Lateraal</b>: van het midden weg",I("orientatie"),T("orientatie")),
("b","craniaal_caudaal","Wat betekenen craniaal en caudaal?","<b>Craniaal</b> (superieur): naar het hoofd toe<br><b>Caudaal</b> (inferieur): naar de voeten toe",I("orientatie"),T("orientatie")),
("b","anterieur_posterieur","Wat betekenen anterieur/ventraal en posterieur/dorsaal?","<b>Anterieur / ventraal</b>: voorkant (buikzijde)<br><b>Posterieur / dorsaal</b>: achterkant (rugzijde)",I("orientatie"),T("orientatie")),
("b","streken","Noem de lichaamsstreken aan de voorkant (anterieur).",ul("Hoofdstreek","Halsstreek","Bovenste lidmaat","Borststreek + buikstreek (= rompstreek)","Bekken, lies, schaamstreek","Onderste lidmaat"),I("streken_ant")+I("streken_post"),T("orientatie","streken")),
# Holten
("b","holten","Welke lichaamsholten zijn er en wat zit erin?",ul("<b>Schedelholte</b>: hersenen","<b>Wervelkanaal</b>: ruggenmerg","<b>Borstholte</b>: longen, hart, luchtpijp, slokdarm, grote bloedvaten","<b>Buikholte</b>: maag, lever, pancreas, milt, galblaas, darmen"),I("holtes"),T("holten")),
("b","mediastinum","Wat zit in het mediastinum?","Het middengedeelte van de borstholte: <b>hart</b>, <b>luchtpijp</b>, <b>slokdarm</b> en <b>grote bloedvaten</b>","",T("holten")),
("b","buik_rb","Welke organen liggen in het rechter bovenkwadrant van de buik?","<b>Lever</b> en <b>galblaas</b>",I("buikkwadranten"),T("buik")),
("b","buik_lb","Welke organen liggen in het linker bovenkwadrant van de buik?","<b>Milt</b>, <b>maag</b>, dikke darm",I("buikkwadranten"),T("buik")),
("b","buik_ro","Welk orgaan ligt typisch in het rechter onderkwadrant (rechter fossa)?","De <b>appendix</b> (blindedarm)",I("buikkwadranten"),T("buik")),
("b","epigastrium","Wat is het epigastrium en welke organen liggen er?","Het bovenste middengebied van de buik (maagregio): <b>maag</b>, <b>lever</b>, <b>alvleesklier</b>",I("negen_buikdelen"),T("buik")),
("b","flanken","Welk orgaan voel je ter hoogte van de flanken?","De <b>nieren</b>","",T("buik")),
# Wervelkolom
("b","wervels_aantal","Uit hoeveel wervels bestaat elk deel van de wervelkolom?",ul("Hals (cervicaal): <b>7</b> (C1–C7)","Rug (thoracaal/dorsaal): <b>12</b> (T1–T12)","Lenden (lumbaal): <b>5</b> (L1–L5)","Heiligbeen (sacrum): meestal <b>5</b>, vergroeid","Staartbeen (coccyx): meestal <b>4</b>"),I("wervelkolom"),T("wervelkolom")),
("b","rugwervels_kanaal","Waarom is een verschuiving van de rugwervels (thoracaal) zo gevaarlijk?","Het <b>ruggenmergkanaal is daar zeer smal</b>: een kleine verplaatsing kan al verlamming geven","",T("wervelkolom")),
("b","tussenwervelschijf","Wat zit er tussen twee wervels?","Een <b>tussenwervelschijf</b>: kraakbeenring met een gelachtige kern","",T("wervelkolom")),
# Zenuwstelsel
("b","vitale_stelsels","Welke 3 lichaamsstelsels zijn vitaal?",ul("<b>Zenuwstelsel</b>","<b>Ademhalingsstelsel</b>","<b>Hart- en bloedvatenstelsel</b>"),"Valt er één weg, dan is er direct levensgevaar.",T("zenuwstelsel")),
("b","czs","Wat vormt het centrale zenuwstelsel?","De <b>hersenen</b> en het <b>ruggenmerg</b>","",T("zenuwstelsel")),
("b","hersendelen","Wat zijn de 3 basisdelen van de hersenen en hun functie?",ul("<b>Grote hersenen</b> (cerebrum): bewustzijn, signalen uitsturen","<b>Kleine hersenen</b> (cerebellum): bewegingen coördineren","<b>Hersenstam</b>: belangrijkste levensfuncties, verbinding met ruggenmerg"),I("hersenen","jpg"),T("zenuwstelsel")),
("b","hersenstam","Wat regelt de hersenstam?",ul("<b>Hartslag</b>","<b>Ademhaling</b>","<b>Bloeddruk</b>","<b>Bewustzijn</b>"),"Daarom van levensbelang.",T("zenuwstelsel")),
("b","hersenkwabben","Welke functie heeft elke hersenkwab?",ul("<b>Frontaal</b> (voorhoofd): plannen, beweging, persoonlijkheid","<b>Pariëtaal</b> (wandbeen): ruimte, aandacht","<b>Occipitaal</b> (achterhoofd): zicht","<b>Temporaal</b> (slaap): geheugen, gehoor, taal"),I("hersenen","jpg"),T("zenuwstelsel")),
("b","kruising","Een patiënt heeft een hersenletsel in de rechterhersenhelft. Welke lichaamshelft is uitgevallen?","De <b>linkerhelft</b>: de zenuwbanen kruisen ter hoogte van de nek/hersenstam","Uitzonderingen: o.a. geur, gezichtsmotoriek, gehoor, tong",T("zenuwstelsel")),
("b","neuron","Wat zijn de onderdelen van een zenuwcel?",ul("<b>Dendrieten</b>: ontvangen signalen","<b>Cellichaam</b>: verwerkt informatie","<b>Axon</b>: geleidt het signaal","<b>Synaps</b>: geeft het signaal door (neurotransmitters)"),I("neuron"),T("zenuwstelsel")),
("b","willekeurig","Wat is het verschil tussen het willekeurig en onwillekeurig zenuwstelsel?","<b>Willekeurig</b>: bewust (praten, bewegen)<br><b>Onwillekeurig / autonoom</b>: maag-darm, klieren, hart","",T("zenuwstelsel")),
("b","ortho_para","Wat doet het orthosympathisch en wat het parasympathisch zenuwstelsel?","<b>Orthosympathisch</b>: fight or flight → hartslag omhoog, vasoconstrictie, glucose vrijgeven<br><b>Parasympathisch</b>: rust → energie opslaan en sparen","",T("zenuwstelsel")),
("c","0_4_10","0-4-10-regel: vanaf {{c1::0}} min klinisch dood, na {{c2::4}} min hersenschade, na {{c3::10}} min onomkeerbare hersendood.","",T("zenuwstelsel","examen")),
("b","belang_zenuw","Welke letsels aan het zenuwstelsel zijn voor de HVA belangrijk?",ul("<b>Zuurstoftekort</b>: hersenschade (0-4-10)","<b>Wervelschade</b>: druk op het ruggenmerg → (mogelijk blijvende) verlamming"),"",T("zenuwstelsel","examen")),
# Ademhaling
("b","ah_onderdelen","Wat zijn de onderdelen van het ademhalingsstelsel, van boven naar onder?","Neus → keelholte → <b>larynx</b> (strottenhoofd) → <b>trachea</b> (luchtpijp) → <b>bronchiën</b> → bronchiolen → <b>alveolen</b> (longblaasjes)",I("ademhalingsstelsel"),T("ademhaling")),
("b","neus_functie","Wat doet de neus met de ingeademde lucht?","<b>Filteren en verwarmen</b> (slijm, neushaartjes) en slechte geuren detecteren","",T("ademhaling")),
("b","baby_neus","Waarom is een verstopte neus gevaarlijk bij een zeer jonge baby?","Baby's ademen bijna <b>enkel via de neus</b>","",T("ademhaling","examen")),
("b","epiglottis","Wat is de epiglottis en wat doet ze?","Het <b>strotklepje</b>: sluit de luchtpijp af bij slikken (scheidt luchtpijp en slokdarm)","",T("ademhaling")),
("b","trachea_ringen","Waarom bestaat de luchtpijp uit halve kraakbeenringen?","Zodat grote voedselbrokken door de <b>slokdarm</b> (achter de luchtpijp) kunnen","",T("ademhaling")),
("b","alveolen","Waar gebeurt de gasuitwisseling?","In de <b>alveolen</b> (longblaasjes): O₂ gaat naar het bloed in de haarvaten, CO₂ terug naar de longen",I("longblaasje"),T("ademhaling")),
("b","inademen","Hoe werkt inademen en uitademen?","<b>Inademen</b>: middenrif spant op (zakt) → onderdruk → lucht stroomt binnen<br><b>Uitademen</b>: middenrif ontspant → lucht stroomt buiten",I("ademproces"),T("ademhaling")),
("b","pleura","Hoe heten de vliezen rond de longen en de ruimte ertussen?","<b>Pleura</b> (longvliezen) en de <b>pleuraholte</b>","",T("ademhaling")),
("b","pneumothorax","Wat is een pneumothorax (klaplong)?","<b>Lucht tussen de twee longvliezen</b> (pleuraholte) die de plaats van de long inneemt → de long valt samen","Open (wonde naar buiten) of gesloten (bv. gebroken rib van binnenuit).",T("ademhaling")),
("b","spanningspneu","Wat is een spanningspneumothorax?","Lucht komt in de pleuraholte maar <b>kan er niet meer uit</b> → druk stijgt en duwt op het hart en de andere long","Levensbedreigend.",T("ademhaling")),
("b","belang_ah","Waarom is het ademhalingsstelsel belangrijk voor de HVA?",ul("Zuurstoftekort → <b>hersenschade</b>","Belemmerde luchtweg (tong, braaksel, voorwerp) is <b>direct levensbedreigend</b>","Gebroken ribben of voorwerpen door de longvliezen verstoren de <b>blaasbalgfunctie</b>"),"",T("ademhaling","examen")),
# Hart
("b","slagader_ader","Wat is het verschil tussen een slagader en een ader?","<b>Slagader</b> (arterie): bloed <b>van het hart weg</b> (meestal zuurstofrijk)<br><b>Ader</b> (vene): bloed <b>naar het hart toe</b> (meestal zuurstofarm), heeft kleppen","",T("hart")),
("b","haarvaten","Wat zijn haarvaten?","De kleinste bloedvaten (tussen slagaders en aders) waar de <b>uitwisseling</b> van O₂ en CO₂ gebeurt","",T("hart")),
("b","longslagader","Welk bloed vervoert de longslagader, en welk de longaders?","<b>Longslagader</b>: <b>zuurstofarm</b> bloed van het hart naar de longen<br><b>Longaders</b>: <b>zuurstofrijk</b> bloed van de longen naar het hart","De uitzondering op 'slagader = zuurstofrijk'.",T("hart")),
("b","holle_aders","Wat doen de holle aders?","Ze brengen <b>zuurstofarm bloed</b> uit het lichaam terug naar de <b>rechtervoorkamer</b> (bovenste en onderste holle ader)","",T("hart")),
("b","kleine_bloedsomloop","Beschrijf de kleine bloedsomloop.","Rechterkamer → <b>longslagader</b> → longen → <b>longaders</b> → linkervoorkamer",I("bloedsomloop"),T("hart")),
("b","grote_bloedsomloop","Beschrijf de grote bloedsomloop.","Linkerkamer → <b>aorta</b> → organen en weefsels → <b>holle aders</b> → rechtervoorkamer",I("bloedsomloop"),T("hart")),
("b","hart_kanten","Welke harthelft pompt waarheen?","<b>Rechts</b>: zuurstofarm bloed naar de <b>longen</b><br><b>Links</b>: zuurstofrijk bloed naar het <b>lichaam</b>",I("hart"),T("hart")),
("b","hartkleppen","Noem de 4 hartkleppen in de volgorde van de bloedstroom.","<ol><li><b>Tricuspidalisklep</b> (rechtervoorkamer → rechterkamer)</li><li><b>Pulmonalisklep</b> (→ longslagader)</li><li><b>Mitralisklep</b> (linkervoorkamer → linkerkamer)</li><li><b>Aortaklep</b> (→ aorta)</li></ol>","Kleppen zorgen voor eenrichtingsverkeer.",T("hart")),
("b","prikkelgeleiding","Welke twee knopen sturen het samentrekken van het hart aan?","<b>SA-knoop</b> (sinusknoop): voorkamers trekken samen<br><b>AV-knoop</b> (atrioventriculaire knoop): geeft het signaal door naar de kamers",I("prikkelgeleiding"),T("hart")),
("c","bloedvolume","Een volwassene heeft {{c1::5 à 6 liter}} bloed (± {{c2::7}} % van het lichaamsgewicht).","",T("hart","bloed")),
("b","bloed_samenstelling","Waaruit bestaat het bloed?",ul("<b>Plasma</b>: eiwitten (stolling, afweer, transport)","<b>Rode bloedcellen</b>: hemoglobine → zuurstoftransport","<b>Witte bloedcellen</b>: afweer","<b>Bloedplaatjes</b>: stolling"),"",T("hart","bloed")),
("b","hemoglobine","Wat is hemoglobine?","Een eiwit met <b>ijzer</b> in de rode bloedcellen dat <b>zuurstof draagt</b>","",T("hart","bloed")),
("b","polsplaatsen","Waar kan je de pols voelen (benoem ook de slagader)?",ul("Hals: <b>a. carotis</b>","Bovenarm: <b>a. brachialis</b>","Pols: <b>a. radialis</b>","Lies: <b>a. femoralis</b>","Knieholte: <b>a. poplitea</b>","Binnenkant enkel: <b>a. tibialis posterior</b>","Voetrug: <b>a. dorsalis pedis</b>"),"",T("hart","pols")),
("b","pericard","Hoe heet het zakje rond het hart?","Het <b>pericard</b> (hartzakje)","Een ontsteking ervan geeft hevige, stekende pijn.",T("hart")),
("b","trombose_kransslagader","Waarom is een bloedprop vooraan in de kransslagader erger dan in een uiteinde?","Vooraan blokkeert ze de <b>volledige</b> toevoer; in een uiteinde enkel een vertakking","",T("hart")),
("b","belang_hart","Waarom zijn de hersenen het eerste slachtoffer als de circulatie stopt?","Zonder circulatie geen zuurstoftransport, en <b>zenuwcellen zijn zeer afhankelijk van zuurstof</b>","",T("hart","examen")),
# Bewegingsstelsel
("b","bewegingsapparaat","Wat zijn de 4 elementen van het bewegingsapparaat?",ul("<b>Spieren</b>: samentrekken → beweging","<b>Pezen</b>: verbinden spier met bot","<b>Ligamenten</b> (gewrichtsbanden): verbinden bot met bot","<b>Botten</b>: het raamwerk"),"",T("beweging")),
("b","pees_ligament","Wat is het verschil tussen een pees en een ligament?","<b>Pees</b>: spier ↔ bot<br><b>Ligament</b>: bot ↔ bot (steun voor een gewricht)","",T("beweging")),
("c","skelet_aantal","Het skelet telt {{c1::206}} beenderen; er zijn {{c2::24}} ribben (12 per kant).",I("skelet"),T("beweging","skelet")),
("b","arm_beenderen","Welke beenderen zitten in de arm?","<b>Opperarmbeen</b> (humerus), <b>spaakbeen</b> (radius) en <b>ellepijp</b> (ulna)","",T("beweging","skelet")),
("b","been_beenderen","Welke beenderen zitten in het been?","<b>Dijbeen</b> (femur), <b>scheenbeen</b> (tibia) en <b>kuitbeen</b> (fibula)","",T("beweging","skelet")),
("b","gewricht","Uit welke delen bestaat een gewricht?",ul("Twee beenderen","<b>Kraakbeen</b>","<b>Gewrichtsvocht</b>","<b>Gewrichtsbanden</b> (ligamenten)","<b>Gewrichtskapsel</b>"),I("gewricht"),T("beweging")),
("b","spiertypes","Welke 3 soorten spieren zijn er?",ul("<b>Skeletspieren</b>: willekeurig","<b>Gladde spieren</b>: onwillekeurig (darmen, bloedvaten, blaas)","<b>Hartspier</b>: aparte categorie, eigen elektrische prikkel"),"",T("beweging")),
# Spijsvertering
("b","spijsvertering_weg","Welke weg legt voedsel af door het spijsverteringsstelsel?","Mond → <b>slokdarm</b> (peristaltiek) → <b>maag</b> → <b>dunne darm</b> (opname voedingsstoffen) → <b>dikke darm</b> (vocht onttrekken)",I("spijsvertering"),T("spijsvertering")),
("b","lever_functie","Wat doet de lever?","Stoffen <b>opslaan</b> als reserve (suikers, vitaminen), omvormen tot bruikbare stoffen en <b>ontgiften</b>","",T("spijsvertering")),
("b","belang_lever","Waarom is een stomp in de bovenbuik gevaarlijk?","De lever is sterk doorbloed → kans op een <b>hevige inwendige bloeding</b>","",T("spijsvertering","examen")),
("b","belang_darmscheur","Waarom is een scheur in het spijsverteringsstelsel gevaarlijk (naast de bloeding)?","De inhoud komt in de buikholte → kans op een <b>hevige infectie</b>","",T("spijsvertering","examen")),
# Urogenitaal
("b","urine_weg","Welke weg volgt urine?","<b>Nier</b> (zuivert bloed) → <b>urineleider</b> → <b>blaas</b> (opslag) → <b>urinekanaal</b>",I("nieren"),T("urogenitaal")),
("b","belang_nieren","Waarom kan een stoot op de buik/flank tot grote bloedingen leiden?","Naar de nieren lopen <b>grote slagaders</b>","",T("urogenitaal","examen")),
# Klieren
("b","endo_exocrien","Wat is het verschil tussen endocrien en exocrien?","<b>Endocrien</b>: klier scheidt hormonen rechtstreeks af in de <b>bloedbaan</b><br><b>Exocrien</b>: via een eigen <b>afvoerkanaal</b> (bv. verteringssappen)","",T("klieren")),
("b","insuline_glucagon","Wat doen insuline en glucagon?","<b>Insuline</b>: bloedsuiker <b>daalt</b><br><b>Glucagon</b>: bloedsuiker <b>stijgt</b><br>Beide uit de <b>pancreas</b>","",T("klieren")),
("b","schildklier","Wat regelt de schildklier?","De snelheid van de <b>stofwisseling</b> (metabolisme)","",T("klieren")),
("b","bijnier","Welke hormonen maakt de bijnier?","<b>Adrenaline / noradrenaline</b> (acute stress, fight or flight) en <b>cortisol</b> (langdurige stress)","",T("klieren")),
("b","belang_pancreas","Wat is het gevolg van een probleem met de pancreas voor de HVA?","Een <b>insulineprobleem</b> → ontregelde suikerhuishouding (hypo-/hyperglycemie)","",T("klieren","examen")),
# Afweer
("b","antigenen","Hoe noemen we de indringers die het afweerstelsel aanvalt?","<b>Antigenen</b> (virussen, bacteriën, …)","De antilichamen heten immunoglobulinen (gemaakt door B-cellen).",T("afweer")),
("b","belang_afweer","Waar let je extra op bij een patiënt met een immuunstoornis?","Extra aandacht voor <b>hygiëne</b>","",T("afweer","examen")),
# Zintuigen
("b","oog_weg","Welke weg volgt licht in het oog?","Pupil → <b>lens</b> → <b>netvlies</b> (retina) → <b>oogzenuw</b> → hersenen","Waar de oogzenuw vertrekt zit de blinde vlek.",T("zintuigen","oog")),
("b","oog_delen","Wat zijn hoornvlies, iris en sclera?","<b>Hoornvlies</b> (cornea): doorzichtig laagje vooraan<br><b>Iris</b>: gekleurd vlies dat de pupil groter/kleiner maakt<br><b>Sclera</b>: het witte, stevige deel",I("oog"),T("zintuigen","oog")),
("b","belang_oog","Waarom kijk je naar de pupillen bij een neurologisch probleem?","Hersenaandoeningen kunnen <b>verschillen in pupilgrootte</b> geven: een eerste teken van een neurologisch probleem","",T("zintuigen","examen")),
("b","oor_weg","Hoe wordt geluid omgezet tot een zenuwsignaal?","Oorschelp → <b>trommelvlies</b> → <b>gehoorbeentjes</b> (hamer, aambeeld, stijgbeugel) → <b>slakkenhuis</b> → gehoorzenuw",I("oor"),T("zintuigen","oor")),
("b","buis_eustachius","Wat doet de buis van Eustachius?","Verbindt het middenoor met de <b>keelholte</b> → gelijke druk aan beide kanten van het trommelvlies","",T("zintuigen","oor")),
("b","evenwichtsorgaan","Waar zit het evenwichtsorgaan?","In het <b>binnenoor</b>: drie halfcirkelvormige kanalen (zoals een waterpas in 3 richtingen)","",T("zintuigen","oor")),
("b","belang_oor","Wat kan wijzen op …<br>a) oorpijn na een luide knal/explosie?<br>b) roze vocht uit het oor?","a) Een <b>gescheurd trommelvlies</b><br>b) Een <b>schedelbasisbreuk</b> (bloed + hersenvocht)","",T("zintuigen","examen")),
("b","huid_lagen","Wat zijn de 3 lagen van de huid?",ul("<b>Opperhuid</b> (epidermis / hoornlaag)","<b>Lederhuid</b> (dermis): zenuwen, talg- en zweetklieren","<b>Onderhuid</b> (hypodermis): vet, haarwortels, bloedvaten"),I("huid"),T("zintuigen","huid")),
("b","belang_huid","Waarom moet je de huidlagen kennen als HVA?","Om de <b>ernst van brandwonden</b> en letsels door bijtende stoffen in te schatten","",T("zintuigen","examen")),
]
media=sorted(glob.glob("h3media/*"))
out,n=build(3,"Anatomie DGH","Anatomie",cards,media,"../content/Source/Anki")
print(out,n)
