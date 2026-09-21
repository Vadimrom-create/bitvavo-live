# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T16:01:23.740055+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : COW-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.960 | entrée 6.100 | trend 8.900 | rang 7.838
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ROSE-EUR | action LATENT_ACCELERATOR | opportunité 7.818 | entrée 5.750 | trend 8.450 | rang 7.548
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KAS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.648 | entrée 7.350 | trend 8.700 | rang 8.078
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.078
2. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.977
3. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.911

## Accélération indépendante

- SAGA-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- NEIRO-EUR — CONFIRMED_ACCELERATION — score 8.894/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- FARTCOIN-EUR — CONFIRMED_ACCELERATION — score 8.408/10 — DETECTED_BUT_TOO_LATE
- FLOKI-EUR — CONFIRMED_ACCELERATION — score 8.049/10 — DETECTED_BUT_TOO_LATE
- BONK-EUR — CONFIRMED_ACCELERATION — score 7.010/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — BUILDING_ACCELERATION — score 6.231/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEAQ-EUR — BUILDING_ACCELERATION — score 6.203/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — BUILDING_ACCELERATION — score 6.000/10 — DETECTED_BUT_TOO_LATE
- SHIB-EUR — BUILDING_ACCELERATION — score 5.748/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SAGA-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- RON-EUR — MEMORY_24H — score mémoire 9.938/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CPOOL-EUR — MEMORY_24H — score mémoire 9.834/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEPE-EUR — MEMORY_24H — score mémoire 9.525/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- THQ-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 9.053/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NEIRO-EUR — ACTIVE_NOW — score mémoire 8.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +250.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZETA-EUR +58.26% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +36.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AIOZ-EUR +32.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +29.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEPE-EUR +29.16% — DETECTED_EARLY — couche NONE — action NONE
- PTB-EUR +28.40% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- KMNO-EUR +23.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WIF-EUR +23.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +22.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
