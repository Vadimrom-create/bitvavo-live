# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T04:22:03.391868+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : INJ-EUR | action LATENT_ACCELERATOR | opportunité 7.563 | entrée 5.400 | trend 8.300 | rang 6.930
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RAY-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.481 | entrée 6.050 | trend 8.000 | rang 7.210
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RAY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.210
2. INJ-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.930
3. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.886

## Accélération indépendante

- C-EUR — CONFIRMED_ACCELERATION — score 8.029/10 — DETECTED_BUT_TOO_LATE
- CELR-EUR — BUILDING_ACCELERATION — score 5.598/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- C-EUR — ACTIVE_NOW — score mémoire 8.029/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — MEMORY_24H — score mémoire 7.949/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.930/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.889/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DOT-EUR — MEMORY_24H — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- 0G-EUR — ACTIVE_NOW — score mémoire 7.813/10 — sources V4 — WATCH_ONLY
- ETC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources V4 — MEMORY_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 7.700/10 — sources V4 — MEMORY_ONLY
- AAVE-EUR — MEMORY_24H — score mémoire 7.654/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PROVE-EUR — MEMORY_24H — score mémoire 7.637/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CELR-EUR +89.55% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +48.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +39.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +24.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +19.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +17.46% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +16.72% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +15.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HEI-EUR +15.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKL-EUR +14.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
