# Audit adversarial Solaire — issue #89 — snapshot du 27/09/2026

**Verdict : l’hypothèse est partiellement confirmée, mais l’explication « le Decision Layer a bloqué QNT/KMNO/TREAD avant leur alerte » est réfutée.** Les trois ont produit un BUY_SENT et un email d’achat retrouvé dans Gmail. TREAD fournit un cas explicite de mauvaise justification dans le chat ; pour QNT/KMNO, le point exact de non-exécution par l’utilisateur n’est pas démontrable. Aucun journal d’ordres ne permet d’assimiler une alerte à une position réellement ouverte.

Le défaut aval le mieux établi combine une restitution incomplète des décisions, une confusion entre nouveaux candidats et thèses déjà alertées, et des journaux parallèles pris à tort pour une chaîne séquentielle. Les gates d’exécution expliquent la majorité des rejets enregistrés ; leur caractère excessif n’est pas prouvé par la hausse ultérieure. Le test économique ne justifie aucune promotion immédiate.

**Version finale :** reprise vérifiée jusqu’au HEAD `44d7e50b9825a439f541fac036d8276bea6837b1` (27/09 21:29:15 UTC) : 97 commits supplémentaires depuis `1ee4d8`, aucun changement Python/workflow. Le workspace d’audit n’est pas un checkout Git ; un ancien checkout distinct reste sur `3235924` avec deux archives déjà modifiées. Il n’a pas été touché. Le correctif chronologique existe dans le replay d’audit, **pas dans le code de production**. Aucun commit/PR de production n’est revendiqué.

**Correction d’horodatage indispensable :** les timestamps `decision_ts` BUY_SENT du journal reprennent `checked_at_utc`, fixé au début du sender. Ils ne datent pas la fin du gate ou la réception utilisateur. Les 125 BUY ont été joints à 111 emails Gmail ; les résultats définitifs de la section D utilisent leur disponibilité Gmail. Deux entrées changent de bougie par rapport au calcul initial. Les timestamps journal sont conservés comme preuves de trace, sans les faire passer pour des heures exactes de disponibilité. Les résultats initiaux sont conservés dans le pack ; ils ne sont pas les résultats économiques finaux.

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


| Actif | +24 h | Premier signal UTC | Prix premier signal | Première confirmation UTC / prix | Premier PASS production | Première décision actionable | Premier moment raisonnablement achetable | Cause exacte / couche | Mouvement après signal | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| QNT-EUR | +60.20 % | 22 10:21:29.533360 | 59.75 | 24 13:50:02.989835 ; 67.948 | Résultat disponible au mail 24 13:59:26 ; 69,091 € | Production connue au mail 24 13:59:26 ; 69,091 € | V3 technique 24 12:22:30.150763 à 64,868 ; V3.1 qualifié 13:02:30.669584 à 66,098 ; production 13:59:24. 100 € plausible ; 150 € dépasse le budget de risque sur le plan production. | Aucun raté sender sur le premier PASS ; 4 rejets stop ultérieurs. Restitution/lecture/exécution utilisateur non retraçable complètement. | MFE 4 h +9.04 % ; MAE -0.58 % (diagnostic depuis signal, pas PnL) | Transport OK ; défaut de restitution plausible, attribution exacte non prouvée |
| AMP-EUR | +57.19 % | 21 01:21:54.484517 | 0.0004057 | 22 15:14:46.746802 ; 0.0004284 | Aucun avant cutoff | Aucune production ; V3.1 shadow 26 19:07:29.238372 | Premier achat shadow qualifié : 26 19:07:29.238372, entrée 0,000639074582. 100 € techniquement plausible ; 150 € dépasse le risque 12 € du carnet proche. | Production : 5 volume + 8 spread. Aucune recommandation production ; qualification shadow tardive. Les 2 rejets stop évoqués dans le constat initial appartiennent au shadow. | MFE 4 h +0.17 % ; MAE -0.59 % (diagnostic depuis signal, pas PnL) | Gate production responsable des rejets ; relâchement global non justifié |
| RARE-EUR | +47.07 % | 21 18:22:06.634635 | 0.011441 | 23 02:41:28.890772 ; 0.012123 | Résultat disponible au mail 25 21:32:50 ; 0,014528 € | Production connue au mail 25 21:32:50 ; 0,014528 € | 25 21:32:48.048104 production à 0,014528. READY technique dès 17:47:23.698099 à 0,014548, qualification économique refusée ensuite. Pas de rétro-validation de ce READY. | 5 volume + 6 stop + 3 spread, mais 2 achats envoyés. Premier PASS production plus tôt que le premier PASS shadow cité. ; nouveau PASS revalidation publié26/09 17:53:32. | MFE 4 h -0.07 % ; MAE -1.00 % (diagnostic depuis signal, pas PnL) | Prémisse « premier achat à 0,020686 » réfutée ; premiers trades simulés perdants |
| HFT-EUR | +28.69 % | 21 00:27:35.662571 | 0.0052 | 21 13:46:16.245676 ; 0.005314 | Aucun avant cutoff | Aucune production | Non établi : aucun PASS ni carnet contemporain suffisant des rejets volume. | 9/9 rejets production INSUFFICIENT_EXECUTION_LIQUIDITY. Conservatisme à 100 € non démontré faute de carnet aux instants refusés. | MFE 4 h +5.52 % ; MAE -2.88 % (diagnostic depuis signal, pas PnL) | Veto volume certain ; faux négatif économique non démontré |
| 2Z-EUR | +21.38 % | 21 12:53:24.606439 | 0.04576 | 24 14:25:02.985555 ; 0.047861 | Aucun avant cutoff | Aucune production ; V3.1 shadow 24 14:43:35.159205 | 24 14:43:35.159205 V3.1 qualifié à 0,04809 ; benchmark profondeur 100 € OK. 150 € non certifiable à cet instant. | 2 range + 1 spread + 2 stop ; V3.1 shadow qualifie une entrée. Dans C1, le range5 peut ajouter une entrée ; dans C2 à 100 €, capacité empêche la première. ; revalidation shadow publiée24/09 16:55:25, sans BUY ; C3 ajoute un trade100 perdant. | MFE 4 h +0.00 % ; MAE -1.15 % (diagnostic depuis signal, pas PnL) | Range5 capture ce cas mais détériore le portefeuille 100 €/4 h |
| RUNE-EUR | +19.33 % | 21 18:22:06.634635 | 0.53895 | 22 13:18:59.284728 ; 0,57712 (production) | Aucun avant cutoff | Aucune production | Technique seulement le 26 09:21:15.284183 à 0,61435 ; V3.1 refuse le score économique. Premier achat raisonnable non établi avant cutoff. | Confirmation production bloquée STRUCTURAL_RANGE_TOO_NARROW. Le READY V3 ultérieur reste économiquement non qualifié. | MFE 4 h +4.66 % ; MAE +0.12 % (diagnostic depuis signal, pas PnL) | Gate range ; aucun achat raisonnable démontré dans la fenêtre |
| KMNO-EUR | +16.90 % | 21 02:49:48.101486 | 0.029702 | 21 02:52:35 ; 0,029897 (signal du mail) | Résultat disponible au mail 21 02:52:35 ; 0,029925 € | Production connue au mail 21 02:52:35 ; 0,029925 € | 21 02:52:35 au plus tard, mail 0,029925 ; 100–150 € compatibles avec le montant guide, profondeur contemporaine non conservée. | Emails présents dès le 21 et le 24 ; 3 autres épisodes bloqués par range. Pas de preuve d’un veto DL sur le PASS. | MFE 4 h +8.83 % ; MAE -5.75 % (diagnostic depuis signal, pas PnL) | Transport et restitution de mails antérieurs prouvés ; non-achat non attribuable précisément |
| COW-EUR | +15.48 % | 22 06:01:02.668430 | 0.14018 | 24 14:42:12.992751 ; 0,12603 (production) | Aucun avant cutoff | Aucune production | Non établi : confirmation bloquée par volume, pas de PASS technique exploitable retrouvé. | INSUFFICIENT_EXECUTION_LIQUIDITY en production ; WIDE_SPREAD_RISK dans la route DL, cause parallèle à ne pas cumuler. | MFE 4 h +0.86 % ; MAE -1.40 % (diagnostic depuis signal, pas PnL) | Volume en production ; données insuffisantes pour contrefactuel petite taille |
| AGI-EUR | +15.21 % | 21 09:42:37.705624 | 0.005104 | 21 14:35:06.464572 ; 0,005154 (production) | Aucun avant cutoff | Aucune production | Technique le 26 22:44:28.956561 à VWAP100 0,006016320176 ; pas de qualification V3.1 avant cutoff, horizon 4 h incomplet. | 8 volume + 1 spread production ; 8 événements seulement dans le sous-ensemble shadow initial. Fin de fenêtre trop proche pour valider le trade technique. | MFE 4 h +1.35 % ; MAE -2.41 % (diagnostic depuis signal, pas PnL) | Volume/spread ; aucune preuve de gain capturable sur le +24 h |
| TREAD-EUR | +14.79 % | 21 01:02:59.123557 | 0.43255 | 21 01:02:59.123557 ; 0.43255 | Résultat disponible au mail 21 10:05:02 ; 0,38501 € | Production connue au mail 21 10:05:02 ; 0,38501 € | 21 10:04:59.447374, 0,38501 ; puis 22 18:47:42.106827, 0,470. 100 € compatible ; 150 € au 22/09 supérieur au montant guide 140,82. | Mail présent ; refus ChatGPT du 22/09 motivé par absence de candidat. Deux suppressions prior thesis le 23 ; nombreux rejets stop/spread distincts. | MFE 4 h +11.36 % ; MAE +0.73 % (diagnostic depuis signal, pas PnL) | Erreur de justification ChatGPT établie par contexte retrouvé ; prior thesis secondaire |

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
| Journal BUY_SENT, début du contrôle | 24/09 13:59:24.097639 | BUY_SENT / DELIVERED ; entrée revalidée 69,091 ; stop 62,916 ; TP1 81,44 |
| Email Gmail | 24/09 13:59:26 | QNT candidat 1/2, avant LAPTOP ; spread 0,043 % ; stop 8,94 % ; montant guide 124,92 € |

