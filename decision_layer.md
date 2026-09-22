# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T06:01:02.668430+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SOL-EUR | action ACHETE_MAINTENANT | opportunité 8.816 | entrée 7.150 | trend 8.500 | rang 8.184
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : COW-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.009 | entrée 6.000 | trend 8.500 | rang 7.532
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MOVR-EUR | action LATENT_ACCELERATOR | opportunité 9.064 | entrée 4.950 | trend 7.550 | rang 7.533
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SSV-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.575 | entrée 5.600 | trend 9.000 | rang 8.064
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.184
2. SSV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.064
3. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.052

## Accélération indépendante

- AIXBT-EUR — CONFIRMED_ACCELERATION — score 7.801/10 — DETECTED_BUT_TOO_LATE
- 0G-EUR — CONFIRMED_ACCELERATION — score 7.322/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CPOOL-EUR — CONFIRMED_ACCELERATION — score 7.196/10 — DETECTED_BUT_TOO_LATE
- DEGEN-EUR — CONFIRMED_ACCELERATION — score 7.029/10 — DETECTED_BUT_TOO_LATE
- BOME-EUR — CONFIRMED_ACCELERATION — score 6.778/10 — DETECTED_BUT_TOO_LATE
- RED-EUR — BUILDING_ACCELERATION — score 6.423/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BREV-EUR — BUILDING_ACCELERATION — score 6.404/10 — DETECTED_BUT_TOO_LATE
- ARX-EUR — BUILDING_ACCELERATION — score 6.299/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XYO-EUR — BUILDING_ACCELERATION — score 6.224/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POPCAT-EUR — BUILDING_ACCELERATION — score 5.953/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PUMP-EUR — ACTIVE_NOW — score mémoire 6.739/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZRC-EUR — MEMORY_24H — score mémoire 9.953/10 — sources ACCELERATION — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 9.177/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.781/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MEW-EUR — MEMORY_24H — score mémoire 8.523/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.438/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +93.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +82.28% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AIOZ-EUR +54.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +33.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +28.62% — DETECTED_EARLY — couche NONE — action NONE
- GRASS-EUR +22.73% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +21.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TAO-EUR +20.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +20.58% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- WIF-EUR +19.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
