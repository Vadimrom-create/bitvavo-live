# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T05:33:16.070810+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 7.925 | entrée 7.650 | trend 8.000 | rang 7.628
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : STX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.608 | entrée 6.500 | trend 8.650 | rang 7.634
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : PENDLE-EUR | action LATENT_ACCELERATOR | opportunité 8.261 | entrée 5.550 | trend 8.950 | rang 7.928
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AIOZ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.960 | entrée 6.950 | trend 8.550 | rang 7.767
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PENDLE-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.928
2. AIOZ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.767
3. ONDO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.729

## Accélération indépendante

- HOME-EUR — CONFIRMED_ACCELERATION — score 8.582/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — BUILDING_ACCELERATION — score 5.856/10 — DETECTED_BUT_TOO_LATE
- CPOOL-EUR — BUILDING_ACCELERATION — score 5.811/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KERNEL-EUR — BUILDING_ACCELERATION — score 5.500/10 — DETECTED_BUT_TOO_LATE
- WLD-EUR — BUILDING_ACCELERATION — score 5.012/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REZ-EUR — BUILDING_ACCELERATION — score 5.008/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEAQ-EUR — BUILDING_ACCELERATION — score 4.887/10 — DETECTED_BUT_TOO_LATE
- SYN-EUR — BUILDING_ACCELERATION — score 4.824/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FORM-EUR — MEMORY_24H — score mémoire 8.879/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BOME-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HOME-EUR — ACTIVE_NOW — score mémoire 8.582/10 — sources ACCELERATION, V4 — WATCH_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- USELESS-EUR — MEMORY_24H — score mémoire 8.481/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZETA-EUR — MEMORY_24H — score mémoire 8.427/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.376/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BLUR-EUR — MEMORY_24H — score mémoire 8.302/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.928/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +60.80% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- FTT-EUR +46.47% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +43.93% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +31.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +26.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NEAR-EUR +25.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +23.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VVV-EUR +20.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +18.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +18.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
