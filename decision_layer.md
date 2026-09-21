# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T12:53:24.606439+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PENDLE-EUR | action ACHETE_MAINTENANT | opportunité 8.237 | entrée 6.800 | trend 8.950 | rang 8.037
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ACH-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.968 | entrée 5.900 | trend 9.000 | rang 7.782
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COW-EUR | action LATENT_ACCELERATOR | opportunité 7.676 | entrée 4.500 | trend 8.950 | rang 7.493
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.733 | entrée 6.450 | trend 8.950 | rang 8.016
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PENDLE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.037
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.016
3. AERO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.984

## Accélération indépendante

- ARKM-EUR — CONFIRMED_ACCELERATION — score 9.893/10 — DETECTED_BUT_TOO_LATE
- ARB-EUR — CONFIRMED_ACCELERATION — score 8.746/10 — DETECTED_BUT_TOO_LATE
- VELO-EUR — CONFIRMED_ACCELERATION — score 8.430/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PROVE-EUR — CONFIRMED_ACCELERATION — score 8.183/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — CONFIRMED_ACCELERATION — score 7.311/10 — DETECTED_BUT_TOO_LATE
- PTB-EUR — CONFIRMED_ACCELERATION — score 6.954/10 — DETECTED_BUT_TOO_LATE
- SPK-EUR — CONFIRMED_ACCELERATION — score 6.589/10 — DETECTED_BUT_TOO_LATE
- LTC-EUR — CONFIRMED_ACCELERATION — score 6.505/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CAP-EUR — CONFIRMED_ACCELERATION — score 6.502/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZAMA-EUR — BUILDING_ACCELERATION — score 6.423/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LTC-EUR — ACTIVE_NOW — score mémoire 7.574/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 9.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARKM-EUR — ACTIVE_NOW — score mémoire 9.893/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- TAI-EUR — MEMORY_24H — score mémoire 9.488/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 9.465/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMX-EUR — MEMORY_24H — score mémoire 9.317/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 9.053/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARB-EUR — ACTIVE_NOW — score mémoire 8.746/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.457/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +69.21% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +66.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +50.37% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- KMNO-EUR +32.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +31.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +29.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +28.06% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AIOZ-EUR +26.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUI-EUR +26.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARKM-EUR +24.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
