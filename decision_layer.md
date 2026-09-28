# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T00:53:49.279139+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 9.239 | entrée 7.600 | trend 9.200 | rang 8.691
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.257 | entrée 5.800 | trend 8.950 | rang 7.864
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IO-EUR | action LATENT_ACCELERATOR | opportunité 8.589 | entrée 5.700 | trend 8.450 | rang 7.841
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SUI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.445 | entrée 7.850 | trend 8.850 | rang 8.330
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. RENDER-EUR — ACHETE_MAINTENANT — rank 8.691 — opportunité 9.239 — entrée 7.600 — trend 9.200
2. EIGEN-EUR — ACHETE_MAINTENANT — rank 8.459 — opportunité 9.272 — entrée 7.350 — trend 8.900
3. DOT-EUR — ACHETE_MAINTENANT — rank 8.090 — opportunité 8.203 — entrée 7.150 — trend 8.950
4. HBAR-EUR — ACHETE_MAINTENANT — rank 7.942 — opportunité 8.787 — entrée 7.650 — trend 7.700
5. GMT-EUR — ACHETE_MAINTENANT — rank 7.938 — opportunité 8.194 — entrée 6.900 — trend 8.750
6. LINK-EUR — ACHETE_MAINTENANT — rank 7.931 — opportunité 8.134 — entrée 6.900 — trend 8.700
7. FET-EUR — ACHETE_MAINTENANT — rank 7.771 — opportunité 8.045 — entrée 7.800 — trend 8.550
8. PYTH-EUR — ACHETE_MAINTENANT — rank 7.743 — opportunité 8.260 — entrée 7.050 — trend 8.850
9. ADA-EUR — ACHETE_MAINTENANT — rank 7.687 — opportunité 7.877 — entrée 7.450 — trend 8.200
10. PENGU-EUR — ACHETE_MAINTENANT — rank 7.162 — opportunité 8.049 — entrée 7.200 — trend 7.000
11. DOGE-EUR — ACHETE_MAINTENANT — rank 7.098 — opportunité 8.603 — entrée 7.400 — trend 6.100

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.691
2. EIGEN-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.459
3. SUI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.330

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 9.062/10 — DETECTED_BUT_TOO_LATE
- GRASS-EUR — CONFIRMED_ACCELERATION — score 7.905/10 — DETECTED_BUT_TOO_LATE
- TURBO-EUR — CONFIRMED_ACCELERATION — score 7.669/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BOME-EUR — BUILDING_ACCELERATION — score 6.075/10 — DETECTED_BUT_TOO_LATE
- MEME-EUR — BUILDING_ACCELERATION — score 5.808/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IRYS-EUR — BUILDING_ACCELERATION — score 5.743/10 — DETECTED_BUT_TOO_LATE
- CRO-EUR — BUILDING_ACCELERATION — score 5.662/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRB-EUR — BUILDING_ACCELERATION — score 5.418/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BIRB-EUR — BUILDING_ACCELERATION — score 5.354/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IO-EUR — BUILDING_ACCELERATION — score 5.303/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EIGEN-EUR — ACTIVE_NOW — score mémoire 8.459/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PENGU-EUR — ACTIVE_NOW — score mémoire 7.162/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- DGB-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — ACTIVE_NOW — score mémoire 9.062/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.691/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QNT-EUR — MEMORY_24H — score mémoire 8.429/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SUI-EUR — ACTIVE_NOW — score mémoire 8.330/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +74.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +41.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INX-EUR +29.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRT-EUR +27.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +27.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUMP-EUR +19.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +19.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IRYS-EUR +19.55% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- IMX-EUR +15.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- W-EUR +14.73% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