**Où a-t-il disparu ?** Pas avant le mail. Le DL n’a pas filtré ce mail. La restitution ultérieure retrouvée du 26/09 20:45:07 décrit QNT comme trop avancé, environ +9,6 % au-dessus du signal de cette journée. Elle n’explique pas le traitement du mail du 24 à 13:59. Impossible d’attribuer le non-achat du 24 au ranking, à la lecture utilisateur ou au chat sans leur jointure temporelle.

L’entrée shadow plus précoce n’est pas automatiquement un achat : celle de 12:22 a été refusée économiquement. La première qualification V3.1 retrouvée est à 13:02. Le DL du 21 est un autre avertissement : `ACHETE_MAINTENANT` n’implique pas nécessairement `trade_plan.valid`. Le consommateur doit les vérifier séparément.

### KMNO

| Étape | UTC | Prix / état exact |
|---|---|---|
| V2 BUILDING archive | 21/09 02:49:48.101486 | 0,029702 € |
| Premier email retrouvé | 21/09 02:52:35 | signal confirmé 0,029897 ; entrée 0,029925 ; stop 0,02822 ; spread 0,084 % ; montant guide 188,16 € |
| BUY_SENT suivant, horodatage de début | 21/09 09:50:28.328058 | entrée 0,030916 ; stop 0,028836 ; email 09:50:30 |
| V3 READY | 24/09 01:56:12.492259 | entrée 0,032219 ; spread 0,0808 % ; VWAP100 0,032219328936 ; impact 0,010333 % |
| V3.1 QUALIFIED_ENTRY | 24/09 01:56:22.083088 | SELECTABLE ; score économique 6,216 |
| Cycle production | 24/09 02:33:14.383466 | signal 0,033073 ; score 7,896 |
| Gate shadow | 24/09 02:34:29.012994 | PASS + actionable ; rang 1 ; entrée 0,033009 ; stop 0,030626 ; PRIOR_BUY_THESIS_EXPIRED |
| Journal BUY_SENT, début du contrôle | 24/09 02:34:33.028774 | entrée 0,032992 ; stop 0,030626 ; TP1 0,037724 |
| Email Gmail | 24/09 02:34:36 | spread 0,100 % ; stop 7,17 % ; montant guide 152,94 € |
| Premier DL immédiat dans la fenêtre | 24/09 13:31:01.048568 | 0,032316 ; survient après l’email, donc pas sa condition d’envoi |

