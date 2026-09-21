# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T04:20:28.311977+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KAS-EUR | action ACHETE_MAINTENANT | opportunité 9.367 | entrée 7.000 | trend 8.700 | rang 8.507
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.846 | entrée 5.950 | trend 8.200 | rang 7.207
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ACH-EUR | action LATENT_ACCELERATOR | opportunité 8.070 | entrée 5.700 | trend 8.450 | rang 7.678
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.374 | entrée 6.200 | trend 8.900 | rang 8.436
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.507
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.436
3. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.061

## Accélération indépendante

- KERNEL-EUR — CONFIRMED_ACCELERATION — score 9.153/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FORM-EUR — CONFIRMED_ACCELERATION — score 8.879/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAFE-EUR — CONFIRMED_ACCELERATION — score 8.565/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZKC-EUR — CONFIRMED_ACCELERATION — score 7.327/10 — DETECTED_BUT_TOO_LATE
- MOCA-EUR — CONFIRMED_ACCELERATION — score 7.280/10 — DETECTED_BUT_TOO_LATE
- LAYER-EUR — CONFIRMED_ACCELERATION — score 6.904/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZETA-EUR — BUILDING_ACCELERATION — score 6.456/10 — DETECTED_BUT_TOO_LATE
- FRAX-EUR — BUILDING_ACCELERATION — score 6.289/10 — DETECTED_BUT_TOO_LATE
- ZKP-EUR — BUILDING_ACCELERATION — score 6.116/10 — DETECTED_BUT_TOO_LATE
- CAP-EUR — BUILDING_ACCELERATION — score 5.952/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PUMP-EUR — ACTIVE_NOW — score mémoire 5.303/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- FTT-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KERNEL-EUR — ACTIVE_NOW — score mémoire 9.153/10 — sources ACCELERATION, V4 — WATCH_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 8.879/10 — sources ACCELERATION, V4 — WATCH_ONLY
- BOME-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SAFE-EUR — ACTIVE_NOW — score mémoire 8.565/10 — sources ACCELERATION, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.507/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- PTB-EUR +96.61% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZETA-EUR +75.24% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- FTT-EUR +42.09% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +28.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +26.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +22.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VVV-EUR +21.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +19.05% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +17.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- S-EUR +17.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
