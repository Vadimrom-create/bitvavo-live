# Audit adversarial NEAR — faux négatif OLD / Solaire

Date: 2026-09-24  
Branche d'audit: `codex/near-false-negative-audit-20260924`  
Base examinée pour l'état V3 actuel: `codex/v3-architecture-hardening-20260924` @ `2e831a7fdf82deb872c560abef5a537799b0678e`

## Question

NEAR a-t-il constitué, ces dernières semaines, une opportunité que OLD/V4 puis Solaire V2 ont vue trop tard ou mal qualifiée, et quelles corrections générales faut-il en tirer sans coder une exception NEAR ni utiliser d'information future ?

## Conclusion courte

Oui. Le cas NEAR met en évidence **plusieurs défauts distincts**, à des époques différentes :

1. **OLD/V4 a détecté NEAR mais n'a pas converti assez tôt cette détection en décision exploitable.**
2. **Une faiblesse historique de fraîcheur du cache de tendance a pu dégrader la qualification de NEAR lors d'une fenêtre de reset.**
3. **La logique de réentrée V4 était trop restrictive : elle exigeait un ancien `BUY_READY`, alors qu'une ancienne `ENTRY_WINDOW` structurellement forte pouvait mériter une requalification.**
4. **Solaire V2 est trop centré sur l'accélération courte pour détecter assez tôt certains leaders persistants.**
5. **Quand V2 a enfin confirmé NEAR, un seuil dur de structure 15m a rejeté plusieurs signaux, dont au moins un avait pourtant une géométrie de trade valide.**
6. **V3/V3.1 ne peuvent pas être tenus responsables de la partie antérieure du mouvement : leurs journaux prospectifs démarrent seulement les 23–24 septembre.**
7. **La V3 actuelle corrige déjà une grande partie du problème (full-universe, thèse persistante, pullback/reclaim, absence du gate V2 à 6 %, fair queues), mais conserve un angle mort potentiel : une thèse ne peut pas encore être semée par la seule persistance d'un leader structurel sans news positive, external spark ou nouveau trigger quantitatif.**

## Chronologie causale

### 1. Première détection OLD/V4 connue — 6 septembre

Dans `v4_signal_log.json` au commit historique `e75d0f9232cf21ffbd61c5d3dc14b5edc3948d6e` :

- première détection NEAR : **2026-09-06 20:47:47 UTC** ;
- prix : **2,0769 EUR** ;
- opportunity score : **8,043** ;
- entry score : **6,95** ;
- trend score : **10** ;
- statut : **ENTRY_WINDOW** ;
- MFE ultérieure de l'épisode : **+12,119 %** ;
- MAE : **-6,2064 %**.

Point important : V4 n'était donc pas aveugle. Le défaut est le passage **détection -> qualification actionable**, pas la couverture.

### 2. Deuxième fenêtre autour de 1,99 EUR — 13 septembre

Snapshots historiques :

- 12:26 UTC : prix **1,9897**, opportunity 7,311, entry 7,30, trend 8,10 ;
- 12:54 UTC : prix **1,9958**, opportunity **7,728**, entry **7,35**, trend **8,10** ;
- NEAR reste `WATCH` / non buy-ready.

Le profil de tendance utilisé à ces instants est toutefois daté du **9 septembre** et conserve notamment `ret7d ~= +31 %`. Le code V4 applique alors `CHASE_RISK` si `ret7d > 30` et que l'entrée n'est pas classée `PULLBACK`.

La fonction de cache historique avait un défaut général :

- fraîcheur pilotée par un timestamp global ;
- un refresh partiellement échoué pouvait laisser un profil par marché ancien ;
- le timestamp global était quand même rafraîchi ;
- un profil ancien pouvait donc rester exploité par le scoring et `CHASE_RISK`.

