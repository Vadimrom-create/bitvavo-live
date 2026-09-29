# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T07:23:51.308276+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 8.507 | entrée 7.150 | trend 8.900 | rang 8.056
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : PLUME-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.346 | entrée 6.700 | trend 7.350 | rang 7.304
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : C-EUR | action LATENT_ACCELERATOR | opportunité 7.676 | entrée 4.500 | trend 8.250 | rang 7.188
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MIOTA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.276 | entrée 6.950 | trend 8.900 | rang 7.899
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. LINK-EUR — ACHETE_MAINTENANT — rank 8.056 — opportunité 8.507 — entrée 7.150 — trend 8.900
2. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 7.984 — opportunité 8.886 — entrée 7.450 — trend 8.100
3. ONDO-EUR — ACHETE_MAINTENANT — rank 7.801 — opportunité 8.824 — entrée 7.650 — trend 7.750
4. PEAQ-EUR — ACHETE_MAINTENANT — rank 7.674 — opportunité 9.070 — entrée 7.100 — trend 7.500
5. WLD-EUR — ACHETE_MAINTENANT — rank 7.617 — opportunité 9.080 — entrée 7.800 — trend 7.300
6. FET-EUR — ACHETE_MAINTENANT — rank 7.500 — opportunité 8.595 — entrée 7.200 — trend 7.550
7. TAO-EUR — ACHETE_MAINTENANT — rank 7.077 — opportunité 8.767 — entrée 7.700 — trend 5.900
8. ADA-EUR — ACHETE_MAINTENANT — rank 6.970 — opportunité 8.369 — entrée 7.700 — trend 5.950
9. BNB-EUR — ACHETE_MAINTENANT — rank 6.533 — opportunité 8.405 — entrée 7.200 — trend 4.650
10. AVAX-EUR — ACHETE_MAINTENANT — rank 6.377 — opportunité 7.821 — entrée 6.950 — trend 6.100

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.056
2. VIRTUAL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.984
3. MIOTA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.899

## Accélération indépendante

- PUFFER-EUR — CONFIRMED_ACCELERATION — score 9.732/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QUID-EUR — CONFIRMED_ACCELERATION — score 9.062/10 — DETECTED_BUT_TOO_LATE
- AGI-EUR — CONFIRMED_ACCELERATION — score 7.529/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARX-EUR — CONFIRMED_ACCELERATION — score 7.460/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — CONFIRMED_ACCELERATION — score 7.161/10 — DETECTED_BUT_TOO_LATE
- VELO-EUR — CONFIRMED_ACCELERATION — score 6.906/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WELL-EUR — CONFIRMED_ACCELERATION — score 6.798/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- COW-EUR — CONFIRMED_ACCELERATION — score 6.733/10 — DETECTED_BUT_TOO_LATE
- SSV-EUR — BUILDING_ACCELERATION — score 6.360/10 — DETECTED_BUT_TOO_LATE
- FLUID-EUR — BUILDING_ACCELERATION — score 6.346/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.674/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- WLD-EUR — ACTIVE_NOW — score mémoire 7.617/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PUFFER-EUR — ACTIVE_NOW — score mémoire 9.732/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 9.687/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QUID-EUR — ACTIVE_NOW — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- FUEL-EUR — MEMORY_24H — score mémoire 9.056/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.582/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ETHFI-EUR — MEMORY_24H — score mémoire 8.321/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NMR-EUR +29.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARX-EUR +24.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CRV-EUR +21.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POND-EUR +20.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HBAR-EUR +19.70% — DETECTED_EARLY — couche NONE — action NONE
- 0G-EUR +18.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CELO-EUR +15.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +15.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CVX-EUR +11.72% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- GRASS-EUR +11.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Gestion des positions détenues

Policy : STAGED_10_20_RUNNER_V1
- +10% : prise partielle 35%.
- +20% : seconde prise 35%.
- Runner conservé : 30%.
- Revue coût d'opportunité après 72 h ; sortie seulement avant la première partielle, proche/sous le PRU et avec momentum 15m affaibli.
- Pas de stop serré mécaniquement après une petite hausse ; le stop reste lié à l'invalidation structurelle.

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
