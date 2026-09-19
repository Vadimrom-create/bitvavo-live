# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T09:55:08.016257+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 9.169 | entrée 7.600 | trend 7.650 | rang 8.016
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RAY-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.764 | entrée 6.200 | trend 8.300 | rang 7.349
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SOL-EUR | action LATENT_ACCELERATOR | opportunité 7.480 | entrée 4.500 | trend 8.250 | rang 7.191
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AVAX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.246 | entrée 8.200 | trend 8.450 | rang 8.170
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AVAX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.170
2. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.016
3. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.739

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- TAO-EUR — ACTIVE_NOW — score mémoire 7.352/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- FET-EUR — ACTIVE_NOW — score mémoire 7.223/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AERO-EUR — ACTIVE_NOW — score mémoire 8.415/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.177/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.171/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AVAX-EUR — ACTIVE_NOW — score mémoire 8.170/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- JUP-EUR — ACTIVE_NOW — score mémoire 8.136/10 — sources V4 — WATCH_ONLY
- SYN-EUR — MEMORY_24H — score mémoire 8.094/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 8.078/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.072/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +36.32% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HEI-EUR +33.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +32.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +31.70% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +31.02% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +28.21% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- XTZ-EUR +26.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +26.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +25.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +25.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