**Où a-t-il disparu ?** Aucun échec d’alerte établi. Les mails KMNO/TREAD du 21 ont même été examinés dans le chat à 11:50:15 UTC. Cela prouve une restitution au moins partielle, pas une exécution. Le traitement exact du mail KMNO du 24 reste non déterminé. Le premier trade du 24 à horizon 4 h est perdant dans le modèle : la hausse au snapshot ne transforme pas chaque entrée précédente en bonne opération.

### TREAD

| Étape | UTC | Prix / état exact |
|---|---|---|
| Première confirmation archive | 21/09 01:02:59.123557 | 0,43255 ; score 8,405 — un signal plus ancien peut être plus cher que l’achat ultérieur |
| Premier BUY_SENT, horodatage de début | 21/09 10:04:59.447374 | entrée 0,38501 ; stop 0,36549 ; email 10:05:02 ; spread 0,003 % |
| Cycle demandé | 22/09 18:46:20.605026 | signal 0,470 ; score 6,875 |
| Gate shadow | 22/09 18:47:38.441151 | rang 3 ; PASS + actionable ; entrée 0,470 ; stop 0,43311 ; TP1 0,54377 ; PRIOR_BUY_THESIS_EXPIRED |
| Journal BUY_SENT, début du contrôle | 22/09 18:47:42.106827 | même entrée/stop ; pas de veto de déduplication |
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


| Actif | Carnet UTC | Spread % | Asks 25 niveaux € | VWAP 100 / 150 | Impact % 100 / 150 | Coût spread € 100 / 150 | Risque € 100 / 150 | Range % | Limite |
|---|---|---|---|---|---|---|---|---|---|
| QNT | 24 19:24:48.009663 | 0.0842 | 28777.08 | 76.113 / 76.113 | 0.0000 / 0.0000 | 0.084 / 0.126 | 5.57 / 8.35 | 3.597 | Sortie non certifiable |
| AMP | 26 18:57:37.113672 | 0.1568 | 38563.01 | 0.000639076759839 / 0.000639084506371 | 0.0433 / 0.0445 | 0.157 / 0.235 | 9.21 / 13.82 | 12.612 | Sortie non certifiable |
| RARE | 25 17:47:23.698099 | 0.2757 | 43289.28 | 0.014548 / 0.014548 | 0.0000 / 0.0000 | 0.275 / 0.412 | 10.29 / 15.43 | 18.177 | Sortie non certifiable |
| HFT | Non retrouvé | ND | ND | ND | ND | ND | ND | ND | ND |
| 2Z | 24 20:11:55.958605 | 0.2916 | 25517.42 | 0.0505610478593 / 0.0505616985561 | 0.0041 / 0.0053 | 0.291 / 0.436 | 4.35 / 6.52 | 2.516 | Sortie non certifiable |
| RUNE | 26 09:21:15.284183 | 0.1908 | 52486.05 | 0.61435 / 0.61435 | 0.0000 / 0.0000 | 0.190 / 0.286 | 4.25 / 6.37 | 3.632 | Sortie non certifiable |
| KMNO | 24 20:34:39.316179 | 0.0656 | 47297.63 | 0.033549736232 / 0.0335498241542 | 0.0022 / 0.0025 | 0.066 / 0.098 | 4.66 / 6.99 | 3.415 | Sortie non certifiable |
| COW | Non retrouvé | ND | ND | ND | ND | ND | ND | ND | ND |
| AGI | 26 22:44:28.956561 | 0.4680 | 5797.25 | 0.00601632017641 / 0.00602176457847 | 0.0885 / 0.1791 | 0.466 / 0.699 | 4.55 / 6.96 | 8.853 | Sortie non certifiable |
| TREAD | 25 00:27:16.265560 | 0.3413 | 15035.30 | 0.61439 / 0.614392079959 | 0.0000 / 0.0003 | 0.340 / 0.510 | 7.90 / 11.85 | 6.947 | Sortie non certifiable |


AMP et RARE illustrent un point décisif : profondeur d’achat suffisante n’implique pas position de 150 € admissible. Sur ces carnets, le risque dépasse 12 € à 150 €. AGI reste exécutable mécaniquement à l’achat dans ce carnet, mais l’impact augmente de 0,0885 à 0,1791 % : il échoue à la variante conservatrice d’impact maximal 0,10 % pour 150 €.

**Premier prix exécutable des mails prioritaires, sous réserve de disponibilité de l’email :** aucune profondeur brute de sortie ne permet de le certifier. Leur spread, leur plan et leur montant guide rendent 100 € compatible avec la validation disponible ; 150 € doit être redimensionné pour QNT et TREAD au 22/09. Au plan QNT, le budget guide est 124,92 €, donc un achat de 150 € ne respecte pas le même budget de risque de 12 €.

### Prototype SMALL_SIZE_EXECUTABLE

Le fichier `small_size_shadow.py` définit une fonction pure, sans intégration production, sans symbole codé en dur. Elle peut remplacer **uniquement le proxy volume 24 h** si : signal éligible inchangé, données connues à l’instant de décision, marché ouvert, carnet bid/ask complet et frais/minimums connus, fraîcheur ≤90 s, spread ≤0,5 %, impact achat et revente immédiate ≤0,10 %, range ≥6 %, stop ≤10 %, risque ≤12 €, RR net ≥1,5. Une information manquante produit UNKNOWN, jamais PASS. Les limites de 90 s et 0,10 % sont des propositions non optimisées, à figer avant le shadow.

Les cinq assertions vérifient notamment qu’un carnet peut accepter 100 € et refuser 150 €, rejeter une observation future/périmée et retourner UNKNOWN sans bids. **Aucun nombre de captures SMALL_SIZE_EXECUTABLE n’est revendiqué historiquement**, faute de bid depth aux instants requis. Étendre les seuils de spread/stop en plus du volume serait un autre challenger, non testé ici.


## 3 bis. Détail contradictoire des sept actifs et des revalidations

La classification conserve une quatrième possibilité, **indéterminé**, quand les données ne permettent pas de choisir honnêtement entre protecteur et trop conservateur. La hausse future n’intervient jamais dans cette décision. Le fichier `all_seven_gate_events.csv` détaille chaque événement avec timestamp, prix signal, motif et limite de preuve.

