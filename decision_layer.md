# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-08T10:20:21.423775+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : MAGIC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.474 | entrée 6.150 | trend 8.650 | rang 7.250
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ALGO-EUR | action LATENT_ACCELERATOR | opportunité 7.517 | entrée 5.300 | trend 8.950 | rang 6.491
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : NMR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.798 | entrée 6.300 | trend 8.650 | rang 7.511
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. NMR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.511
2. MAGIC-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.250
3. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.049

## Accélération indépendante

- CTSI-EUR — CONFIRMED_ACCELERATION — score 9.155/10 — DETECTED_BUT_TOO_LATE
- OGN-EUR — CONFIRMED_ACCELERATION — score 8.541/10 — DETECTED_BUT_TOO_LATE
- FOLD-EUR — CONFIRMED_ACCELERATION — score 7.202/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PROM-EUR — BUILDING_ACCELERATION — score 6.135/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHR-EUR — BUILDING_ACCELERATION — score 5.295/10 — DETECTED_BUT_TOO_LATE
- ZK-EUR — BUILDING_ACCELERATION — score 5.211/10 — DETECTED_BUT_TOO_LATE
- EDU-EUR — BUILDING_ACCELERATION — score 5.058/10 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — BUILDING_ACCELERATION — score 4.985/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SWELL-EUR — MEMORY_24H — score mémoire 9.284/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTSI-EUR — ACTIVE_NOW — score mémoire 9.155/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- OGN-EUR — ACTIVE_NOW — score mémoire 8.541/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NOS-EUR — MEMORY_24H — score mémoire 8.214/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_DECAY_24_72H — score mémoire 7.963/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NMR-EUR — ACTIVE_NOW — score mémoire 7.511/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 7.495/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AAVE-EUR — MEMORY_24H — score mémoire 7.340/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MAGIC-EUR — ACTIVE_NOW — score mémoire 7.250/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FOLD-EUR — ACTIVE_NOW — score mémoire 7.202/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- MET-EUR +63.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OGN-EUR +37.75% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +31.78% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOS-EUR +21.52% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- QUID-EUR +18.81% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALGO-EUR +17.86% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- JUP-EUR +17.00% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- W-EUR +15.79% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WIN-EUR +14.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +13.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

## Gestion des positions détenues

Policy : STAGED_10_20_RUNNER_V1
- +10% : prise partielle 35%.
- +20% : seconde prise 35%.
- Runner conservé : 30%.
- Revue coût d'opportunité après 72 h ; sortie seulement avant la première partielle, proche/sous le PRU et avec momentum 15m affaibli.
- Pas de stop serré mécaniquement après une petite hausse ; le stop reste lié à l'invalidation structurelle.

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
