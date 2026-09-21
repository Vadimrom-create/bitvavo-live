# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T07:11:40.610665+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 9.314 | entrée 7.800 | trend 8.750 | rang 8.532
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SUPER-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.774 | entrée 6.100 | trend 8.400 | rang 7.962
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : PENDLE-EUR | action LATENT_ACCELERATOR | opportunité 7.768 | entrée 4.500 | trend 8.650 | rang 7.462
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.055 | entrée 6.450 | trend 8.900 | rang 7.877
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.532
2. SUPER-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.962
3. AIOZ-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.950

## Accélération indépendante

- IKA-EUR — CONFIRMED_ACCELERATION — score 6.825/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — BUILDING_ACCELERATION — score 6.381/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DUSK-EUR — BUILDING_ACCELERATION — score 6.111/10 — DETECTED_BUT_TOO_LATE
- HUMA-EUR — BUILDING_ACCELERATION — score 6.082/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INIT-EUR — BUILDING_ACCELERATION — score 6.041/10 — DETECTED_BUT_TOO_LATE
- MEGA-EUR — BUILDING_ACCELERATION — score 5.145/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OSMO-EUR — BUILDING_ACCELERATION — score 4.917/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CTC-EUR — MEMORY_24H — score mémoire 9.245/10 — sources ACCELERATION — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.049/10 — sources ACCELERATION — MEMORY_ONLY
- FORM-EUR — MEMORY_24H — score mémoire 8.879/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BOME-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HOME-EUR — MEMORY_24H — score mémoire 8.582/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ONDO-EUR — ACTIVE_NOW — score mémoire 8.532/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- USELESS-EUR — MEMORY_24H — score mémoire 8.481/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +63.40% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PTB-EUR +49.63% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +42.42% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +34.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +30.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EPIC-EUR +28.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NEAR-EUR +24.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +23.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VVV-EUR +22.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +18.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