| Actif | Rejets de production avant cutoff | Premier instant technique documenté | Appréciation causale du gate |
|---|---|---|---|
| AMP | 5 volume, puis 8 spread ; aucun BUY | 26/09 18:57:37.113672 V3 READY ; V3.1 SELECTABLE à 19:07:29.238372 | Les refus volume antérieurs restent indéterminés faute de carnet contemporain. Les refus spread respectent le plafond, leur coût exact n’est pas journalisé. À 19:09:01 le suivi de rejet retrouve une exécution propre mais le signal est BUILDING 5,081, donc **pas éligible à un BUY production**. Le premier fully actionable de ce suivi est le 27/09 05:41, hors fenêtre. |
| HFT | 9 volume ; aucun BUY | Non établi | Premier rejet 21/09 13:56:20.167155, signal 0,005314. Volume inférieur au seuil ; pas de carnet de gate ni de READY ultérieur prouvé. Impossible de classer « trop conservateur pour 100 € » avec le +28,69 %. |
| 2Z | 2 range, 1 spread, 2 stop ; aucun BUY | 24/09 14:42:21.893310 V3 READY ; V3.1 14:43:35.159205 | Le range V3 de 5,950593 % montre une frontière structurelle proche de 6 %, avec profondeur100 valide. Ce n’est pas la preuve que toute baisse de seuil est bonne. Après rejet spread 16:53:11.999954, contrôle shadow propre à 16:55:09.997647 ; disponible dans un commit à **16:55:25**. Le refus spread ancien devient obsolète pour cette nouvelle quote, mais le trade plus tardif perd dans C3. |
| RUNE | 1 range ; aucun BUY avant cutoff | 26/09 09:21:15.284183 V3 READY technique | Premier rejet 22/09 13:18:59.284728 à 0,57712. Au READY du 26, range encore 3,632332 % : reste sous 6 et 5 %. Exécution mécanique100/150 plausible, mais V3.1 refuse le score économique à 09:28:06.683830 (5,287), puis 11:36:00.419025 (5,59). Aucun achat économique validé ne doit être inventé. |
| COW | 1 volume ; aucun BUY | Non établi | Rejet 24/09 14:42:12.992751 à 0,12603. Aucun READY ni carnet approprié permettant le recalcul. WIDE_SPREAD_RISK du DL est une route parallèle, pas la cause de ce veto sender. |
| RARE | 5 volume, 6 stop, 3 spread, **2 BUY** | V3 READY 25/09 17:47:23.698099 ; production reçue à 21:32:50 à **0,014528 €** | Le READY de 17:47 est rejeté économiquement à 17:53:15.915791, score5,074. 150 € excède le risque12 sur ce plan. Après un autre refus stop le 26 à17:44, revalidation propre à17:53:17.072912, publiée17:53:32, sans nouvelle alerte production. Le prix 0,020686 est le PASS shadow du 26, pas le premier achat. |
| AGI | 8 volume, 1 spread ; aucun BUY | 26/09 22:44:28.956561 READY technique | Le carnet permet de chiffrer l’entrée, mais pas la liquidité future de sortie. À150, impact0,1791 % dépasse le cap conservateur0,10 % du prototype. Pas de V3.1 SELECTABLE ni horizon4h mature ; le +24h n’est pas une preuve de trade capturable. |

**Bornes sur les refus sans mesures conservées.** SPREAD_TOO_WIDE signifie spread>0,5 %, soit coût top-book >0,4975 € pour100 et >0,7463 € pour150, avant frais et impact. STRUCTURAL_STOP_TOO_WIDE signifie distance>10 % : à150, risque brut>15 €, donc ce refus protège effectivement le budget12 € ; à100, la distance exacte est nécessaire pour savoir si un sizing100 suffit. STRUCTURAL_RANGE_TOO_NARROW est une règle structurelle, non une preuve de carnet insuffisant. INSUFFICIENT_EXECUTION_LIQUIDITY indique volume24h<75000 €, sans mesure de VWAP par ce chemin. Aucun de ces journaux n’autorise à inventer le nombre manquant.

### Premières exécutions techniques conservées — 100 / 150 €

Les mesures sont celles de l’instant indiqué, jamais reportées sur les refus antérieurs. « ≥100 » signifie que le benchmark100 est rempli, sans inventer la profondeur totale ni un VWAP150. La qualification économique est indiquée séparément plus haut.
| Actif | Disponible UTC | Spread % | Asks € | VWAP100 /150 | Impact %100 /150 | Range % | Stop € (%distance) | Risque €100 /150 | Spread €100 /150 |
|---|---|---|---|---|---|---|---|---|---|
| AMP-EUR | 26 18:57:37.113672 | 0.1568 | 38563.01 | 0.000639076759839 / 0.000639084506371 | 0.0433 / 0.0445 | 12.6123 | 0.0005837 (8.6541 %) | 9.21 / 13.82 | 0.157 / 0.235 |
| HFT-EUR | Non établi | ND | ND | ND | ND | ND | ND | ND | ND |
| 2Z-EUR | 24 14:42:21.893310 | 0.1270 | ≥100 ; total ND | 0.04809 / ND | 0.0000 / ND | 5.9506 | 0.045657 (5.0593 %) | 5.63 / ND | 0.127 / 0.190 |
| RUNE-EUR | 26 09:21:15.284183 | 0.1908 | 52486.05 | 0.61435 / 0.61435 | 0.0000 / 0.0000 | 3.6323 | 0.59179 (3.6722 %) | 4.25 / 6.37 | 0.190 / 0.286 |
| COW-EUR | Non établi | ND | ND | ND | ND | ND | ND | ND | ND |
| RARE-EUR | 25 17:47:23.698099 | 0.2757 | 43289.28 | 0.014548 / 0.014548 | 0.0000 / 0.0000 | 18.1775 | 0.01313 (9.7470 %) | 10.29 / 15.43 | 0.275 / 0.412 |
| AGI-EUR | 26 22:44:28.956561 | 0.4680 | 5797.25 | 0.00601632017641 / 0.00602176457847 | 0.0885 / 0.1791 | 8.8531 | 0.005777 (3.9727 %) | 4.55 / 6.96 | 0.466 / 0.699 |

### 2Z : le pattern REJECT → conditions améliorées → pas de BUY

