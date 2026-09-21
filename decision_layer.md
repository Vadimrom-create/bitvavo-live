# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T21:36:39.996837+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 8.178 | entrée 7.400 | trend 8.700 | rang 7.868
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZIL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.817 | entrée 6.100 | trend 8.650 | rang 7.682
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CELO-EUR | action LATENT_ACCELERATOR | opportunité 7.870 | entrée 5.200 | trend 8.700 | rang 7.588
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GRT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.263 | entrée 6.450 | trend 8.600 | rang 8.336
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. GRT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.336
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.995
3. AVAX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.920

## Accélération indépendante

- SYRUP-EUR — BUILDING_ACCELERATION — score 5.921/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ATH-EUR — BUILDING_ACCELERATION — score 5.194/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SWELL-EUR — BUILDING_ACCELERATION — score 5.167/10 — DETECTED_BUT_TOO_LATE
- MEGA-EUR — BUILDING_ACCELERATION — score 4.795/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- STX-EUR — ACTIVE_NOW — score mémoire 7.738/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- GIGA-EUR — MEMORY_24H — score mémoire 9.738/10 — sources ACCELERATION — MEMORY_ONLY
- ZKJ-EUR — MEMORY_24H — score mémoire 9.182/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- THQ-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 8.767/10 — sources ACCELERATION — MEMORY_ONLY
- LUMIA-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 8.336/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SFP-EUR — MEMORY_24H — score mémoire 8.323/10 — sources ACCELERATION — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.995/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +117.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +96.26% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZETA-EUR +53.36% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- FORM-EUR +39.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +37.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +36.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SWELL-EUR +30.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +30.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +25.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +24.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
