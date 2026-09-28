from replay import *
import csv

def read(n):return json.loads((OUT/(n+'.json')).read_text())
def mdtable(headers,rows):return '\n'.join(['| '+' | '.join(headers)+' |','|'+'|'.join(['---']*len(headers))+'|']+['| '+' | '.join(str(v).replace('|','/') for v in r)+' |' for r in rows])
def fmt(v,n=2):return 'ND' if v is None else f'{v:.{n}f}'
def stamp(v):return v.replace('2026-09-','').replace('T',' ').replace('+00:00','')
M=read('metrics');A=read('archive_summary');F=read('first_events');B=read('first_ready_books')
sections=[]
sections.append('''# Audit adversarial Solaire — issue #89 — snapshot du 27/09/2026

**Verdict : l’hypothèse est partiellement confirmée, mais l’explication « le Decision Layer a bloqué QNT/KMNO/TREAD avant leur alerte » est réfutée.** Les trois ont produit un BUY_SENT et un email d’achat retrouvé dans Gmail. TREAD fournit un cas explicite de mauvaise justification dans le chat ; pour QNT/KMNO, le point exact de non-exécution par l’utilisateur n’est pas démontrable. Aucun journal d’ordres ne permet d’assimiler une alerte à une position réellement ouverte.

Le défaut aval le mieux établi combine une restitution incomplète des décisions, une confusion entre nouveaux candidats et thèses déjà alertées, et des journaux parallèles pris à tort pour une chaîne séquentielle. Les gates d’exécution expliquent la majorité des rejets enregistrés ; leur caractère excessif n’est pas prouvé par la hausse ultérieure. Le test économique ne justifie aucune promotion immédiate.

## Périmètre, causalité et preuves

- Référence immuable des données : `0fbc84babfe8567d40979e2a3f695ca57c001182`. Reprise comparée à `1ee4d8439ecf02d977b8b3f0c860f4fd9c913067` : 89 commits, 133 fichiers modifiés, aucun changement Python/workflow entre ces deux états. Aucun patch de production effectué.
- Snapshot adversarial : **27/09 00:47 UTC**, soit 02:47 à Paris. Les pourcentages +24 h sont ceux fournis par l’utilisateur ; ils ne servent à aucune règle de sélection.
- Fenêtre d’archives : **21/09 00:00:26.028393 → 27/09 00:25:24.256106 UTC**, 543 scans, 426–427 marchés par scan, 739 873 bougies 5 minutes distinctes. 544 archives récupérées, une après le cutoff effectif exclue. SHA Git des octets compressés vérifiés. Dernière bougie complète : 00:20–00:25 UTC.
- Journal production exploitable à partir du 21/09 09:35:08.781284 ; l’email KMNO du matin est donc hors de ce journal, mais retrouvé séparément. V3 commence le 23/09 22:09 ; V3.1 le 23/09 23:22 ; mémoire le 24/09 20:30. Ce sont des censures à gauche, pas des absences de signal.
- Les décisions proviennent uniquement de champs enregistrés avant leur timestamp ; les champs `evaluations` ne sont jamais utilisés pour sélectionner. Les bougies futures servent exclusivement à mesurer les fills hypothétiques et les résultats. Horaires ci-dessous **UTC** ; ajouter deux heures pour Paris.
- Une décision de production, un PASS shadow, une qualification V3.1, une allocation shadow, un email, une réponse du chat et un ordre réel sont des objets distincts. Deux validations à quelques secondes d’écart peuvent donner des prix ou des verdicts différents.

**Limites non résolues :** absence de profondeur complète côté bid, frais du compte non vérifiés, absence des tickets d’ordre et des transcriptions intégrales ChatGPT. Le ledger funnel conservé ne commence que le 26/09 à 20:25 ; il ne reconstruit pas rétroactivement les allocations du 21–25. Aucun journal autonome nommé V3.5 n’a été identifié : les états d’allocation disponibles sont conservés tels quels, sans inventer une étape V3.5 ni un veto. Le replay est une simulation causale des décisions, avec un modèle d’exécution, pas une preuve d’exécution historique ni une validation hors échantillon.

## Le funnel réel

La production suit **accélération → éligibilité → validation exécution → prior thesis → sender → email**. Le payload porte `v4_required=False` et `decision_layer_required=False` ; le sender traite les candidats avec `limit=None` et regroupe les candidats validés dans le mail. Il n’applique pas un top 3 du Decision Layer à l’envoi.

En parallèle, V4 alimente un Decision Layer `DECISION_LAYER_V1_SHADOW`. V3 produit des hypothèses et validations shadow ; V3.1 qualifie économiquement des entrées ; mémoire et allocations suivent leurs propres états. Leur présence dans un schéma conceptuel ne prouve pas qu’ils aient causé un rejet en production.

## 1. Tableau des dix actifs

« Premier signal » signifie premier BUILDING ou CONFIRMED observé dans la fenêtre, sans prétendre au premier signal absolu. « Actionable » distingue ici production et shadow ; le premier ACHETE_MAINTENANT du DL figure séparément dans la chronologie. Un PASS technique seul ne suffit pas à recommander l’entrée.
''')