- 24/09 14:42:12.992751 : refus production range, signal0,04775. Neuf secondes plus tard, V3 a une entrée0,04809, stop0,045657, range5,950593 %, spread0,127 %, benchmark100 sur un niveau sans impact ; risque100≈5,63 €, risque150 non certifié faute de profondeur brute à cet instant.
- 16:53:11.999954 : nouveau refus production SPREAD_TOO_WIDE, signal0,052384.
- 16:55:09.997647 : début du contrôle shadow enregistré ; résultat validé avec entrée0,051556, stop0,047122, spread0,326925 %, range13,816184 %, distance stop8,600357 %, score8,5, quatre preuves, CONFIRMED_ACCELERATION. **Publication GitHub à16:55:25** : borne vérifiable à laquelle tout le résultat existe.
- À la quote validée, risque estimé100≈9,15 € et150≈13,72 € ; coût top-book≈0,326 /0,489 €. Pas de profondeur brute dans ce snapshot : VWAP/slippage100/150 non certifiés. 150 est exclu par le budget12, 100 reste un candidat au modèle.
- Aucun BUY production 2Z dans la fenêtre. Le suivi de rejet est explicitement shadow ; il ne déclenche pas le sender. C’est un défaut possible de routage/reprise, pas une panne SMTP et pas une preuve que l’ancien rejet spread était erroné.
- C3 à100 simule une entrée17:00 à0,051692641 : MFE4h+1,69 %, MAE−3,96 %, stop non touché, PnL net−4,45 €. La reprise automatique ajoute ici **un trade perdant**, malgré le statut de gagnant quotidien de2Z.

### Généralisation, sans sélection des futurs non-alertés

467 commits du journal de rejet ont été recensés ; 86 versions précises relues contiennent 96 revalidations confirmées sur63 marchés. Les timestamps de publication bornent leur disponibilité, de0,71 à33,87 secondes après le début de contrôle. Les snapshots postérieurs au cutoff, dont le fully actionable AMP du27 à05:41, sont exclus.

Sur94 revalidations avec quatre heures d’observation disponibles,90 n’ont aucun BUY production dans ces quatre heures. **Ce ne sont pas90 faux négatifs économiques.** `fully_actionable` dans ce journal signifie confirmé + exécution valide ; le script n’applique pas le contrôle de thèse antérieure. En le conservant de manière prudente,74 des96 cas sont retenus ;22 seulement deviennent candidats à la reprise. La sélection C3 ne regarde jamais si un BUY apparaîtra ensuite ; cette absence future sert uniquement au diagnostic.

C3 reprend une seule fois chaque événement validé, à sa première publication connue, avec quote âgée de moins de90s, score≥6,5, preuves≥3, et protection des alertes antérieures encore actives. Faute d’identifiant d’épisode suffisant dans ce snapshot, aucun bypass « nouvel épisode » n’est inventé : traitement conservateur. Capital, risque et exécution modélisée sont ensuite identiques aux autres variantes.


## A. Diagnostic transversal

1. **Confusion de routes.** Un refus shadow ne remplace pas le verdict du sender ; RARE en fournit une contradiction directement observable. Un état DL immédiat n’est pas non plus une validation d’exécution complète. De même, le terme fully_actionable du suivi de rejets n’intègre pas le prior thesis.
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

Ajouter au protocole shadow un registre des refus réévaluables ; publier un changement d’état EXÉCUTION_REVALIDÉE avec son heure de disponibilité, puis appliquer les mêmes protections de thèse, risque et données. C3 ne justifie pas encore de convertir systématiquement ces changements en recommandations d’achat.

Corriger séparément l’évaluateur : tri chronologique, exclusion de bougies non clôturées à l’horizon, contrôle de couverture et chemin stop/TP explicite. Ce correctif de mesure ne change pas la stratégie. Le bypass prior thesis nouvel épisode existe déjà : le mesurer prospectivement au lieu de le réimplémenter.

**Livrable avant patch respecté :** seules des extractions, simulations et fonctions hors production sont créées. Aucun changement scanner, gate, sender ou workflow ; aucun ordre.

## D. Comparaison économique définitive — causalité et contrôles négatifs

**Ces tableaux remplacent les valeurs du replay initial basé sur l’heure du début du sender.** La correction de disponibilité ne change ni les seuils ni les choix de variantes. 125 BUY sont rapprochés d’emails ; deux franchissent une frontière5min. TREAD du21 est un exemple : début contrôle10:04:59, email10:05:02. Entrer à10:05 sur la seule trace journal aurait devancé l’email ; le test isolé prend désormais la bougie suivante et obtient NO_FILL.

**Fenêtre principale commune aux quatre variantes : 23/09 23:22:23.220478 → 27/09 00:25 UTC pour les prix complets**, décisions limitées au snapshot00:47. Tous les candidats de l’univers disponibles dans cette fenêtre sont éligibles, pas uniquement les dix gagnants. B reprend les BUY réellement envoyés ; C1 ajoute les confirmations range5 préexistantes ; C2 ajoute les qualifications V3.1 ; C3 ajoute les revalidations après protections conservées. Les comparaisons complètes depuis le21 sont aussi conservées pour ne pas effacer le résultat défavorable de C1 dans la fenêtre initiale.

Modèle fixé : capital2331,61 € fictif, max10positions, une par marché, 100 ou150 € frais inclus, risque≤12 €. Entrée au premier open5min après disponibilité ×1,001, limite quote×1,005 ; frais0,25 %/côté. Stop structurel inchangé, gap et sortie−0,10 % ; sinon clôture après4h. Sensibilité24h, sans choisir l’horizon favorable a posteriori. C1 utilise le timestamp enregistré après validation ; C2 la décision qualifiée avec plan déjà disponible ; C3 la publication de son résultat. Les heures et prix futurs ne servent qu’à mesurer l’exécution modélisée et les résultats, jamais à choisir les candidats.

Les bid depths complets, latences humaines et frais réels de compte restent manquants : il s’agit d’un replay causal avec **modèle de fill**, pas d’ordres certifiés. Les bougies sont triées, complètes et évaluées jusqu’au cutoff. Les horizons non matures sont censurés. MFE/MAE sur tout l’horizon incluent potentiellement l’après-stop ; les fichiers donnent aussi les excursions jusqu’à la bougie de sortie, sans prétendre connaître l’ordre intrabar.

