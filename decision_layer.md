# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T07:46:40.131526+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 7.906 | entrée 7.350 | trend 8.500 | rang 7.802
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SOL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.675 | entrée 6.450 | trend 8.250 | rang 7.506
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : APT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.431 | entrée 5.250 | trend 8.450 | rang 7.330
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.802
2. SOL-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.506
3. APT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.330

## Accélération indépendante

- G-EUR — CONFIRMED_ACCELERATION — score 9.927/10 — DETECTED_BUT_TOO_LATE
- SYN-EUR — BUILDING_ACCELERATION — score 5.152/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- G-EUR — ACTIVE_NOW — score mémoire 9.927/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- A-EUR — ACTIVE_NOW — score mémoire 8.295/10 — sources V4 — WATCH_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.067/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.047/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 8.033/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.955/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.921/10 — sources V4 — WATCH_ONLY
- RAY-EUR — ACTIVE_NOW — score mémoire 7.870/10 — sources ACCELERATION, V4 — WATCH_ONLY
- SSV-EUR — MEMORY_24H — score mémoire 7.845/10 — sources V4 — MEMORY_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.829/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- EDGE-EUR +53.70% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +31.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +28.61% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +28.12% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +26.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HEI-EUR +25.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +24.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +21.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +19.95% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- EPIC-EUR +17.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