Cette faiblesse n'explique pas seule l'absence de BUY (l'opportunity score était aussi sous certains seuils), mais elle biaisait la qualification dans le mauvais sens précisément pendant un reset.

### 3. Défaut de réentrée V4

Le code historique de `v4_detector.py` n'autorise `REENTRY_READY` que si `hm.ever_buy_ready` est déjà vrai.

NEAR avait une ancienne **ENTRY_WINDOW** le 6 septembre mais pas nécessairement un ancien `BUY_READY`. Une opportunité forte pouvait donc :

- être identifiée ;
- ne jamais devenir BUY_READY lors du premier épisode ;
- corriger/reconstruire proprement ;
- rester inéligible à la logique de réentrée prévue pour les anciens gagnants.

C'est un défaut structurel de machine d'état, pas un cas NEAR.

### 4. Solaire V2 — manque de précocité

La production directe scanne bien l'univers EUR complet, mais sa détection V2 repose surtout sur :

- momentum 5m ;
- accélération du momentum 5m ;
- expansion de volume ;
- pression breakout ;
- confirmation 15m.

Au début des scans de production du 20 septembre :

- 19:27, 20:57, 21:45 et 22:33 UTC : NEAR ne figure ni dans `tracking` ni dans `watch` ;
- le 21 septembre à 04:00 UTC, NEAR apparaît enfin en `BUILDING_ACCELERATION` ;
- prix : **3,8301 EUR** ;
- variation 24h : **+25,33 %** ;
- score : **5,357** ;
- encore non actionable car sous le seuil confirmé de 6,50.

Donc V2 finit par voir NEAR, mais seulement après une part importante du déplacement. C'est cohérent avec un système optimisé pour une ignition courte, moins avec un système qui doit aussi suivre un leader persistant / continuation après reset.

### 5. V2 confirme ensuite NEAR, mais l'exécution le rejette

Premier rejet confirmé documenté :

- 22 septembre 00:49 UTC ;
- prix **3,7801 EUR** ;
- score accélération **6,603** ;
- raison : `STRUCTURAL_RANGE_TOO_NARROW` ;
- amplitude structurelle 15m : **3,3785 %** ;
- plan calculé pourtant valide :
  - entrée 3,7801 ;
  - stop 3,6414 ;
  - distance stop 3,6692 % ;
  - TP1 4,0575 ;
  - net R:R TP1 1,5179.

Résultat observé après rejet :

- MFE 1h : +3,492 % ;
- MFE 4h : **+5,775 %** ;
- MFE 12h/24h : **+7,4892 %** ;
- MAE 4h : -1,3359 %.

Le gate de production actuel impose `MIN_15M_CONSOLIDATION_RANGE_PCT = 6.0` avant même de retenir le plan. Le sweep disponible montre cependant qu'il serait dangereux de simplement abaisser ce seuil à cause de NEAR : l'échantillon est petit et plusieurs rejets sous 6 % ont de mauvais résultats. **Conclusion : ne pas optimiser le seuil V2 sur NEAR.**

La meilleure réponse architecturale est celle déjà expérimentée par V3 : ne pas faire de l'amplitude 15m >= 6 % un veto binaire, mais conserver la qualité du plan, la géométrie de risque et la possibilité de WAIT/revalidation.

## Responsabilité des versions

### OLD/V4

Responsable du raté au sens économique : oui. Il détecte NEAR tôt mais ne le convertit pas en recommandation exploitable assez tôt.

### Solaire V2

Responsable également : oui. Le scanner full-universe n'est pas le problème ; la combinaison **détecteur d'accélération courte + gate d'exécution dur** est trop restrictive pour ce type de trajectoire.

### V3

Le journal prospectif V3 commence le **2026-09-23 22:09 UTC**. Il serait méthodologiquement faux de lui attribuer les ratés des semaines précédentes.

Sur la branche actuelle, NEAR :

- ouvre une thèse persistante le **24 septembre 01:40:41 UTC** à **3,7718 EUR** ;
- obtient un `RAW_READY` le **24 septembre 02:16:27 UTC** à **3,8646 EUR** ;
- reste ensuite suivi en `REENTRY_READY_THESIS` ;
- à 17:58 UTC, le profil long affiche +60,73 % sur 7 jours et +49,67 points de force relative vs BTC sur 7 jours.

Cela montre que l'architecture actuelle traite effectivement mieux ce cas.

### V3.1

Le journal V3.1 commence le **2026-09-23 23:22 UTC**. Même réserve : pas de responsabilité possible pour le mouvement antérieur.

## Corrections déjà présentes dans l'architecture actuelle

1. **Garde de fraîcheur par marché du trend cache** : `research/trend_cache_guard.py`, exécuté avant V4, avec test de non-régression.
2. **Thèse persistante Opportunity != Entry** : un setup peut survivre à la disparition de l'accélération courte.
3. **Pullback / reclaim / re-entry** : la réentrée n'exige plus que le micro-signal initial reste actif.
4. **Pas de gate V2 fixe >= 6 % dans V3** : les échecs de structure sont des WAIT réversibles.
5. **Full-universe news + rotation dynamique + external spark**.
6. **Fair queues** : suppression du risque qu'un candidat reste indéfiniment derrière un top-N fixe.
7. **Promotion d'une `REENTRY_READY_THESIS` dans le flux candidat principal.**

## Défaut encore actif révélé par NEAR

La V3 actuelle n'ouvre une nouvelle thèse que si elle reçoit au moins l'un des déclencheurs suivants :

- fresh opportunity trigger (early quant + contexte positif, ou V2 confirmé) ;
- news positive suffisamment forte ;
- external spark.

En revanche, **la seule persistance d'un leader structurel de prix/force relative ne peut pas semer une thèse**. Le long-trend est calculé après sélection des marchés de thèse, donc il ne peut pas lui-même faire entrer un nouvel actif dans cette couche.

NEAR a été sauvé dans la V3 actuelle notamment parce qu'il disposait d'un contexte news positif. Un actif présentant le même comportement de prix sans news ni external spark pourrait encore être raté.

## Correction recommandée à tester en shadow

Ajouter un chemin général `STRUCTURAL_LEADER_SEED`, sans exception NEAR :

- source uniquement marché/prix, jamais le rendement futur ;
- full-universe ;
- persistance multi-cycles obligatoire ;
- combinaison de force relative 1h/4h, tendance 4h/24h, participation/volume et qualité de structure ;
- autoriser le seed d'une thèse même sans news ;
- **ne pas déclencher un BUY** : seulement ouvrir une thèse persistante ;
- le BUY reste soumis au pullback/reclaim ou à une entrée structurelle valide ;
- pénaliser les extensions trop verticales plutôt que supprimer le candidat ;
- mesurer prospectivement MFE, MAE, stop hit, net return, immobilisation et coût d'opportunité.

Ce chemin doit être évalué sur un panier de faux négatifs (NEAR, NIL, ONDO, FET et autres cas documentés), et sur des contrôles négatifs, avant toute promotion.

## Tests de non-régression proposés

1. Un profil de tendance périmé ne peut jamais créer un veto/CHASE négatif.
2. Une ancienne `ENTRY_WINDOW` forte peut être requalifiée après reset sans exiger un ancien BUY.
3. Un leader full-universe persistant peut ouvrir une thèse sans news.
4. Un leader très étendu ne déclenche pas automatiquement une entrée : il passe en WAIT/PULLBACK.
5. Un seuil de range 15m ne peut pas être l'unique raison d'effacer une opportunité si un plan structurel valide existe ; il peut réduire la qualité/taille ou imposer WAIT.
6. Les résultats NEAR ne doivent jamais être utilisés comme condition codée en dur.

## Décision d'audit

**NEAR est un faux négatif utile et reproductible.**  
Le problème n'est pas la couverture de l'univers. Le problème historique est la conversion entre :

`détection -> mémoire de l'opportunité -> requalification -> validation d'entrée`.

La V3 actuelle a déjà corrigé une part substantielle de cette chaîne. Le principal axe encore à tester est un **seed de leader structurel purement marché**, afin que la persistance d'un actif fort puisse ouvrir une thèse même sans news ni nouvelle accélération courte.
