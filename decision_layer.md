# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T02:24:44.403676+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.598 | entrée 6.950 | trend 8.900 | rang 8.196
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : HUMA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.652 | entrée 6.200 | trend 8.650 | rang 7.578
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : FLUID-EUR | action LATENT_ACCELERATOR | opportunité 7.726 | entrée 5.350 | trend 9.000 | rang 7.676
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : IMX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.976 | entrée 6.350 | trend 8.700 | rang 8.016
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.196 — opportunité 8.598 — entrée 6.950 — trend 8.900
2. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.438 — opportunité 7.695 — entrée 7.100 — trend 8.150
3. WLD-EUR — ACHETE_MAINTENANT — rank 7.396 — opportunité 8.226 — entrée 6.950 — trend 8.700
4. UNI-EUR — ACHETE_MAINTENANT — rank 7.218 — opportunité 8.800 — entrée 7.500 — trend 6.100

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.196
2. IMX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.016
3. ZRO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.994

## Accélération indépendante

- FOLD-EUR — CONFIRMED_ACCELERATION — score 7.055/10 — DETECTED_BUT_TOO_LATE
- LPT-EUR — CONFIRMED_ACCELERATION — score 6.873/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CT-EUR — BUILDING_ACCELERATION — score 6.471/10 — DETECTED_BUT_TOO_LATE
- WLD-EUR — BUILDING_ACCELERATION — score 6.008/10 — DETECTED_BUT_TOO_LATE
- ME-EUR — BUILDING_ACCELERATION — score 5.867/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAND-EUR — BUILDING_ACCELERATION — score 5.729/10 — DETECTED_BUT_TOO_LATE
- SWEAT-EUR — BUILDING_ACCELERATION — score 5.665/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QNT-EUR — BUILDING_ACCELERATION — score 5.568/10 — DETECTED_BUT_TOO_LATE
- SKY-EUR — BUILDING_ACCELERATION — score 5.099/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OP-EUR — BUILDING_ACCELERATION — score 4.836/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.196/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 8.016/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 7.994/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SKY-EUR — ACTIVE_NOW — score mémoire 7.882/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +54.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENJ-EUR +16.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GALA-EUR +14.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +13.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WLD-EUR +12.75% — DETECTED_EARLY — couche NONE — action NONE
- ATH-EUR +12.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APE-EUR +11.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +11.02% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TREAD-EUR +9.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BAT-EUR +8.90% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
