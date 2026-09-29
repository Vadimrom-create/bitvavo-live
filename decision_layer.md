# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T22:51:29.091615+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ZRO-EUR | action ACHETE_MAINTENANT | opportunité 8.945 | entrée 6.950 | trend 8.150 | rang 7.838
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : JASMY-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.263 | entrée 6.050 | trend 9.000 | rang 8.007
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : HUMA-EUR | action LATENT_ACCELERATOR | opportunité 7.708 | entrée 5.750 | trend 8.900 | rang 7.672
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : CRV-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.480 | entrée 6.550 | trend 9.000 | rang 8.627
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ZRO-EUR — ACHETE_MAINTENANT — rank 7.838 — opportunité 8.945 — entrée 6.950 — trend 8.150
2. AAVE-EUR — ACHETE_MAINTENANT — rank 7.818 — opportunité 8.554 — entrée 7.200 — trend 8.900
3. ETHFI-EUR — ACHETE_MAINTENANT — rank 7.766 — opportunité 8.359 — entrée 7.050 — trend 8.950

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. CRV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.627
2. COMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.123
3. JASMY-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.007

## Accélération indépendante

- PHA-EUR — CONFIRMED_ACCELERATION — score 9.888/10 — DETECTED_BUT_TOO_LATE
- EDGE-EUR — CONFIRMED_ACCELERATION — score 8.544/10 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — CONFIRMED_ACCELERATION — score 7.382/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — CONFIRMED_ACCELERATION — score 6.935/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QKC-EUR — BUILDING_ACCELERATION — score 5.758/10 — DETECTED_BUT_TOO_LATE
- TRIA-EUR — BUILDING_ACCELERATION — score 5.153/10 — DETECTED_BUT_TOO_LATE
- ALICE-EUR — BUILDING_ACCELERATION — score 4.809/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ZRO-EUR — ACTIVE_NOW — score mémoire 7.838/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PHA-EUR — ACTIVE_NOW — score mémoire 9.888/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NOS-EUR — MEMORY_24H — score mémoire 9.477/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 9.160/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.866/10 — sources ACCELERATION — MEMORY_ONLY
- CRV-EUR — ACTIVE_NOW — score mémoire 8.627/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- EDGE-EUR — ACTIVE_NOW — score mémoire 8.544/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- COMP-EUR — ACTIVE_NOW — score mémoire 8.123/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +36.12% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRASS-EUR +30.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVR-EUR +26.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +24.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUMP-EUR +22.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZBCN-EUR +22.00% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- 0G-EUR +19.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +18.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XDP-EUR +15.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TRIA-EUR +14.53% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
