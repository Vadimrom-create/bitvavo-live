# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T10:13:53.228701+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAO-EUR | action ACHETE_MAINTENANT | opportunité 8.725 | entrée 7.200 | trend 7.700 | rang 7.617
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : HYPE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.774 | entrée 6.500 | trend 8.750 | rang 7.737
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SOL-EUR | action LATENT_ACCELERATOR | opportunité 7.525 | entrée 4.500 | trend 8.250 | rang 7.205
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AVAX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.043 | entrée 7.400 | trend 7.900 | rang 7.634
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.737
2. AVAX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.634
3. TAO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.617

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- TAO-EUR — ACTIVE_NOW — score mémoire 7.617/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ONDO-EUR — ACTIVE_NOW — score mémoire 7.473/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PROVE-EUR — ACTIVE_NOW — score mémoire 8.539/10 — sources V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.157/10 — sources V4 — WATCH_ONLY
- SYN-EUR — MEMORY_24H — score mémoire 8.094/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.067/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.047/10 — sources V4 — DETECTED_BUT_TOO_LATE
- LPT-EUR — ACTIVE_NOW — score mémoire 8.030/10 — sources ACCELERATION, V4 — WATCH_ONLY
- ARX-EUR — ACTIVE_NOW — score mémoire 8.020/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.989/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- EDGE-EUR +48.16% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +35.41% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +31.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HEI-EUR +29.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +28.62% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +27.96% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- XTZ-EUR +26.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +25.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +23.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +23.54% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
