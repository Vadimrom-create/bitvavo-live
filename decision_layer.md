# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T07:50:39.650115+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 9.205 | entrée 7.400 | trend 8.900 | rang 8.532
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : DYM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.924 | entrée 5.800 | trend 8.200 | rang 7.488
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COMP-EUR | action LATENT_ACCELERATOR | opportunité 7.465 | entrée 4.500 | trend 8.450 | rang 7.212
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : JUP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.086 | entrée 7.100 | trend 8.950 | rang 7.989
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.532
2. JUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.989
3. ZRO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.940

## Accélération indépendante

- NIL-EUR — CONFIRMED_ACCELERATION — score 8.160/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — CONFIRMED_ACCELERATION — score 7.203/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — CONFIRMED_ACCELERATION — score 6.736/10 — DETECTED_BUT_TOO_LATE
- NOM-EUR — BUILDING_ACCELERATION — score 5.667/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — BUILDING_ACCELERATION — score 5.581/10 — DETECTED_BUT_TOO_LATE
- ARK-EUR — BUILDING_ACCELERATION — score 5.391/10 — DETECTED_BUT_TOO_LATE
- JASMY-EUR — BUILDING_ACCELERATION — score 4.876/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- UP-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.532/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- NIL-EUR — ACTIVE_NOW — score mémoire 8.160/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NOS-EUR — MEMORY_24H — score mémoire 8.008/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.989/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 7.940/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- TREAD-EUR +52.86% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- QNT-EUR +38.94% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +27.77% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +26.13% — DETECTED_EARLY — couche NONE — action NONE
- ARK-EUR +20.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +19.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +18.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DBR-EUR +18.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FET-EUR +15.34% — DETECTED_EARLY — couche NONE — action NONE
- LDO-EUR +14.96% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