### Même fenêtre, horizon4h
| Variante | € | Trades | Gagnants/perdants | Réussite % | Espérance € | PnL € | DD MTM € | Stops | Turnover achat € | Cibles capturées |
|---|---|---|---|---|---|---|---|---|---|---|
| F_Baseline | 100 | 46 | 15/31 | 32.61 | -1.40 | -64.27 | 70.14 | 8 | 4600 | KMNO-EUR, QNT-EUR, RARE-EUR |
| F_C1_range5 | 100 | 64 | 23/41 | 35.94 | -0.98 | -62.72 | 93.85 | 9 | 6400 | 2Z-EUR, KMNO-EUR, QNT-EUR, RARE-EUR |
| F_C2_v31 | 100 | 124 | 48/76 | 38.71 | -0.36 | -44.53 | 98.20 | 19 | 12400 | AMP-EUR, KMNO-EUR, QNT-EUR, RARE-EUR, TREAD-EUR |
| F_C3_revalidation | 100 | 54 | 18/36 | 33.33 | -1.44 | -77.82 | 85.23 | 9 | 5400 | 2Z-EUR, KMNO-EUR, QNT-EUR, RARE-EUR |
| F_Baseline | 150 | 28 | 9/19 | 32.14 | -2.95 | -82.59 | 89.28 | 7 | 4200 | RARE-EUR |
| F_C1_range5 | 150 | 49 | 15/34 | 30.61 | -2.36 | -115.71 | 136.06 | 9 | 7350 | 2Z-EUR, RARE-EUR |
| F_C2_v31 | 150 | 112 | 45/67 | 40.18 | -0.49 | -54.61 | 123.01 | 17 | 16800 | 2Z-EUR, KMNO-EUR, QNT-EUR, RARE-EUR, TREAD-EUR |
| F_C3_revalidation | 150 | 34 | 13/21 | 38.24 | -2.31 | -78.38 | 86.80 | 8 | 5100 | RARE-EUR |

### MFE/MAE et contrôles hors des dix gagnants

Les « contrôles négatifs » désignent ici tous les marchés hors de la liste adversariale, y compris leurs trades gagnants : on ne fabrique pas un groupe de contrôle en ne gardant que les perdants après coup.

| Variante | € | Cohorte | Trades | Gagnants/perdants | PnL € | MFE médiane % | MAE médiane % | Stops |
|---|---|---|---|---|---|---|---|---|
| F_Baseline | 100 | 10_winners | 4 | 1/3 | -10.53 | 4.00 | -6.46 | 2 |
| F_Baseline | 100 | negative_controls | 42 | 14/28 | -53.74 | 3.52 | -3.71 | 6 |
| F_C1_range5 | 100 | 10_winners | 5 | 2/3 | -4.51 | 6.99 | -3.87 | 2 |
| F_C1_range5 | 100 | negative_controls | 59 | 21/38 | -58.21 | 3.12 | -3.47 | 7 |
| F_C2_v31 | 100 | 10_winners | 13 | 4/9 | 3.88 | 1.84 | -2.69 | 2 |
| F_C2_v31 | 100 | negative_controls | 111 | 44/67 | -48.41 | 2.66 | -2.65 | 17 |
| F_C3_revalidation | 100 | 10_winners | 6 | 1/5 | -20.60 | 3.03 | -6.20 | 2 |
| F_C3_revalidation | 100 | negative_controls | 48 | 17/31 | -57.22 | 3.45 | -3.80 | 7 |
| F_Baseline | 150 | 10_winners | 2 | 0/2 | -21.90 | 4.00 | -9.15 | 2 |
| F_Baseline | 150 | negative_controls | 26 | 9/17 | -60.69 | 3.30 | -3.50 | 5 |
| F_C1_range5 | 150 | 10_winners | 3 | 1/2 | -12.87 | 6.99 | -9.05 | 2 |
| F_C1_range5 | 150 | negative_controls | 46 | 14/32 | -102.83 | 2.77 | -3.18 | 7 |
| F_C2_v31 | 150 | 10_winners | 12 | 4/8 | 5.15 | 2.50 | -2.47 | 2 |
| F_C2_v31 | 150 | negative_controls | 100 | 41/59 | -59.76 | 2.31 | -2.49 | 15 |
| F_C3_revalidation | 150 | 10_winners | 2 | 0/2 | -21.90 | 4.00 | -9.15 | 2 |
| F_C3_revalidation | 150 | negative_controls | 32 | 13/19 | -56.48 | 3.27 | -3.50 | 6 |

### Faux positifs ajoutés et trades déplacés

Un faux positif est défini ici comme un trade au PnL net négatif sous la sortie fixée. Une hausse24h ne définit pas le succès d’une entrée.

| Variante | € | Trades supplémentaires distincts | Dont perdants | Baseline déplacés | Dont perdants | Cibles supplémentaires |
|---|---|---|---|---|---|---|
| F_C1_range5 | 100 | 21 | 13 | 3 | 3 | 2Z-EUR |
| F_C2_v31 | 100 | 89 | 52 | 11 | 7 | AMP-EUR, TREAD-EUR |
| F_C3_revalidation | 100 | 9 | 5 | 1 | 0 | 2Z-EUR |
| F_C1_range5 | 150 | 21 | 15 | 0 | 0 | 2Z-EUR |
| F_C2_v31 | 150 | 87 | 49 | 3 | 1 | 2Z-EUR, KMNO-EUR, QNT-EUR, TREAD-EUR |
| F_C3_revalidation | 150 | 7 | 2 | 1 | 0 |  |

À100 sur cette fenêtre commune, C1 améliore seulement le total de1,55 € mais augmente le drawdown d’environ23,71 € ; son espérance reste négative. C2 réduit la perte totale d’environ19,74 € mais ajoute45 perdants nets et augmente le drawdown. C3 ajoute9 trades distincts, dont5 perdants, et déplace1 baseline : PnL dégradé d’environ13,54 €, drawdown accru. À150, C3 améliore légèrement le total mais reste déficitaire, sur très peu d’ajouts ; ce n’est pas une validation.

### Fenêtre initiale depuis le21 — ne pas réécrire le résultat défavorable de C1
| Variante | € | Trades | Gagnants/perdants | PnL € | DD MTM € |
|---|---|---|---|---|---|
| F_full_Baseline | 100 | 95 | 31/64 | -118.17 | 143.30 |
| F_full_C1 | 100 | 132 | 45/87 | -132.78 | 159.87 |
| F_full_C3 | 100 | 109 | 35/74 | -149.63 | 176.41 |
| F_full_Baseline | 150 | 54 | 15/39 | -155.94 | 195.37 |
| F_full_C1 | 150 | 96 | 28/68 | -206.55 | 239.98 |
| F_full_C3 | 150 | 63 | 20/43 | -150.11 | 191.26 |