changes=dict(zip(TARGETS,[60.20,57.19,47.07,28.69,21.38,19.33,16.90,15.48,15.21,14.79]))
confirm_override={'KMNO':('21 02:52:35','0,029897 (signal du mail)'), 'AGI':('21 14:35:06.464572','0,005154 (production)'), 'RUNE':('22 13:18:59.284728','0,57712 (production)'), 'COW':('24 14:42:12.992751','0,12603 (production)')}
passmap={'QNT':'24 13:59:24.097639 ; 69,091 €','KMNO':'21 02:52:35 au plus tard ; mail 0,029925 €','TREAD':'21 10:04:59.447374 ; 0,38501 €','RARE':'25 21:32:48.048104 ; 0,014528 €'}
buyable={'QNT':'V3 technique 24 12:22:30.150763 à 64,868 ; V3.1 qualifié 13:02:30.669584 à 66,098 ; production 13:59:24. 100 € plausible ; 150 € dépasse le budget de risque sur le plan production.',
'KMNO':'21 02:52:35 au plus tard, mail 0,029925 ; 100–150 € compatibles avec le montant guide, profondeur contemporaine non conservée.',
'TREAD':'21 10:04:59.447374, 0,38501 ; puis 22 18:47:42.106827, 0,470. 100 € compatible ; 150 € au 22/09 supérieur au montant guide 140,82.',
'AMP':'Premier achat shadow qualifié : 26 19:07:29.238372, entrée 0,000639074582. 100 € techniquement plausible ; 150 € dépasse le risque 12 € du carnet proche.',
'RARE':'25 21:32:48.048104 production à 0,014528. READY technique dès 17:47:23.698099 à 0,014548, qualification économique refusée ensuite. Pas de rétro-validation de ce READY.',
'HFT':'Non établi : aucun PASS ni carnet contemporain suffisant des rejets volume.',
'2Z':'24 14:43:35.159205 V3.1 qualifié à 0,04809 ; benchmark profondeur 100 € OK. 150 € non certifiable à cet instant.',
'RUNE':'Technique seulement le 26 09:21:15.284183 à 0,61435 ; V3.1 refuse le score économique. Premier achat raisonnable non établi avant cutoff.',
'COW':'Non établi : confirmation bloquée par volume, pas de PASS technique exploitable retrouvé.',
'AGI':'Technique le 26 22:44:28.956561 à VWAP100 0,006016320176 ; pas de qualification V3.1 avant cutoff, horizon 4 h incomplet.'}
causes={'QNT':'Aucun raté sender sur le premier PASS ; 4 rejets stop ultérieurs. Restitution/lecture/exécution utilisateur non retraçable complètement.',
'KMNO':'Emails présents dès le 21 et le 24 ; 3 autres épisodes bloqués par range. Pas de preuve d’un veto DL sur le PASS.',
'TREAD':'Mail présent ; refus ChatGPT du 22/09 motivé par absence de candidat. Deux suppressions prior thesis le 23 ; nombreux rejets stop/spread distincts.',
'AMP':'Production : 5 volume + 8 spread. Aucune recommandation production ; qualification shadow tardive. Les 2 rejets stop évoqués dans le constat initial appartiennent au shadow.',
'RARE':'5 volume + 6 stop + 3 spread, mais 2 achats envoyés. Premier PASS production plus tôt que le premier PASS shadow cité.',
'HFT':'9/9 rejets production INSUFFICIENT_EXECUTION_LIQUIDITY. Conservatisme à 100 € non démontré faute de carnet aux instants refusés.',
'2Z':'2 range + 1 spread + 2 stop ; V3.1 shadow qualifie une entrée. Dans C1, le range5 peut ajouter une entrée ; dans C2 à 100 €, capacité empêche la première.',
'RUNE':'Confirmation production bloquée STRUCTURAL_RANGE_TOO_NARROW. Le READY V3 ultérieur reste économiquement non qualifié.',
'COW':'INSUFFICIENT_EXECUTION_LIQUIDITY en production ; WIDE_SPREAD_RISK dans la route DL, cause parallèle à ne pas cumuler.',
'AGI':'8 volume + 1 spread production ; 8 événements seulement dans le sous-ensemble shadow initial. Fin de fenêtre trop proche pour valider le trade technique.'}
verdict={'QNT':'Transport OK ; défaut de restitution plausible, attribution exacte non prouvée','KMNO':'Transport et restitution de mails antérieurs prouvés ; non-achat non attribuable précisément','TREAD':'Erreur de justification ChatGPT établie par contexte retrouvé ; prior thesis secondaire','AMP':'Gate production responsable des rejets ; relâchement global non justifié','RARE':'Prémisse « premier achat à 0,020686 » réfutée ; premiers trades simulés perdants','HFT':'Veto volume certain ; faux négatif économique non démontré','2Z':'Range5 capture ce cas mais détériore le portefeuille 100 €/4 h','RUNE':'Gate range ; aucun achat raisonnable démontré dans la fenêtre','COW':'Volume en production ; données insuffisantes pour contrefactuel petite taille','AGI':'Volume/spread ; aucune preuve de gain capturable sur le +24 h'}
table=[];db=sqlite3.connect(OUT/'bars.sqlite')
for s in TARGETS:
 f=A['first'].get(s+'-EUR',{});sig=f.get('first_building_or_confirmed');conf=f.get('first_confirmed');e=F.get(s+'-EUR',{})
 cf=(stamp(conf['at_utc'])+' ; '+str(conf['price'])) if conf else 'Non observée dans les archives'
 if s in confirm_override:cf=' ; '.join(confirm_override[s])
 ts=datetime.fromisoformat(sig['at_utc']).timestamp();bars=list(db.execute('select h,l from bars where m=? and t>=? and t<?',(s+'-EUR',(int(ts)//300+1)*300000,(int(ts)//300+1)*300000+14400000)))
 move=f"MFE 4 h {100*(max(x[0] for x in bars)/sig['price']-1):+.2f} % ; MAE {100*(min(x[1] for x in bars)/sig['price']-1):+.2f} % (diagnostic depuis signal, pas PnL)" if len(bars)==48 else 'Horizon incomplet'
 act=passmap.get(s,'Aucune production')
 if s not in passmap and e.get('first_v31_selectable'):act+=' ; V3.1 shadow '+stamp(e['first_v31_selectable']['at_utc'])
 table.append({'Actif':s+'-EUR','+24 h':f'{changes[s]:+.2f} %','Premier signal UTC':stamp(sig['at_utc']),'Prix premier signal':sig['price'],'Première confirmation UTC / prix':cf,'Premier PASS production':passmap.get(s,'Aucun avant cutoff'),'Première décision actionable':act,'Premier moment raisonnablement achetable':buyable[s],'Cause exacte / couche':causes[s],'Mouvement après signal':move,'Verdict':verdict[s]})
csvout('Tableau_10_actifs',table);sections.append(mdtable(list(table[0]),[list(r.values()) for r in table]))
sections.append('''
La table conserve les fractions de seconde quand elles existent. L’email KMNO 02:52:35 est une borne supérieure de la validation, pas un timestamp de gate inventé. Les archives du scanner legacy et les cycles du scan direct n’ont pas les mêmes horaires ; les premières confirmations production sont donc parfois antérieures à celles des archives.

## 2. QNT / KMNO / TREAD : suivi prioritaire

### QNT

| Étape | UTC | Prix / état exact |
|---|---|---|
| DL immédiat ancien | 21/09 08:59:21.708216 | 57,932 € ; ACHETE_MAINTENANT, rang 133 ; plan exécution distinct INVALID, net RR 1,191848 |
| V2 BUILDING observé | 22/09 10:21:29.533360 | 59,75 € |
| V3 ENTRY_READY_SHADOW | 24/09 12:22:30.150763 | entrée 64,868 ; stop 62,073 ; TP1 70,457 ; spread 0,0663 % ; VWAP100 64,868 |
| V3.1 refuse le premier READY | 24/09 12:23:43.422447 | INSUFFICIENT_RELATIVE_STRENGTH ; score économique 6,048 |
| V3 persistante | 24/09 13:01:26.827553 | entrée 66,098 ; spread 0,0545 % ; benchmark100 impact nul |
| V3.1 PERSIST_30M_QUALIFIED_ENTRY | 24/09 13:02:30.669584 | SELECTABLE ; score économique 6,769 |
| V2 CONFIRMED dans archive | 24/09 13:50:02.989835 | 67,948 € ; score 8,209 |
| Cycle production | 24/09 13:58:05.394315 | signal 69,39 € ; score 8,431 |
| Gate shadow | 24/09 13:59:22.509463 | PASS + actionable, rang 1 ; entrée 69,113 ; stop 62,916 ; TP1 81,507 ; NO_TRACKED_PRIOR_BUY_THESIS |
| Décision production | 24/09 13:59:24.097639 | BUY_SENT / DELIVERED ; entrée revalidée 69,091 ; stop 62,916 ; TP1 81,44 |
| Email Gmail | 24/09 13:59:26 | QNT candidat 1/2, avant LAPTOP ; spread 0,043 % ; stop 8,94 % ; montant guide 124,92 € |

**Où a-t-il disparu ?** Pas avant le mail. Le DL n’a pas filtré ce mail. La restitution ultérieure retrouvée du 26/09 20:45:07 décrit QNT comme trop avancé, environ +9,6 % au-dessus du signal de cette journée. Elle n’explique pas le traitement du mail du 24 à 13:59. Impossible d’attribuer le non-achat du 24 au ranking, à la lecture utilisateur ou au chat sans leur jointure temporelle.

L’entrée shadow plus précoce n’est pas automatiquement un achat : celle de 12:22 a été refusée économiquement. La première qualification V3.1 retrouvée est à 13:02. Le DL du 21 est un autre avertissement : `ACHETE_MAINTENANT` n’implique pas nécessairement `trade_plan.valid`. Le consommateur doit les vérifier séparément.

### KMNO

| Étape | UTC | Prix / état exact |
|---|---|---|
| V2 BUILDING archive | 21/09 02:49:48.101486 | 0,029702 € |
| Premier email retrouvé | 21/09 02:52:35 | signal confirmé 0,029897 ; entrée 0,029925 ; stop 0,02822 ; spread 0,084 % ; montant guide 188,16 € |
| BUY_SENT suivant | 21/09 09:50:28.328058 | entrée 0,030916 ; stop 0,028836 ; email 09:50:30 |
| V3 READY | 24/09 01:56:12.492259 | entrée 0,032219 ; spread 0,0808 % ; VWAP100 0,032219328936 ; impact 0,010333 % |
| V3.1 QUALIFIED_ENTRY | 24/09 01:56:22.083088 | SELECTABLE ; score économique 6,216 |
| Cycle production | 24/09 02:33:14.383466 | signal 0,033073 ; score 7,896 |
| Gate shadow | 24/09 02:34:29.012994 | PASS + actionable ; rang 1 ; entrée 0,033009 ; stop 0,030626 ; PRIOR_BUY_THESIS_EXPIRED |
| BUY_SENT | 24/09 02:34:33.028774 | entrée 0,032992 ; stop 0,030626 ; TP1 0,037724 |
| Email Gmail | 24/09 02:34:36 | spread 0,100 % ; stop 7,17 % ; montant guide 152,94 € |
| Premier DL immédiat dans la fenêtre | 24/09 13:31:01.048568 | 0,032316 ; survient après l’email, donc pas sa condition d’envoi |

**Où a-t-il disparu ?** Aucun échec d’alerte établi. Les mails KMNO/TREAD du 21 ont même été examinés dans le chat à 11:50:15 UTC. Cela prouve une restitution au moins partielle, pas une exécution. Le traitement exact du mail KMNO du 24 reste non déterminé. Le premier trade du 24 à horizon 4 h est perdant dans le modèle : la hausse au snapshot ne transforme pas chaque entrée précédente en bonne opération.

### TREAD

| Étape | UTC | Prix / état exact |
|---|---|---|
| Première confirmation archive | 21/09 01:02:59.123557 | 0,43255 ; score 8,405 — un signal plus ancien peut être plus cher que l’achat ultérieur |
| Premier BUY_SENT | 21/09 10:04:59.447374 | entrée 0,38501 ; stop 0,36549 ; email 10:05:02 ; spread 0,003 % |
| Cycle demandé | 22/09 18:46:20.605026 | signal 0,470 ; score 6,875 |
| Gate shadow | 22/09 18:47:38.441151 | rang 3 ; PASS + actionable ; entrée 0,470 ; stop 0,43311 ; TP1 0,54377 ; PRIOR_BUY_THESIS_EXPIRED |
| BUY_SENT | 22/09 18:47:42.106827 | même entrée/stop ; pas de veto de déduplication |
| Email Gmail | 22/09 18:47:44 | montant guide 140,82 € ; spread 0,0021277 % ; range 6,7553 % ; stop 7,8489 % |
| Recommandation ChatGPT retrouvée | 22/09 19:44:15 | refus motivé par absence du dernier alert_candidates ; « je n’achète aucun » |
| Rejet prior thesis | 23/09 01:21:35.643986 | signal 0,49576 ; score 9,012 ; PRIOR_BUY_THESIS_STILL_ACTIVE |
| Rejet prior thesis | 23/09 12:01:32.570918 | signal 0,50763 ; score 6,518 ; même raison |
| Nouvel email | 23/09 21:31:06 | entrée 0,46738 ; stop 0,44389 ; spread 0,303 % |
| V3 reentry : disponibilité réelle | 25/09 00:27:16.265560 | READY à 0,61439 ; le decision_ts 00:26:17.973975 précède l’exécution, donc ne pas l’utiliser comme heure d’achat |
| V3.1 qualifie ensuite | 25/09 01:39:05.678443 | entrée 0,62099 ; score économique 6,367 |

**Maillon cassé démontrable : justification dans ChatGPT.** Un flux de nouveaux candidats n’est pas le registre des thèses actives. Une alerte sortie du flux doit être réévaluée avec prix, stop, âge et carnet ; son absence seule ne signifie ni invalidation ni nouveau feu vert. Le refus du 22 précède les deux suppressions prior thesis du 23 : ces dernières ne peuvent pas l’expliquer rétroactivement.

Le bypass de prior thesis pour un **nouvel épisode d’accélération** existe déjà dans le code repris, introduit le 25/09 (`e1a4109431a631bbdda5d91aa26a48948d4d83bd`). Il serait erroné de le proposer comme correctif encore absent. Aucune règle spécifique TREAD n’est nécessaire.

## 3. Audit des gates 100–150 €

| Protection production | Règle observée | Relation réelle à la taille | Verdict |
|---|---|---|---|
| Liquidité | volume quote 24 h ≥ 75 000 € ; vérifié avant lecture du carnet | proxy non dépendant du montant ; ne mesure pas le VWAP d’un ordre de 100 € | suspect de conservatisme, non innocenté sans carnet contemporain |
| Spread | ask/bid − 1 ≤ 0,5 % | son pourcentage ne diminue pas avec une petite position ; coût euro proportionnel | conserver ; mesurer en euros et avec profondeur |
| Profondeur | sender récupère 25 niveaux mais conserve/utilise surtout bid/ask pour cette validation | absence de preuve de VWAP 100/150 dans ce chemin | mesure manquante, pas preuve de liquidité institutionnelle |
| Stop | distance ≤ 10 % | risque euro dépend du montant, du stop et des coûts | 150 € peut être trop élevé quand 100 € est acceptable |
| Range | amplitude structurelle 15 min sur 2 h ≥ 6 % | règle de structure/économie, pas règle de profondeur | effet 6→5 % testé séparément ; résultat global défavorable à 100 €/4 h |
| Sizing | budget risque 12 €, cap notional 250 €, frais 0,25 %/côté, slippage 0,10 %/côté, RR net ≥ 1,5 | déjà dimensionné retail, non institutionnel | ajuster le montant si nécessaire ; ne pas relever le risque implicitement |

Formules : achat au VWAP des asks pour le notional ; impact = VWAP/ask − 1. Spread affiché = ask/bid − 1 ; coût d’un aller-retour au meilleur prix, sans frais ni impact = N × (1 − bid/ask). Risque des tableaux de carnets : N − N/[VWAP × (1+f)] × stop × (1−s) × (1−f), avec N budget frais inclus, f=0,0025, s=0,001. Le coût spread calculé avec N est donc un repère pour un notional N, tandis que le risque utilise un budget tout compris N ; aucune double facturation du spread dans le risque.

**Carnets READY avec asks bruts : premières observations conservées, souvent plus tardives que les premières alertes. Ils ne valident pas rétroactivement un rejet antérieur.** 1 346 snapshots sur 246 marchés ; zéro profondeur bid complète. La somme des 25 asks est informative ; le VWAP simulé utilise les niveaux nécessaires. Le carnet courant ne garantit pas le carnet lors d’un futur stop.
''')
bookrows=[]
for s in TARGETS:
 r=B.get(s+'-EUR')
 if not r:bookrows.append([s,'Non retrouvé']+['ND']*8);continue
 bookrows.append([s,stamp(r['available_utc']),fmt(r['spread_pct'],4),fmt(r['ask_depth_eur']),f"{r['vwap_100']:.12g} / {r['vwap_150']:.12g}",f"{r['impact_pct_100']:.4f} / {r['impact_pct_150']:.4f}",f"{r['spread_cost_eur_100']:.3f} / {r['spread_cost_eur_150']:.3f}",f"{r.get('risk_eur_100',0):.2f} / {r.get('risk_eur_150',0):.2f}",fmt(r.get('range_pct'),3),'Sortie non certifiable'])
sections.append(mdtable(['Actif','Carnet UTC','Spread %','Asks 25 niveaux €','VWAP 100 / 150','Impact % 100 / 150','Coût spread € 100 / 150','Risque € 100 / 150','Range %','Limite'],bookrows))
sections.append('''
AMP et RARE illustrent un point décisif : profondeur d’achat suffisante n’implique pas position de 150 € admissible. Sur ces carnets, le risque dépasse 12 € à 150 €. AGI reste exécutable mécaniquement à l’achat dans ce carnet, mais l’impact augmente de 0,0885 à 0,1791 % : il échoue à la variante conservatrice d’impact maximal 0,10 % pour 150 €.

**Premier prix exécutable des mails prioritaires :** aucune profondeur brute de sortie ne permet de le certifier. Leur spread, leur plan et leur montant guide rendent 100 € compatible avec la validation disponible ; 150 € doit être redimensionné pour QNT et TREAD au 22/09. Au plan QNT, le budget guide est 124,92 €, donc un achat de 150 € ne respecte pas le même budget de risque de 12 €.

### Prototype SMALL_SIZE_EXECUTABLE

Le fichier `small_size_shadow.py` définit une fonction pure, sans intégration production, sans symbole codé en dur. Elle peut remplacer **uniquement le proxy volume 24 h** si : signal éligible inchangé, données connues à l’instant de décision, marché ouvert, carnet bid/ask complet et frais/minimums connus, fraîcheur ≤90 s, spread ≤0,5 %, impact achat et revente immédiate ≤0,10 %, range ≥6 %, stop ≤10 %, risque ≤12 €, RR net ≥1,5. Une information manquante produit UNKNOWN, jamais PASS. Les limites de 90 s et 0,10 % sont des propositions non optimisées, à figer avant le shadow.

Les cinq assertions vérifient notamment qu’un carnet peut accepter 100 € et refuser 150 €, rejeter une observation future/périmée et retourner UNKNOWN sans bids. **Aucun nombre de captures SMALL_SIZE_EXECUTABLE n’est revendiqué historiquement**, faute de bid depth aux instants requis. Étendre les seuils de spread/stop en plus du volume serait un autre challenger, non testé ici.

## A. Diagnostic transversal

1. **Confusion de routes.** Un refus shadow ne remplace pas le verdict du sender ; RARE en fournit une contradiction directement observable. Un état DL immédiat n’est pas non plus une validation d’exécution complète.
2. **Restitution trop courte.** Le DL stocke `ranked` intégralement mais calcule `top_actionable` avec trois candidats, tous buckets confondus. Lire uniquement ce top 3 élimine des achats immédiats de l’affichage sans les supprimer des données.
3. **Mauvais cycle de vie dans le chat.** Disparition d’un candidat nouveau, mail déjà envoyé, thèse active, recommandation et position détenue ne sont pas interchangeables. TREAD démontre une justification invalide ; les preuves disponibles ne quantifient pas tous les achats perdus par le chat.
4. **Veto d’exécution à premier échec.** Le volume, le spread, le range ou le stop arrêtent la validation ; les refus volume ne conservent pas forcément le carnet. Les motifs indiquent le premier blocage, pas la totalité des contraintes qui auraient échoué ensuite.
5. **Évaluation économique historique fragile.** `evaluate_bars` ne trie pas ses bougies, utilise `bars[-1]` comme clôture et n’exige pas un horizon continu complet. L’API documente un retour du plus récent au plus ancien et des absences de bougies sans transactions. Avec les mêmes 288 bougies QNT, rendement clôture 24 h = +18,8925 % en ordre croissant et +1,4546 % en ordre décroissant ; MFE/MAE identiques. Les décomptes TP/stop peuvent aussi dépendre de l’ordre. Le replay ci-dessous ne réutilise pas ces évaluations.

Sur 543 scans : **2 468 occurrences ACHETE_MAINTENANT**, dont seulement **532 dans le top 3** ; 1 936, soit **78,4 %**, ne sont pas affichées si le consommateur se limite au top 3. Sur 473 scans contenant au moins un achat immédiat, 142 n’en ont aucun dans ce top 3. QNT : 32 occurrences, 3 dans le top 3 ; KMNO : 2, dont 1 ; TREAD : aucune. Ce sont des occurrences répétées, pas 1 936 trades indépendants manqués. Les classements recalculés sont identiques à trois archives de décisions contrôlées, avant et après le changement de version.

La logique de buckets est déterministe : immédiat exige buy_ready et Entry≥6,8 ; structure forte exige Opportunity≥7,4 et Trend≥7,3 ; pullback/reentry peut prendre priorité sur limite passive ; les hard veto incluent notamment LOW_LIQUIDITY et WIDE_SPREAD_RISK. HIGH_EXTENSION_OR_CHASE devient contexte de risque dans la version du 25/09 ; appliquer cette version à tous les jours antérieurs serait une réécriture de la baseline.

## B. Répartition des responsabilités

Il faut quantifier des événements, sans inventer une répartition des euros perdus.

| Couche | Preuve / quantité | Ce que l’on peut conclure |
|---|---|---|
| Scanner | les 10 actifs ont un signal observé ; confirmations également retrouvées par archives/production | pas de preuve justifiant un changement amont sur ces cas ; pas une mesure du recall de tout le marché |
| Decision Layer | 0 veto DL dans le chemin sender observé ; 1 936 occurrences immédiates hors top3 | problème de consommation possible, pas 1 936 échecs d’envoi |
| Execution gate | 1 437 rejets sur les 1 599 événements production ; 85 sur les 97 événements des 10 actifs | cause immédiate majoritaire des refus, sans présumer qu’ils étaient excessifs |
| Prior thesis | 37 rejets tous marchés ; 2 TREAD parmi les 10 | effet réel, secondaire dans ce corpus ; bypass nouvel épisode déjà présent |
| Email | 125 BUY_SENT dans la fenêtre journal ; 10 sur les 10 actifs, concernant QNT/KMNO/TREAD/RARE | mails prioritaires retrouvés dans Gmail ; pas d’échec de transport démontré pour ces premiers PASS |
| ChatGPT | TREAD refusé pour absence de candidat ; omission de 16 achats DL reconnue dans un échange antérieur | responsabilité de restitution établie sur des exemples ; taux global non mesurable sans transcripts complets |
| Exécution utilisateur | ordres / confirmations non disponibles | aucun achat réel ni manque à gagner réalisé attribuable avec certitude |

Le journal commence après le premier mail KMNO du 21 : les 125 BUY_SENT ne sont pas un recensement de tous les emails depuis minuit. Sur les 1 474 rejets journalisés, les causes sont volume **597**, range **400**, spread **298**, stop **142**, prior thesis **37**. Les motifs ne sont pas additionnables aux veto de routes shadow.

## C. Correctif minimal proposé

**Priorité C0 : corriger le consommateur et le registre des alertes, sans modifier les signaux.**

- Lire toutes les lignes `ranked` avec action immédiate, et présenter séparément les autres buckets. Un top 3 transversal ne doit pas être interprété comme la liste exhaustive des achats.
- Joindre chaque alerte à signal_id / episode_id / plan_id / gate timestamp / email id / état de restitution. Distinguer SENT, PRESENTED, REVALIDATION_REQUIRED, INVALIDATED et ORDER_CONFIRMED ; ne jamais déduire ORDER_CONFIRMED de SENT.
- Garder une alerte non traitée dans un registre. Si elle a vieilli, revalider prix, carnet, plan et risque avant toute recommandation. Absence du flux candidat → REVALIDATION_REQUIRED, avec motif ; pas annulation implicite.
- Exiger un plan valide et une exécution fraîche même quand le DL dit ACHETE_MAINTENANT. Le cas QNT du 21 interdit de transformer tous les buckets immédiats en achats automatiques.

Corriger séparément l’évaluateur : tri chronologique, exclusion de bougies non clôturées à l’horizon, contrôle de couverture et chemin stop/TP explicite. Ce correctif de mesure ne change pas la stratégie. Le bypass prior thesis nouvel épisode existe déjà : le mesurer prospectivement au lieu de le réimplémenter.

**Livrable avant patch respecté :** seules des extractions, simulations et fonctions hors production sont créées. Aucun changement scanner, gate, sender ou workflow ; aucun ordre.

## D. Baseline vs challengers causaux

### Règles et limites du modèle

- B = événements BUY_SENT enregistrés, sans sélection a posteriori sur les 10 gagnants.
- C1 = B + confirmations refusées uniquement par range6, mais déjà acceptées par le challenger range5 enregistré. 125 événements baseline + 66 supplémentaires sur la même fenêtre production. Ce mécanisme existait avant l’observation des gagnants.
- C2 = B + toutes les entrées V3.1 SELECTABLE (`QUALIFIED_ENTRY`, persistance et pullback inclus). Fenêtre commune à partir du 23/09 23:22:23.220478 : 65 baseline + 237 entrées supplémentaires. C2 teste l’accès à une autre route qualifiée ; il ne mesure pas l’effet isolé d’un seul gate.
- Même univers et mêmes contraintes dans chaque paire, aucune whitelist des dix actifs. Les candidats négatifs font partie du test. Les files et dispositions complètes sont livrées.
- Capital fictif constant 2 331,61 €, maximum 10 positions, une position par marché, budget 100 ou 150 € frais inclus, risque maximal 12 €. Ce capital sert au comparateur, ce n’est pas une lecture du portefeuille réel.
- Entrée au premier open 5 min strictement postérieur à la décision ×1,001, refus au-delà de la quote ×1,005 ou sous le stop ; frais supposés 0,25 % par côté. Sortie au stop si touché, avec gap au pire de open/stop puis −0,10 %, sinon clôture après 4 h (sensibilité 24 h) −0,10 %. Pas de take-profit choisi après observation. Ce test n’est pas le backtest de la gestion TP1/runner réelle.
- Les données manquantes sont UNKNOWN/INCOMPLETE ; les horizons après 27/09 00:25 sont censurés. Les MFE/MAE de l’horizon peuvent inclure l’après-stop et sont explicitement étiquetées ; les extrêmes de la bougie du stop ne révèlent pas leur ordre intrabar.
- Les frais, la profondeur à chaque entrée, la priorité dans le carnet et la latence humaine ne sont pas reconstituables pour tout l’univers. Le modèle ne démontre donc pas des fills réels. Une sensibilité sans entrée sur bougie sans transaction est fournie. Les règles de sélection sont causales, mais les valeurs de coût/exécution restent des hypothèses.

### Résultats principaux — horizon 4 h
''')
headers=['Paire / règle','Taille €','Entrées','Gagnants/perdants','Réussite %','Espérance €/trade','PnL net €','DD MTM €','Turnover achats €','Stops','Actifs des 10 capturés']
sections.append(mdtable(headers,[[x['policy'],x['stake'],x['fills'],f"{x['wins']}/{x['losses']}",fmt(x['win_rate_pct']),fmt(x['expectancy_eur']),fmt(x['net_pnl_eur']),fmt(x['mtm_drawdown_eur']),x['buy_turnover_eur'],x['stops'],', '.join(x['targets_captured'])] for x in M if x['horizon_hours']==4]))
sections.append('''
À 100 €/4 h, C1 passe de 4 à 5 actifs cibles capturés, mais dégrade le PnL de **14,61 €** et le drawdown de **16,58 €**. Il ajoute 41 trades effectivement différents, dont 27 perdants, et en déplace 4 de la baseline : net +37 trades, +23 perdants et +3 700 € de turnover achat (+38,5 %). La meilleure espérance par trade reste négative et masque un total plus mauvais.

C2 à 100 €/4 h passe de 3 à 5 actifs cibles sur sa fenêtre commune. Le PnL s’améliore de **19,74 €**, mais reste négatif ; DD +28,06 €. Il ajoute 89 trades distincts, dont 52 perdants, et déplace 11 baseline, dont 7 perdants : net +78 trades et +45 perdants ; turnover +169,6 %. « Faux positif » signifie ici trade au PnL net négatif sous la politique de sortie fixée, pas simplement baisse immédiate. Aucune précision de classification sur les non-trades n’est inventée.

À 150 €, la contrainte de risque écarte des plans encore admissibles à 100 € : on ne peut pas multiplier tous les résultats par 1,5. C1 ajoute 42 trades/29 perdants ; C2 ajoute 87 trades/49 perdants et déplace 3 baseline. Les variations de capacité expliquent pourquoi certains actifs sont capturés dans une configuration et pas dans une autre.

### Entrées et excursions ciblées, modèle 100 €/4 h
''')
trs=[]
for policy in ('C1_baseline','C1_range5','C2_v31'):
 es=list(csv.DictReader((OUT/f'trades_{policy}_100_4h.csv').open()));seen=set()
 for e in es:
  m=e['market'];s=m.split('-')[0]
  if s not in TARGETS or m in seen:continue
  seen.add(m)
  if policy=='C1_range5' and s!='2Z':continue
  trs.append([policy,s,stamp(e['entry_utc']),e['entry_eur'],fmt(float(e['risk_eur'])),fmt(float(e['mfe_horizon_pct'])),fmt(float(e['mae_horizon_pct'])),e['exit_reason'],fmt(float(e['pnl_eur']))])
sections.append(mdtable(['Route','Actif','Entrée UTC','Prix modèle €','Risque €','MFE 4 h %','MAE 4 h %','Sortie','PnL net €'],trs))
sections.append('''
Le premier RARE acheté dans la baseline touche le stop, malgré sa présence parmi les gagnants du snapshot. Une liste de gagnants journaliers n’est donc pas une liste de trades gagnants. Le QNT shadow plus précoce améliore ce cas précis ; cela ne suffit pas à valider les 237 ajouts V3.1. AGI est trop proche de la fin de fenêtre pour une évaluation complète de l’entrée technique du 26 à 22:44.

### Sensibilité à l’horizon — 24 h
''')
sections.append(mdtable(['Règle','Taille €','Entrées','Réussite %','Espérance €','PnL €','DD MTM €','Stops','Censurés'],[[x['policy'],x['stake'],x['fills'],fmt(x['win_rate_pct']),fmt(x['expectancy_eur']),fmt(x['net_pnl_eur']),fmt(x['mtm_drawdown_eur']),x['stops'],x['dispositions'].get('RIGHT_CENSORED',0)] for x in M if x['horizon_hours']==24]))
sections.append('''
Certaines cellules 24 h sont positives, notamment C2 à 150 €. Elles portent sur peu de positions, davantage de censure et une occupation de capital différente. Elles ne justifient pas de sélectionner a posteriori l’horizon favorable. Le signe varie avec la politique de sortie et la taille : aucune robustesse économique hors échantillon n’est démontrée.

### Sensibilité aux bougies d’entrée sans transaction

Le modèle principal contient 4 fills sur bougie sans transaction dans B/C1 100 €, et 9 dans C2 100 €. Le contrôle ci-dessous interdit ces fills dans les deux branches. Cette condition porte sur la réalisation simulée, pas sur une décision qui connaîtrait le volume futur.
''')
SM=read('metrics_trade_bar_sensitivity');sections.append(mdtable(['Règle','Taille €','Fills','PnL €','DD MTM €'],[[x['policy'],x['stake'],x['fills'],fmt(x['net_pnl_eur']),fmt(x['mtm_drawdown_eur'])] for x in SM]))
sections.append('''
Le diagnostic principal ne change pas : C1 détériore les résultats 4 h, C2 réduit les pertes mais reste négatif et augmente le drawdown. Une sensibilité de fill n’est pas une estimation de probabilité d’exécution.

### Effet isolé des autres gates

| Modification | Mesure disponible | Conclusion autorisée |
|---|---|---|
| Range 6→5 % uniquement | C1, confirmations, règle shadow préexistante | améliore certains cas ; détériore le portefeuille 100 €/4 h |
| Volume 75k remplacé par carnet petite taille | profondeur ask partielle, bid complet absent | effet économique non identifiable ; challenger SMALL_SIZE reste UNKNOWN |
| Spread seul relâché | pas de carnet contemporain complet pour tous les refus | aucun uplift causal chiffré ; protection conservée |
| Stop maximal relâché | risque euro calculable sur plans existants, pas de contre-plan complet sur tous les refus | ne pas confondre réduction de taille et amélioration du signal |
| Prior thesis retirée | 37 événements de rejet ; correction nouvel épisode déjà en place | coût global d’une suppression totale non établi ; pas de relâchement supplémentaire |
| Restitution exhaustive DL | 1 936 occurrences immédiates supplémentaires visibles | gain de couverture certain pour un consommateur top3, gain de PnL non établi |
| Ajout V3.1 | C2, même fenêtre / univers | effet d’une route complète, pas décomposition causale de chaque gate |

## E. Shadow test prospectif

**Aucune modification du comportement production pour ce protocole.** L’instrumentation et les candidats parallèles doivent être déployés dans un environnement de mesure distinct après revue du livrable. Aucun test prospectif n’a encore été lancé pendant cet audit.

1. Figer avant démarrage C0 restitution, C1 range5, C2 V3.1 et C3 SMALL_SIZE séparément, leurs versions, coûts, sorties, capital et politique d’épisodes. Pas de règle ni de seuil par symbole. Préenregistrer l’analyse principale 4 h ; 24 h et délais 5/15/60 min seulement comme sensibilités, sans choisir le gagnant ensuite.
2. Collecter tous les candidats, y compris refusés et sans hausse, avec generated_at/observed_at/available_at, version de code, état amont, tous les gates, prix, stop, frais/minimums, carnet bid/ask brut, motif de premier échec et vecteur complet lorsque disponible. Journaliser le rang global, tous les achats immédiats, le top3 et la perte d’affichage.
3. Lier signal → décision → gate → épisode → mail → restitution → recommandation → confirmation d’ordre. Les états inconnus restent inconnus ; ne pas remplir automatiquement les accusés de lecture ou d’achat.
4. Durée minimale **28 jours et 100 épisodes indépendants arrivés à maturité** par comparaison économique. Un même épisode répété n’augmente pas artificiellement l’échantillon. Prolonger au maximum à 56 jours ; si la puissance reste insuffisante, classer inconclusif plutôt que promouvoir.
5. Comparer simultanément baseline et challengers sur tous les marchés, à mêmes capital, risque, latence et coûts. Mesurer PnL net, espérance, DD, MFE/MAE avant/après stop, fills, rejets, captures, perdants ajoutés et déplacés, turnover total, concentration par actif/jour et données manquantes.
6. Promotion économique seulement si espérance nette positive et borne basse de l’IC 95 % de l’amélioration d’espérance >0, bootstrap par blocs de jours/épisodes ; pas de dépendance à un seul actif ; DD ≤ baseline +2 points de capital ; aucun dépassement de risque ; turnover ≤1,5× baseline sauf profit incrémental net robuste préspécifié. Ne pas considérer le nombre « capturé sur les 10 » comme critère de promotion.
7. C0 se juge d’abord sur exhaustivité et traçabilité : 100 % des lignes immédiates consultables, zéro disparition silencieuse d’alerte et revalidation explicite des alertes périmées. Ce succès ne démontre pas une amélioration de trading.
8. Arrêt immédiat si donnée future utilisée pour décider, UNKNOWN converti en PASS, ordre réel involontaire, risque dépassé ou horodatage non fiable. Abandon du challenger à 56 jours si espérance incrémentale négative, drawdown excessif, coûts annulant le bénéfice ou besoin d’exceptions par actif. Prévoir un jeu prospectif ultérieur réservé avant toute promotion définitive.

## Sources et reproductibilité

Sources primaires GitHub, toutes à la référence d’audit :

- [Production gate](https://github.com/Vadimrom-create/bitvavo-live/blob/0fbc84babfe8567d40979e2a3f695ca57c001182/research/production_gate.py), [sender](https://github.com/Vadimrom-create/bitvavo-live/blob/0fbc84babfe8567d40979e2a3f695ca57c001182/scripts/send_production_buy_alert.py), [Decision Layer](https://github.com/Vadimrom-create/bitvavo-live/blob/0fbc84babfe8567d40979e2a3f695ca57c001182/research/decision_layer.py).
- [Journal production](https://github.com/Vadimrom-create/bitvavo-live/blob/0fbc84babfe8567d40979e2a3f695ca57c001182/production_decision_journal.json), [shadow actionable](https://github.com/Vadimrom-create/bitvavo-live/blob/0fbc84babfe8567d40979e2a3f695ca57c001182/production_all_actionable_shadow_journal.json), [range5](https://github.com/Vadimrom-create/bitvavo-live/blob/0fbc84babfe8567d40979e2a3f695ca57c001182/production_v21_range5_shadow_journal.json).
- [V3](https://github.com/Vadimrom-create/bitvavo-live/blob/0fbc84babfe8567d40979e2a3f695ca57c001182/solaire_v3_journal.json), [V3.1](https://github.com/Vadimrom-create/bitvavo-live/blob/0fbc84babfe8567d40979e2a3f695ca57c001182/solaire_v31_journal.json), [mémoire](https://github.com/Vadimrom-create/bitvavo-live/blob/0fbc84babfe8567d40979e2a3f695ca57c001182/solaire_memory_entry_challenger_journal.json), archives `history/` et `decision_history/` du même commit ; manifest des SHA inclus.
- [Évaluateur production](https://github.com/Vadimrom-create/bitvavo-live/blob/0fbc84babfe8567d40979e2a3f695ca57c001182/research/production_journal.py) ; [documentation officielle Bitvavo des bougies](https://docs.bitvavo.com/docs/rest-api/get-candlestick-data/) : ordre récent→ancien, absence de bougie sans transaction.
- Emails Gmail primaires relus pour QNT24, KMNO24, TREAD22, RARE25 et les premiers KMNO/TREAD21 ; dates, entrées et plans repris dans les tableaux. Les preuves d’emails n’établissent ni lecture humaine ni ordre. Les preuves ChatGPT proviennent de contexte conversationnel retrouvé, pas d’un export intégral ; les attributions conservent cette limite.

Fichiers : `Tableau_10_actifs.csv`, `timeline_journals.csv`, `timeline_archive.csv`, `book_sizes.csv`, `funnel_targets_extracted.json`, métriques, toutes les listes d’entrées/dispositions et scripts. `replay.py` reconstruit les bougies depuis les archives hashées ; `evidence.py` extrait les preuves ; `small_size_shadow.py` reste hors production. Le pack source inclut les données nécessaires et permet de recalculer les résultats sans API de marché courante. Les évaluations produites après le cutoff sont exclues des décisions et ne sont pas utilisées comme vérité économique.
''')
(OUT/'Audit_Solaire_2026-09-27.md').write_text('\n\n'.join(sections))
print('report_chars',len('\n\n'.join(sections)))
