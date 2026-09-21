# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T04:55:42.219868+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.009 | entrée 7.600 | trend 8.000 | rang 7.615
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : DYM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.958 | entrée 6.100 | trend 7.350 | rang 7.559
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DEEP-EUR | action LATENT_ACCELERATOR | opportunité 9.319 | entrée 5.500 | trend 8.950 | rang 8.214
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AIOZ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.272 | entrée 6.750 | trend 8.550 | rang 8.341
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AIOZ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.341
2. DEEP-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 8.214
3. WAL-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.982

## Accélération indépendante

- ZETA-EUR — CONFIRMED_ACCELERATION — score 8.427/10 — DETECTED_BUT_TOO_LATE
- KERNEL-EUR — CONFIRMED_ACCELERATION — score 7.662/10 — DETECTED_BUT_TOO_LATE
- TOSHI-EUR — CONFIRMED_ACCELERATION — score 7.369/10 — DETECTED_BUT_TOO_LATE
- WAL-EUR — CONFIRMED_ACCELERATION — score 7.092/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XVG-EUR — CONFIRMED_ACCELERATION — score 6.965/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBCN-EUR — CONFIRMED_ACCELERATION — score 6.855/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- METIS-EUR — BUILDING_ACCELERATION — score 6.423/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BLUR-EUR — BUILDING_ACCELERATION — score 6.240/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRO-EUR — BUILDING_ACCELERATION — score 5.821/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MERL-EUR — BUILDING_ACCELERATION — score 5.795/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- FTT-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- FORM-EUR — MEMORY_24H — score mémoire 8.879/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BOME-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SAFE-EUR — MEMORY_24H — score mémoire 8.565/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- USELESS-EUR — MEMORY_24H — score mémoire 8.481/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZETA-EUR — ACTIVE_NOW — score mémoire 8.427/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- U-EUR — MEMORY_24H — score mémoire 8.376/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +75.24% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PTB-EUR +68.87% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +39.70% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +27.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NEAR-EUR +26.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +25.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VVV-EUR +22.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +20.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +20.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +19.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