À100 dans la fenêtre initiale, C1 reste moins bon de14,61 € malgré2Z capturé. Le changement de deux bougies dû aux emails déplace le niveau des résultats, pas cette comparaison. C3 dégrade aussi le résultat à100. Aucun choix de sous-fenêtre ne doit transformer ces variantes en stratégie promouvable.

### Sensibilité24h sur la même fenêtre principale
| Variante | € | Trades | Gagnants/perdants | PnL € | Espérance € | DD MTM € | Stops | Censurés |
|---|---|---|---|---|---|---|---|---|
| F_Baseline | 100 | 27 | 9/18 | 7.68 | 0.28 | 47.29 | 12 | 20 |
| F_C1_range5 | 100 | 27 | 13/14 | 36.08 | 1.34 | 48.17 | 10 | 27 |
| F_C2_v31 | 100 | 29 | 15/14 | 19.55 | 0.67 | 47.35 | 11 | 96 |
| F_C3_revalidation | 100 | 26 | 10/16 | 22.71 | 0.87 | 40.15 | 10 | 27 |
| F_Baseline | 150 | 20 | 6/14 | -52.68 | -2.63 | 75.50 | 11 | 20 |
| F_C1_range5 | 150 | 29 | 11/18 | -56.27 | -1.94 | 90.69 | 13 | 27 |
| F_C2_v31 | 150 | 29 | 15/14 | 62.05 | 2.14 | 64.92 | 10 | 88 |
| F_C3_revalidation | 150 | 23 | 8/15 | -62.63 | -2.72 | 77.54 | 12 | 27 |

Le signe dépend de l’horizon, de la taille et de l’occupation de capital. Certaines cellules24h sont positives ; elles ne permettent pas de choisir rétroactivement la variante ou la sortie gagnante. Aucun résultat hors échantillon n’est établi. Les sensibilités initiales interdisant les fills sur bougies sans transaction restent disponibles dans le pack ; elles ne validaient ni C1 ni C2.

### Premières entrées ciblées, disponibilité réellement prise en compte
| Variante | Actif | Entrée UTC | Prix € | Risque € | MFE % | MAE % | Sortie | PnL € |
|---|---|---|---|---|---|---|---|---|
| F_Baseline | KMNO-EUR | 24 02:35:00 | 0.03313309999999999 | 8.12 | 0.76 | -3.87 | HORIZON | -3.25 |
| F_Baseline | QNT-EUR | 24 14:00:00 | 69.29722799999999 | 9.75 | 11.94 | -1.29 | HORIZON | 7.32 |
| F_Baseline | RARE-EUR | 25 21:35:00 | 0.014355340999999997 | 7.40 | 1.01 | -9.05 | STOP | -7.40 |
| F_C1_range5 | 2Z-EUR | 24 14:45:00 | 0.047816768999999995 | 5.09 | 15.57 | -0.31 | HORIZON | 6.02 |
| F_C2_v31 | KMNO-EUR | 24 02:00:00 | 0.032359327 | 5.73 | 3.17 | -1.57 | HORIZON | -1.28 |
| F_C2_v31 | QNT-EUR | 24 13:05:00 | 65.734669 | 4.79 | 18.00 | -0.10 | HORIZON | 12.72 |
| F_C2_v31 | TREAD-EUR | 25 01:40:00 | 0.62161099 | 6.54 | 13.00 | -5.37 | HORIZON | 4.69 |
| F_C2_v31 | RARE-EUR | 25 21:35:00 | 0.014355340999999997 | 7.40 | 1.01 | -9.05 | STOP | -7.40 |
| F_C2_v31 | AMP-EUR | 26 19:10:00 | 0.0006364357999999999 | 8.83 | 19.76 | -3.04 | HORIZON | 7.10 |
| F_C3_revalidation | 2Z-EUR | 24 17:00:00 | 0.05169264099999999 | 9.39 | 1.69 | -3.96 | HORIZON | -4.45 |

Le premier RARE de la baseline touche son stop (−7,40 €/100), malgré sa hausse au snapshot. Le premier mail KMNO du21, hors fenêtre journal initiale, donne dans le test isolé une entrée02:55 à0,029940911 et un stop, soit−6,31 €/100 et−9,47 €/150. TREAD22 donne une entrée18:50 à0,47047, MFE+10,02 %, MAE−0,94 %, mais seulement+0,36 € au terme4h ;150 dépasse le risque12. QNT24 donne+7,32 €/100 ;150 est aussi refusé par le risque. KMNO24 donne−3,25 €/100 ; le glissement jusqu’à la bougie d’entrée fait également dépasser le risque12 à150. Ces contre-exemples empêchent d’assimiler « bon gagnant quotidien » à « bon trade à toute heure ».

### Ce qui est isolé et ce qui ne l’est pas

C1 isole le seuil range6→5 dans le sous-ensemble confirmé déjà testé. C2 mesure l’ajout d’une route qualifiée entière, pas un gate unique. C3 mesure la reprise de validations après rejet avec contrôle de thèse conservé. L’override volume petite taille ne peut pas être chiffré complètement faute de profondeur bid ; aucun uplift de spread/stop relâché n’est inventé. La réduction du montant est distincte d’une amélioration de signal.


## E. Shadow test prospectif

**Aucune modification du comportement production pour ce protocole.** L’instrumentation et les candidats parallèles doivent être déployés dans un environnement de mesure distinct après revue du livrable. Aucun test prospectif n’a encore été lancé pendant cet audit.

