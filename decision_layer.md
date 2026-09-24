# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T07:40:11.784101+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ETC-EUR | action ACHETE_MAINTENANT | opportunité 8.730 | entrée 7.800 | trend 8.400 | rang 8.045
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SKY-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.671 | entrée 6.550 | trend 7.350 | rang 7.563
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CAKE-EUR | action LATENT_ACCELERATOR | opportunité 7.464 | entrée 4.500 | trend 7.800 | rang 6.987
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AKT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.223 | entrée 6.600 | trend 8.350 | rang 8.267
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AKT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.267
2. ETC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.045
3. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.723

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 9.471/10 — DETECTED_BUT_TOO_LATE
- CVC-EUR — CONFIRMED_ACCELERATION — score 7.430/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SPX-EUR — BUILDING_ACCELERATION — score 6.444/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOS-EUR — BUILDING_ACCELERATION — score 6.243/10 — DETECTED_BUT_TOO_LATE
- ARPA-EUR — BUILDING_ACCELERATION — score 5.757/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- COMP-EUR — BUILDING_ACCELERATION — score 5.665/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KITE-EUR — BUILDING_ACCELERATION — score 5.545/10 — DETECTED_BUT_TOO_LATE
- MORPHO-EUR — BUILDING_ACCELERATION — score 5.397/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDEN-EUR — BUILDING_ACCELERATION — score 5.276/10 — DETECTED_BUT_TOO_LATE
- HYPE-EUR — BUILDING_ACCELERATION — score 5.144/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LSK-EUR — ACTIVE_NOW — score mémoire 9.471/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CELR-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 8.917/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 8.660/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TRAC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- C98-EUR — MEMORY_24H — score mémoire 8.347/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.307/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AKT-EUR — ACTIVE_NOW — score mémoire 8.267/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NOM-EUR +55.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +37.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +19.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RAY-EUR +19.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IMU-EUR +12.09% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOSO-EUR +10.65% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- CELR-EUR +10.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CVC-EUR +9.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +8.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +8.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
