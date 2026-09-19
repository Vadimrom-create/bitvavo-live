# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T06:23:13.706786+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : APT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.428 | entrée 6.000 | trend 8.450 | rang 7.179
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.149 | entrée 6.300 | trend 8.950 | rang 7.953
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.953
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.527
3. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.489

## Accélération indépendante

- SYN-EUR — CONFIRMED_ACCELERATION — score 7.297/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.247/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.093/10 — sources V4 — DETECTED_BUT_TOO_LATE
- COTI-EUR — MEMORY_24H — score mémoire 7.972/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.953/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.863/10 — sources V4 — WATCH_ONLY
- SSV-EUR — MEMORY_24H — score mémoire 7.845/10 — sources V4 — MEMORY_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.838/10 — sources V4 — WATCH_ONLY
- ARX-EUR — ACTIVE_NOW — score mémoire 7.830/10 — sources V4 — WATCH_ONLY
- T-EUR — MEMORY_24H — score mémoire 7.733/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.707/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- EDGE-EUR +98.33% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +42.51% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +32.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +27.56% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ESP-EUR +27.32% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- F-EUR +26.39% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +22.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +20.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +20.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +19.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
