# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T00:00:14.448688+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : DATAIP-EUR | action ACHETE_MAINTENANT | opportunité 9.306 | entrée 7.400 | trend 8.700 | rang 8.530
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ATH-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.466 | entrée 5.850 | trend 9.200 | rang 8.066
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BRETT-EUR | action LATENT_ACCELERATOR | opportunité 8.078 | entrée 4.750 | trend 9.000 | rang 7.692
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : APE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.364 | entrée 7.100 | trend 8.700 | rang 8.463
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. DATAIP-EUR — ACHETE_MAINTENANT — rank 8.530 — opportunité 9.306 — entrée 7.400 — trend 8.700
2. AAVE-EUR — ACHETE_MAINTENANT — rank 8.482 — opportunité 9.071 — entrée 7.050 — trend 9.000
3. DOT-EUR — ACHETE_MAINTENANT — rank 8.390 — opportunité 8.976 — entrée 7.450 — trend 8.950
4. RENDER-EUR — ACHETE_MAINTENANT — rank 8.367 — opportunité 8.798 — entrée 7.300 — trend 9.200
5. TIA-EUR — ACHETE_MAINTENANT — rank 8.040 — opportunité 8.651 — entrée 7.000 — trend 8.650
6. LTC-EUR — ACHETE_MAINTENANT — rank 7.834 — opportunité 8.095 — entrée 7.350 — trend 8.400
7. SUI-EUR — ACHETE_MAINTENANT — rank 7.648 — opportunité 8.122 — entrée 6.900 — trend 8.850
8. PENGU-EUR — ACHETE_MAINTENANT — rank 7.365 — opportunité 8.810 — entrée 7.200 — trend 7.000
9. KMNO-EUR — ACHETE_MAINTENANT — rank 7.340 — opportunité 8.464 — entrée 6.900 — trend 7.800

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DATAIP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.530
2. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.482
3. APE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.463

## Accélération indépendante

- ONDO-EUR — CONFIRMED_ACCELERATION — score 9.187/10 — DETECTED_BUT_TOO_LATE
- TOSHI-EUR — CONFIRMED_ACCELERATION — score 7.894/10 — DETECTED_BUT_TOO_LATE
- IRYS-EUR — CONFIRMED_ACCELERATION — score 7.234/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 6.357/10 — DETECTED_BUT_TOO_LATE
- AVA-EUR — BUILDING_ACCELERATION — score 5.262/10 — DETECTED_BUT_TOO_LATE
- VELO-EUR — BUILDING_ACCELERATION — score 5.131/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DYM-EUR — BUILDING_ACCELERATION — score 5.019/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NES-EUR — BUILDING_ACCELERATION — score 4.787/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZORA-EUR — BUILDING_ACCELERATION — score 4.782/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CC-EUR — BUILDING_ACCELERATION — score 4.781/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TIA-EUR — ACTIVE_NOW — score mémoire 8.040/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EIGEN-EUR — ACTIVE_NOW — score mémoire 8.020/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- DGB-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ONDO-EUR — ACTIVE_NOW — score mémoire 9.187/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- DATAIP-EUR — ACTIVE_NOW — score mémoire 8.530/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.482/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- APE-EUR — ACTIVE_NOW — score mémoire 8.463/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- QNT-EUR — MEMORY_24H — score mémoire 8.429/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CFG-EUR — ACTIVE_NOW — score mémoire 8.412/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +86.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +44.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INX-EUR +30.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRT-EUR +29.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +21.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- W-EUR +19.57% — DETECTED_EARLY — couche NONE — action NONE
- PUMP-EUR +17.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IMX-EUR +16.54% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOM-EUR +14.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- JASMY-EUR +14.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
