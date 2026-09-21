# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T13:09:20.489356+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : STX-EUR | action ACHETE_MAINTENANT | opportunité 8.074 | entrée 7.050 | trend 8.600 | rang 7.836
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : COW-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.910 | entrée 5.850 | trend 9.200 | rang 7.875
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZK-EUR | action LATENT_ACCELERATOR | opportunité 7.666 | entrée 4.500 | trend 8.700 | rang 7.422
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RSR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.229 | entrée 7.100 | trend 8.450 | rang 8.306
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RSR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.306
2. ACH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.068
3. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.032

## Accélération indépendante

- AIOZ-EUR — CONFIRMED_ACCELERATION — score 7.537/10 — DETECTED_BUT_TOO_LATE
- KMNO-EUR — CONFIRMED_ACCELERATION — score 6.934/10 — DETECTED_BUT_TOO_LATE
- VELO-EUR — CONFIRMED_ACCELERATION — score 6.781/10 — DETECTED_BUT_TOO_LATE
- DEEP-EUR — BUILDING_ACCELERATION — score 6.279/10 — DETECTED_BUT_TOO_LATE
- ARX-EUR — BUILDING_ACCELERATION — score 6.123/10 — DETECTED_BUT_TOO_LATE
- SXT-EUR — BUILDING_ACCELERATION — score 6.102/10 — DETECTED_BUT_TOO_LATE
- BLUR-EUR — BUILDING_ACCELERATION — score 5.893/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CPOOL-EUR — BUILDING_ACCELERATION — score 5.807/10 — DETECTED_BUT_TOO_LATE
- WIF-EUR — BUILDING_ACCELERATION — score 5.787/10 — DETECTED_BUT_TOO_LATE
- PUNDIX-EUR — BUILDING_ACCELERATION — score 5.049/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ALGO-EUR — ACTIVE_NOW — score mémoire 7.832/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- RAY-EUR — ACTIVE_NOW — score mémoire 7.342/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- TIA-EUR — ACTIVE_NOW — score mémoire 7.152/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 9.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARKM-EUR — MEMORY_24H — score mémoire 9.893/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.488/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 9.465/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 9.053/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARB-EUR — MEMORY_24H — score mémoire 8.746/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +68.67% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +64.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +48.33% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- KMNO-EUR +33.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +32.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +32.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +29.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUI-EUR +28.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FTT-EUR +26.70% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +25.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
