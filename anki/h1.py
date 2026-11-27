import sys; sys.path.insert(0,".")
from dgh_common import *
T=lambda *x:["H1"]+[f"H1::{t}" for t in x]
cards=[
# Organisatie
("c","dgh_betekenis","{{c1::DGH}} staat voor {{c2::Dringende Geneeskundige Hulpverlening}}.","",T("organisatie")),
("c","dgh_definitie","DGH = het {{c1::onmiddellijk}} verstrekken van de {{c2::aangepaste}} hulp aan {{c3::alle}} personen.","",T("organisatie")),
("c","wet_1964","De DGH is geregeld door de wet van {{c1::8 juli 1964}} betreffende de dringende geneeskundige hulpverlening.","",T("organisatie","wetgeving")),
("c","opleiding_kb","De opleiding en bijscholing van de HVA worden geregeld door de {{c1::Koninklijke Besluiten}} van 13 februari en 19 maart 1998 en 23 maart 1999.","",T("organisatie","wetgeving")),
("b","oproepnummer","Wat is het oproepnummer voor dringende geneeskundige hulpverlening?","<b>112</b>","Historisch: 900 → 100 → 112",T("organisatie")),
("b","voor_1964","Wie moest vóór de wet van 1964 iedere persoon in nood helpen?","De <b>commissies van openbare onderstand</b> <i>(= huidig OCMW)</i>, op het grondgebied van hun gemeente","Enkel ziekenhuizen van die commissies waren verplicht slachtoffers op te nemen.",T("organisatie","historiek")),
# Noodcentrale
("b","calltaker","Hoe heet de 'aangestelde' van de noodcentrale 112?","De <b>calltaker-operator 112</b>","",T("noodcentrale")),
("b","opvorderingsrecht","Waarvoor heeft de calltaker-operator 112 een opvorderingsrecht?",ul("De <b>hulpverlening</b>","Het <b>transport</b>","Het <b>onthaal in een aangepast ziekenhuis</b>"),"",T("noodcentrale")),
("b","middelen_nc112","Op welke middelen kan de NC 112 beroep doen?",ul("Ambulance 112","MUG","PIT","PIT/P (PIT + MUG-arts)","Arts of huisarts van wacht"),"",T("noodcentrale")),
("c","pit","PIT staat voor {{c1::Paramedisch Interventie Team}}.","",T("noodcentrale","slides")),
# Ambulancediensten
("b","ambulancedienst_taak","Waarvoor staan de ambulancediensten in?","Het <b>transport</b> van patiënten","Zowel openbaar (brandweer, ziekenhuis) als privé (met overeenkomst met de Staat)",T("ambulancedienst")),
("b","ambulance_eisen","Aan welke eisen moeten ambulancediensten voldoen (FOD Volksgezondheid)?",ul("Voertuigen met het <b>minimale materiaal</b>","Personeel met een <b>geldig brevet</b> DGH","<b>Badge</b> FOD Volksgezondheid"),"",T("ambulancedienst")),
("b","badge","Wat moet je met je badge van de FOD Volksgezondheid doen tijdens je dienst?","<b>Verplicht zichtbaar dragen</b>","Bewijs van je officiële opleiding",T("ambulancedienst")),
("b","badge_foto",'<img src="dgh_h1_s18_1.png"><br>Wat is dit en wat doe je ermee?',"De <b>badge</b> hulpverlener-ambulancier van de FOD Volksgezondheid → in functie <b>verplicht zichtbaar dragen</b>","",T("ambulancedienst","foto")),
("b","enkel_polo","Waarom mag je als HVA niet enkel in een polo in enamelblauw rijden?","Je bent dan <b>niet verzekerd</b>","Ambulancekledij moet fluogeel + enamelblauw zijn.",T("ambulancedienst","kledij")),
("b","stol_kleuren",'<img src="dgh_h1_s19_1.png"><br>Waar staat elke kleur van de Star of Life voor?',ul("<b>Blauw</b>: hulpverlener-ambulancier","<b>Groen</b>: verpleegkundige","<b>Rood</b>: arts"),"Verpleegkundige = met bijzondere beroepstitel spoed en intensieve zorgen",T("ambulancedienst","kledij","foto")),
("c","stol_plaats","De Star of Life hangt op de {{c1::rechterborst}} en op de {{c2::rug}}.","",T("ambulancedienst","kledij")),
("b","fgi_bevoegdheid","Welke bevoegdheid heeft de federale gezondheidsinspecteur?","Een <b>politionele bevoegdheid</b> op eigen grondgebied","",T("ambulancedienst")),
# MUG
("c","mug_betekenis","MUG staat voor {{c1::Mobiele UrgentieGroep}}.","",T("mug")),
("b","mug_samenstelling","Uit wie bestaat een MUG?","<b>Arts + verpleegkundige</b>","",T("mug")),
("b","mug_tussenkomst","Op wiens vraag komt de MUG tussen?","<b>Enkel op vraag van het HC 112</b> <i>(noodcentrale)</i>","",T("mug")),
("b","mug_vertrekbasis","Wat is de vertrekbasis van de MUG?","Het <b>ziekenhuis</b> <i>(de MUG is een ziekenhuisfunctie)</i>","",T("mug")),
("c","sih","{{c1::SIH}} staat voor {{c2::Snelst Inzetbaar Hulpteam}}: de waarborg voor de bevolking (programmatie MUG).","",T("mug")),
# Ziekenhuis bestemming
("b","zh_bestemming","Naar welk ziekenhuis rijdt een ziekenwagen standaard?","Het <b>dichtstbijzijnde</b> ziekenhuis met een erkende functie <b>gespecialiseerde spoedgevallenzorg</b>","Wordt meegegeven door het HC 112.",T("ziekenhuis")),
("b","zh_afwijkingen","Wanneer mag je afwijken van het dichtstbijzijnde ziekenhuis? (volgens de slides)",ul("Op vraag van de <b>arts MUG</b>","Bij een <b>collectieve noodsituatie</b> (ramp)","Als <b>specifieke diagnostische of therapeutische middelen</b> nodig zijn","Met een <b>attest van de behandelende arts</b>"),"Afwijkingen zijn zeldzaam.",T("ziekenhuis","slides")),
("b","zh_kind","Wat moet je doen als de noodcentrale niet weet dat je patiënt een kind is?","<b>Melden</b>: er moet ook gespecialiseerde <b>pediatrie</b> aanwezig zijn in het ziekenhuis","",T("ziekenhuis")),
# Commissies
("b","commissie_dgh","Wat is de commissie voor dringende geneeskundige hulpverlening?","Een <b>coördinatie-instrument</b> tussen alle betrokken instanties, opgericht in <b>iedere provincie</b>","",T("organisatie","commissie")),
("b","commissie_leden","Wie zetelt in de provinciale commissie voor DGH?",ul("Vertegenwoordiger 112-diensten","Vertegenwoordiger MUG-diensten","Vertegenwoordiger spoedgevallendiensten","Vertegenwoordiger huisartsen"),"",T("organisatie","commissie")),
# Verantwoordelijkheden
("b","verplichte_bijstand","Wat als je als HVA een opvordering van de NC 112 weigert?","<b>Strafrechtelijke vervolging</b> is mogelijk","Je bent verplicht bijstand te geven aan personen in nood.",T("verantwoordelijkheden")),
("b","kennis_kunde","Hoe moet een HVA handelen volgens de wet?","Steeds volgens zijn <b>kennis en kunde</b>: niet meer en niet minder","bv. reanimeren moet je kunnen, maar een infuus prikken mag je niet.",T("verantwoordelijkheden")),
("b","nalatigheid_gevolg","Waarvan is er sprake als een HVA niet volgens zijn kennis en kunde handelt?",ul("<b>Onvrijwillige slagen en verwondingen</b>","of <b>onopzettelijke doding</b>"),"",T("verantwoordelijkheden")),
("c","art458","Het beroepsgeheim wordt bestraft door artikel {{c1::458}} van het strafwetboek.","",T("verantwoordelijkheden","beroepsgeheim")),
("b","beroepsgeheim_voorwaarden","Aan welke 3 voorwaarden moet informatie voldoen om onder het beroepsgeheim te vallen?",ul("Ontvangen <b>omwille van je beroep</b> (of tijdens de uitoefening)","Een <b>geheim karakter</b> hebben","<b>Toevertrouwd</b> zijn"),"",T("verantwoordelijkheden","beroepsgeheim")),
("b","geheim_karakter_vb","Is 'er is een auto-ongeval gebeurd' beroepsgeheim? En 'de bestuurder had gedronken'?","Het ongeval: <b>nee</b> (iedereen ziet het)<br>Gedronken: <b>ja</b> (geheim karakter)","",T("verantwoordelijkheden","beroepsgeheim")),
("b","geheim_collegas","Mag je patiëntgegevens uitwisselen met collega's?","<b>Ja</b>, als het doel is <b>zorg te verstrekken</b>","Bv. overdracht aan het ziekenhuis.",T("verantwoordelijkheden","beroepsgeheim")),
("b","getuigenis_rechte","Je wordt opgeroepen voor een getuigenis in rechte. Moet je je beroepsgeheim doorbreken?","Je <b>mag</b>, maar je <b>moet niet</b>: je beslist zelf, in eer en geweten","Getuigenis voor burgerlijke rechter, strafrechter, onderzoeksrechter of parlementaire commissie. Medewerking met de politie valt hier NIET onder.",T("verantwoordelijkheden","beroepsgeheim","slides")),
("b","wet_verplicht_melden","In welke gevallen verplicht de wet je een geheim bekend te maken?",ul("Patiënt is <b>slachtoffer van een misdrijf</b> en kan zelf niet beslissen (bv. bewusteloos)","<b>Kindermishandeling</b> (best via arts / vertrouwensartscentrum)","Patiënt is slachtoffer van een <b>ongeval op de openbare weg</b> en wordt door de 112-dienst naar het ziekenhuis gebracht"),"",T("verantwoordelijkheden","beroepsgeheim")),
("b","nood_breekt_wet","Wanneer mag je het beroepsgeheim nog doorbreken? (andere uitzonderingen)",ul("Als <b>zwijgen de directe dood</b> van andere personen betekent: 'nood breekt wet' (art. 422bis)","Voor je eigen <b>wettelijke verdediging</b> (vraag juridisch advies)"),"",T("verantwoordelijkheden","beroepsgeheim")),
("b","burgerlijke_aansprakelijkheid","Wat is burgerlijke aansprakelijkheid?","De wettelijke verplichting om <b>schade te vergoeden</b> die je door een fout, onachtzaamheid of nalatigheid aan iemand anders berokkend hebt","",T("verantwoordelijkheden","aansprakelijkheid")),
("b","contractueel","Wie dekt de burgerlijke aansprakelijkheid van een contractueel tewerkgestelde HVA? En wanneer niet?","De <b>werkgever</b>, behalve bij:"+ul("Frauduleus optreden","Zware fouten","Lichte fouten bij herhaling"),"",T("verantwoordelijkheden","aansprakelijkheid")),
("b","statutair","Wie is verantwoordelijk bij een fout van een statutair tewerkgestelde HVA?","De HVA <b>zelf, samen met de instelling</b> <i>(je maakt deel uit van de instelling)</i>","",T("verantwoordelijkheden","aansprakelijkheid")),
("b","bewijslast_fout","Wie moet wat bewijzen bij een fout van een HVA?","Het <b>slachtoffer</b> moet bewijzen dat de schade het <b>rechtstreeks gevolg</b> is van de fout","",T("verantwoordelijkheden","aansprakelijkheid")),
("b","primaire_balans","Is het een fout als je nalaat een primaire balans (eerste beoordeling) te maken?","<b>Ja</b>","",T("verantwoordelijkheden","aansprakelijkheid","slides")),
# Weigering transport
("b","weigering_inlichten","Een patiënt weigert transport. Wat moet je als HVA altijd doen?",ul("De patiënt <b>inlichten</b> over zijn toestand en de gevolgen van weigeren","Bij een kritieke toestand: toch <b>MUG/arts</b> inroepen","Weigeringsdocument laten ondertekenen en overlopen","Indien mogelijk een <b>agent</b> als getuige"),"",T("verantwoordelijkheden","weigering")),
("b","weigering_document","Welke juridische waarde heeft een ondertekend weigeringsdocument?","<b>Geen juridische waarde</b>, maar de rechtbank kan het wel in aanmerking nemen","",T("verantwoordelijkheden","weigering","slides")),
("b","weigering_bewijslast","De zieke loopt letsels op na een weigering. Wat moet hij/zij bewijzen?","Dat hij <b>geen toestemming</b> gaf, of dat het <b>geen geïnformeerde</b> toestemming was","",T("verantwoordelijkheden","weigering")),
# Taken
("b","voorbereidende_taken","Wat zijn de voorbereidende taken van een HVA voor de shift?",ul("<b>Persoonlijk</b>: orde en netheid (nagels, haar, ...)","<b>Voertuig</b>: technisch in orde, materiaal opgeladen en aanwezig, net","<b>Administratief</b>: boorddocumenten en registratieformulieren aanwezig"),"",T("taken")),
("b","oproep_noteren","Wat noteer je bij het beantwoorden van een oproep?",ul("Adres","Oproepuur","Ritnummer"),"",T("taken")),
("b","radiomeldingen","Welke radiomeldingen geef je tijdens een rit?",ul("Vertrokken","Ter plaatse","Vertrokken naar ziekenhuis","Aankomst ziekenhuis","Terug beschikbaar","Terug op standplaats"),"Via het ASTRID-systeem",T("taken")),
("b","behandeling_plaats","Welke handelingen mag je ter plaatse stellen?","Enkel handelingen volgens het <b>handboek</b> én op de <b>lijst van toegelaten handelingen</b>","",T("taken")),
("b","rapportering","Aan wie rapporteer je steeds?",ul("Een aanwezig <b>MUG-team / huisarts</b>","De ontvangende <b>spoedgevallendienst</b>"),"Bv. via het registratieformulier of AMBUREG",T("taken")),
("b","prioritair_uitzonderingen","Met zwaailicht en sirene mag je afwijken van de wegcode, behalve van ... ?",ul("De bevelen van een <b>bevoegd persoon</b> (politie)","Het <b>gsm-verbod</b> achter het stuur","De <b>gordelplicht</b>","Het verbod om op <b>spoorwegen</b> stil te staan","En: <b>niet roekeloos</b> rijden en anderen in gevaar brengen"),"Anders ben je ook burgerlijk aansprakelijk.",T("taken","prioritair_rijden")),
("b","prioritair_wanneer","Wanneer mag je prioritair rijden?","Enkel als het <b>toegestaan</b> is: de rit heeft prioriteit (<b>levensgevaar</b>)","",T("taken","prioritair_rijden")),
("b","houding_hva","Welke houding verwacht men van een HVA? (noem er een paar)",ul("Stiptheid","Verantwoordelijkheid","Integriteit","Empathie","Professionaliteit","Collegialiteit","Tact","Taalgebruik","Persoonlijke hygiëne","Kledij","Correct gsm-gebruik"),"",T("taken","houding","slides")),
]
out,n=build(1,"Wetgeving DGH","Wetgeving",cards,["h1media/dgh_h1_s19_1.png","h1media/dgh_h1_s18_1.png"],"../content/Source/Anki")
print(out,n)
