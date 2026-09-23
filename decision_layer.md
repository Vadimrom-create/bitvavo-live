# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T05:18:17.294450+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.656 | entrée 8.200 | trend 8.500 | rang 8.097
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RECALL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.947 | entrée 6.400 | trend 7.300 | rang 7.605
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BTT-EUR | action LATENT_ACCELERATOR | opportunité 9.000 | entrée 5.550 | trend 8.450 | rang 7.599
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : QNT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.334 | entrée 7.950 | trend 8.700 | rang 8.061
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.097
2. QNT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.061
3. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.042

## Accélération indépendante

- BTT-EUR — CONFIRMED_ACCELERATION — score 8.755/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRASS-EUR — CONFIRMED_ACCELERATION — score 8.627/10 — DETECTED_BUT_TOO_LATE
- THQ-EUR — CONFIRMED_ACCELERATION — score 8.568/10 — DETECTED_BUT_TOO_LATE
- NOS-EUR — CONFIRMED_ACCELERATION — score 7.051/10 — DETECTED_BUT_TOO_LATE
- CSPR-EUR — CONFIRMED_ACCELERATION — score 6.821/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — CONFIRMED_ACCELERATION — score 6.795/10 — DETECTED_BUT_TOO_LATE
- POWR-EUR — BUILDING_ACCELERATION — score 6.466/10 — DETECTED_BUT_TOO_LATE
- HNT-EUR — BUILDING_ACCELERATION — score 6.153/10 — DETECTED_BUT_TOO_LATE
- LIGHTER-EUR — BUILDING_ACCELERATION — score 6.001/10 — DETECTED_BUT_TOO_LATE
- GRT-EUR — BUILDING_ACCELERATION — score 5.515/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- SAGA-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BTT-EUR — ACTIVE_NOW — score mémoire 8.755/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GRASS-EUR — ACTIVE_NOW — score mémoire 8.627/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- THQ-EUR — ACTIVE_NOW — score mémoire 8.568/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.118/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 8.097/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QNT-EUR — ACTIVE_NOW — score mémoire 8.061/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- NIL-EUR +43.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +33.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +32.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BCH-EUR +29.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +28.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CHR-EUR +27.43% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SUPER-EUR +24.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PENGU-EUR +22.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +22.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FLOCK-EUR +20.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
