# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T00:30:35.195964+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 9.526 | entrée 8.150 | trend 9.200 | rang 8.716
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RPL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.193 | entrée 5.900 | trend 8.700 | rang 7.816
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BRETT-EUR | action LATENT_ACCELERATOR | opportunité 8.362 | entrée 5.700 | trend 9.000 | rang 7.908
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : CFG-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.005 | entrée 6.950 | trend 8.750 | rang 8.231
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. RENDER-EUR — ACHETE_MAINTENANT — rank 8.716 — opportunité 9.526 — entrée 8.150 — trend 9.200
2. ALGO-EUR — ACHETE_MAINTENANT — rank 8.278 — opportunité 9.059 — entrée 7.150 — trend 8.700
3. AAVE-EUR — ACHETE_MAINTENANT — rank 8.192 — opportunité 8.437 — entrée 7.550 — trend 9.000
4. EIGEN-EUR — ACHETE_MAINTENANT — rank 8.086 — opportunité 8.717 — entrée 7.400 — trend 8.900
5. DOT-EUR — ACHETE_MAINTENANT — rank 8.008 — opportunité 8.289 — entrée 6.950 — trend 8.950
6. LINK-EUR — ACHETE_MAINTENANT — rank 8.001 — opportunité 8.274 — entrée 7.150 — trend 8.700
7. GMT-EUR — ACHETE_MAINTENANT — rank 7.993 — opportunité 8.323 — entrée 6.900 — trend 8.750
8. BABY-EUR — ACHETE_MAINTENANT — rank 7.817 — opportunité 8.211 — entrée 7.200 — trend 8.350
9. PYTH-EUR — ACHETE_MAINTENANT — rank 7.806 — opportunité 8.571 — entrée 6.800 — trend 8.850
10. ADA-EUR — ACHETE_MAINTENANT — rank 7.692 — opportunité 8.073 — entrée 7.250 — trend 8.200
11. FET-EUR — ACHETE_MAINTENANT — rank 7.607 — opportunité 8.158 — entrée 7.150 — trend 8.550
12. PENGU-EUR — ACHETE_MAINTENANT — rank 7.399 — opportunité 8.987 — entrée 6.900 — trend 7.000
13. SYRUP-EUR — ACHETE_MAINTENANT — rank 6.066 — opportunité 8.000 — entrée 6.850 — trend 5.700

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.716
2. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.278
3. CFG-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.231

## Accélération indépendante

- SEI-EUR — CONFIRMED_ACCELERATION — score 7.426/10 — DETECTED_BUT_TOO_LATE
- HFT-EUR — CONFIRMED_ACCELERATION — score 7.279/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRUST-EUR — CONFIRMED_ACCELERATION — score 6.646/10 — DETECTED_BUT_TOO_LATE
- PHA-EUR — BUILDING_ACCELERATION — score 6.325/10 — DETECTED_BUT_TOO_LATE
- SKY-EUR — BUILDING_ACCELERATION — score 6.031/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IRYS-EUR — BUILDING_ACCELERATION — score 6.007/10 — DETECTED_BUT_TOO_LATE
- XDC-EUR — BUILDING_ACCELERATION — score 5.612/10 — DETECTED_BUT_TOO_LATE
- MAV-EUR — BUILDING_ACCELERATION — score 5.552/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EIGEN-EUR — BUILDING_ACCELERATION — score 5.544/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PENDLE-EUR — BUILDING_ACCELERATION — score 5.534/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EIGEN-EUR — ACTIVE_NOW — score mémoire 8.086/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PENGU-EUR — ACTIVE_NOW — score mémoire 7.399/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- DGB-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.716/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QNT-EUR — MEMORY_24H — score mémoire 8.429/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 8.278/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CFG-EUR — ACTIVE_NOW — score mémoire 8.231/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.192/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +88.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +45.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRT-EUR +30.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INX-EUR +29.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- W-EUR +19.97% — DETECTED_EARLY — couche NONE — action NONE
- TREAD-EUR +19.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUMP-EUR +17.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +16.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IMX-EUR +15.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- JASMY-EUR +15.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