1. Figer avant démarrage C0 restitution, C1 range5, C2 V3.1 et C3 revalidation et C4 SMALL_SIZE séparément, leurs versions, coûts, sorties, capital et politique d’épisodes. Pas de règle ni de seuil par symbole. Préenregistrer l’analyse principale 4 h ; 24 h et délais 5/15/60 min seulement comme sensibilités, sans choisir le gagnant ensuite.
2. Collecter tous les candidats, y compris refusés et sans hausse, avec generated_at/observed_at/available_at, version de code, état amont, tous les gates, prix, stop, frais/minimums, carnet bid/ask brut, motif de premier échec et vecteur complet lorsque disponible. Journaliser le rang global, tous les achats immédiats, le top3 et la perte d’affichage.
3. Lier signal → décision → gate → épisode → mail → restitution → recommandation → confirmation d’ordre. Les états inconnus restent inconnus ; ne pas remplir automatiquement les accusés de lecture ou d’achat.
4. Durée minimale **28 jours et 100 épisodes indépendants arrivés à maturité** par comparaison économique. Un même épisode répété n’augmente pas artificiellement l’échantillon. Prolonger au maximum à 56 jours ; si la puissance reste insuffisante, classer inconclusif plutôt que promouvoir.
5. Comparer simultanément baseline et challengers sur tous les marchés, à mêmes capital, risque, latence et coûts. Mesurer PnL net, espérance, DD, MFE/MAE avant/après stop, fills, rejets, captures, perdants ajoutés et déplacés, turnover total, concentration par actif/jour et données manquantes.
6. Promotion économique seulement si espérance nette positive et borne basse de l’IC 95 % de l’amélioration d’espérance >0, bootstrap par blocs de jours/épisodes ; pas de dépendance à un seul actif ; DD ≤ baseline +2 points de capital ; aucun dépassement de risque ; turnover ≤1,5× baseline sauf profit incrémental net robuste préspécifié. Ne pas considérer le nombre « capturé sur les 10 » comme critère de promotion.
7. C0 se juge d’abord sur exhaustivité et traçabilité : 100 % des lignes immédiates consultables, zéro disparition silencieuse d’alerte et revalidation explicite des alertes périmées. Ce succès ne démontre pas une amélioration de trading.
8. Arrêt immédiat si donnée future utilisée pour décider, UNKNOWN converti en PASS, ordre réel involontaire, risque dépassé ou horodatage non fiable. Abandon du challenger à 56 jours si espérance incrémentale négative, drawdown excessif, coûts annulant le bénéfice ou besoin d’exceptions par actif. Prévoir un jeu prospectif ultérieur réservé avant toute promotion définitive.

## Attribution finale des faux négatifs

- **Faux négatif de détection :** non établi sur les dix ; l’absence de BUY ne l’implique pas.
- **Faux négatif d’envoi après premier PASS :** réfuté pour QNT/KMNO/TREAD et corrigé pour RARE. Leur email existe ; la suite ne prouve pas un achat réalisé.
- **Erreur de restitution identifiable :** TREAD22, confusion flux de nouveaux candidats / thèse antérieure ; omission d’achats DL par un consommateur top3. Impact euro utilisateur non identifiable sans ordre et transcript complet.
- **Conditions devenues meilleures après rejet :** 2Z24 et RARE26 attestés ; pas de re-routage production de ces validations shadow. Le premier refus pouvait être correct. C3 montre que la réactivation ajoute aussi des perdants ; ces cas ne sont pas tous des faux négatifs économiques.
- **Gates conservateurs prouvés économiquement :** aucun relâchement global démontré supérieur. 2Z autour de5,95 % montre une opportunité mécaniquement plausible sous le seuil6 ; HFT/COW restent indéterminés faute de carnets, AMP redevient propre pendant BUILDING, RUNE reste non qualifié, AGI est censuré.
- **Responsabilité non attribuable :** lecture/ordre QNT et KMNO, prix d’exécution à150 sur les carnets non conservés, allocation V3.5 ancienne, totalité des omissions ChatGPT. Ces inconnues ne sont attribuées artificiellement à aucune couche.

## Sources et reproductibilité

Sources primaires GitHub, toutes à la référence d’audit :

- [Production gate](https://github.com/Vadimrom-create/bitvavo-live/blob/0fbc84babfe8567d40979e2a3f695ca57c001182/research/production_gate.py), [sender](https://github.com/Vadimrom-create/bitvavo-live/blob/0fbc84babfe8567d40979e2a3f695ca57c001182/scripts/send_production_buy_alert.py), [Decision Layer](https://github.com/Vadimrom-create/bitvavo-live/blob/0fbc84babfe8567d40979e2a3f695ca57c001182/research/decision_layer.py).
- [Journal production](https://github.com/Vadimrom-create/bitvavo-live/blob/0fbc84babfe8567d40979e2a3f695ca57c001182/production_decision_journal.json), [shadow actionable](https://github.com/Vadimrom-create/bitvavo-live/blob/0fbc84babfe8567d40979e2a3f695ca57c001182/production_all_actionable_shadow_journal.json), [range5](https://github.com/Vadimrom-create/bitvavo-live/blob/0fbc84babfe8567d40979e2a3f695ca57c001182/production_v21_range5_shadow_journal.json).
- [V3](https://github.com/Vadimrom-create/bitvavo-live/blob/0fbc84babfe8567d40979e2a3f695ca57c001182/solaire_v3_journal.json), [V3.1](https://github.com/Vadimrom-create/bitvavo-live/blob/0fbc84babfe8567d40979e2a3f695ca57c001182/solaire_v31_journal.json), [mémoire](https://github.com/Vadimrom-create/bitvavo-live/blob/0fbc84babfe8567d40979e2a3f695ca57c001182/solaire_memory_entry_challenger_journal.json), archives `history/` et `decision_history/` du même commit ; manifest des SHA inclus.
- [Évaluateur production](https://github.com/Vadimrom-create/bitvavo-live/blob/0fbc84babfe8567d40979e2a3f695ca57c001182/research/production_journal.py) ; [documentation officielle Bitvavo des bougies](https://docs.bitvavo.com/docs/rest-api/get-candlestick-data/) : ordre récent→ancien, absence de bougie sans transaction.
- Emails Gmail primaires relus pour QNT24, KMNO24, TREAD22, RARE25 et les premiers KMNO/TREAD21 ; dates, entrées et plans repris dans les tableaux. Les preuves d’emails n’établissent ni lecture humaine ni ordre. Les preuves ChatGPT proviennent de contexte conversationnel retrouvé, pas d’un export intégral ; les attributions conservent cette limite.

Fichiers : `Tableau_10_actifs.csv`, `timeline_journals.csv`, `timeline_archive.csv`, `book_sizes.csv`, `funnel_targets_extracted.json`, métriques, toutes les listes d’entrées/dispositions et scripts. `replay.py` reconstruit les bougies depuis les archives hashées ; `evidence.py` extrait les preuves ; `small_size_shadow.py` reste hors production. Le pack source inclut les données nécessaires et permet de recalculer les résultats sans API de marché courante. Les évaluations produites après le cutoff sont exclues des décisions et ne sont pas utilisées comme vérité économique.
