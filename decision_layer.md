# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T14:04:21.956677+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : UNI-EUR | action ACHETE_MAINTENANT | opportunité 9.180 | entrée 7.600 | trend 7.750 | rang 7.921
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : SIGN-EUR | action LATENT_ACCELERATOR | opportunité 8.085 | entrée 4.500 | trend 8.950 | rang 7.569
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : DRIFT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.144 | entrée 6.850 | trend 8.650 | rang 8.334
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DRIFT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.334
2. ETC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.284
3. UNI-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.921

## Accélération indépendante

- VET-EUR — CONFIRMED_ACCELERATION — score 7.698/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QNT-EUR — CONFIRMED_ACCELERATION — score 7.575/10 — DETECTED_BUT_TOO_LATE
- RON-EUR — CONFIRMED_ACCELERATION — score 7.150/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LTC-EUR — BUILDING_ACCELERATION — score 6.291/10 — DETECTED_BUT_TOO_LATE
- NOS-EUR — BUILDING_ACCELERATION — score 5.812/10 — DETECTED_BUT_TOO_LATE
- IQ-EUR — BUILDING_ACCELERATION — score 5.332/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CTSI-EUR — BUILDING_ACCELERATION — score 5.247/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — BUILDING_ACCELERATION — score 5.183/10 — DETECTED_BUT_TOO_LATE
- LAPTOP-EUR — BUILDING_ACCELERATION — score 5.132/10 — DETECTED_BUT_TOO_LATE
- IMU-EUR — BUILDING_ACCELERATION — score 5.040/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- RENDER-EUR — ACTIVE_NOW — score mémoire 7.746/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.700/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- VET-EUR — ACTIVE_NOW — score mémoire 7.698/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.456/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 9.446/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LUNA2-EUR — MEMORY_24H — score mémoire 8.989/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- REZ-EUR — MEMORY_24H — score mémoire 8.510/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NOM-EUR +44.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +32.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +27.30% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +13.42% — DETECTED_EARLY — couche NONE — action NONE
- LTC-EUR +12.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARX-EUR +12.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MORPHO-EUR +12.61% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- INIT-EUR +12.04% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- IMU-EUR +9.39% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +8.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
