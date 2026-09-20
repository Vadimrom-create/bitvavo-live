# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T11:41:01.944115+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : ZAMA-EUR | action LATENT_ACCELERATOR | opportunité 7.510 | entrée 5.550 | trend 7.950 | rang 6.466
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ENA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.863 | entrée 6.700 | trend 8.500 | rang 7.373
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.373
2. AVAX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.357
3. ZIL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.896

## Accélération indépendante

- G-EUR — BUILDING_ACCELERATION — score 5.682/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- ZAMA-EUR — BUILDING_ACCELERATION — score 5.285/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CAKE-EUR — ACTIVE_NOW — score mémoire 8.300/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.960/10 — sources V4 — WATCH_ONLY
- COTI-EUR — MEMORY_24H — score mémoire 7.904/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.872/10 — sources V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.863/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.841/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.766/10 — sources V4 — WATCH_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 7.683/10 — sources V4 — WATCH_ONLY
- BIGTIME-EUR — MEMORY_24H — score mémoire 7.662/10 — sources V4 — MEMORY_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.638/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +72.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +15.70% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +14.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +14.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENSO-EUR +12.69% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CTSI-EUR +12.52% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKL-EUR +10.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +9.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALLO-EUR +8.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +8.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
