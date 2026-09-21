# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T06:30:05.564047+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 9.293 | entrée 8.050 | trend 8.450 | rang 8.351
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : STX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.793 | entrée 6.000 | trend 8.650 | rang 7.627
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : WAL-EUR | action LATENT_ACCELERATOR | opportunité 8.254 | entrée 5.750 | trend 9.200 | rang 7.824
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.922 | entrée 7.650 | trend 8.900 | rang 7.952
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.351
2. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.343
3. TAO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.019

## Accélération indépendante

- DRIFT-EUR — CONFIRMED_ACCELERATION — score 9.955/10 — DETECTED_BUT_TOO_LATE
- APT-EUR — CONFIRMED_ACCELERATION — score 9.739/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CTC-EUR — CONFIRMED_ACCELERATION — score 9.245/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- CETUS-EUR — CONFIRMED_ACCELERATION — score 7.544/10 — DETECTED_BUT_TOO_LATE
- DYDX-EUR — CONFIRMED_ACCELERATION — score 7.474/10 — DETECTED_BUT_TOO_LATE
- HAEDAL-EUR — CONFIRMED_ACCELERATION — score 6.647/10 — DETECTED_BUT_TOO_LATE
- RENDER-EUR — BUILDING_ACCELERATION — score 6.474/10 — DETECTED_BUT_TOO_LATE
- PENGU-EUR — BUILDING_ACCELERATION — score 5.991/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOT-EUR — BUILDING_ACCELERATION — score 5.936/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- APT-EUR — ACTIVE_NOW — score mémoire 9.739/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ONDO-EUR — ACTIVE_NOW — score mémoire 8.351/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- DRIFT-EUR — ACTIVE_NOW — score mémoire 9.955/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- INIT-EUR — MEMORY_24H — score mémoire 9.655/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTC-EUR — ACTIVE_NOW — score mémoire 9.245/10 — sources ACCELERATION — WATCH_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.049/10 — sources ACCELERATION — MEMORY_ONLY
- FORM-EUR — MEMORY_24H — score mémoire 8.879/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BOME-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HOME-EUR — MEMORY_24H — score mémoire 8.582/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +68.11% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PTB-EUR +57.77% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +49.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +37.05% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +26.69% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +24.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +23.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +21.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +21.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- VVV-EUR +21.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
