# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T20:25:13.882920+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SOL-EUR | action ACHETE_MAINTENANT | opportunité 9.296 | entrée 8.050 | trend 8.200 | rang 8.335
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MERL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.980 | entrée 6.000 | trend 8.900 | rang 7.833
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COW-EUR | action LATENT_ACCELERATOR | opportunité 8.012 | entrée 5.200 | trend 8.900 | rang 7.729
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RENDER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.260 | entrée 7.950 | trend 8.100 | rang 8.155
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.335
2. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.155
3. VET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.103

## Accélération indépendante

- GRASS-EUR — CONFIRMED_ACCELERATION — score 9.531/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — CONFIRMED_ACCELERATION — score 9.205/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — CONFIRMED_ACCELERATION — score 8.767/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — BUILDING_ACCELERATION — score 6.496/10 — DETECTED_BUT_TOO_LATE
- LRC-EUR — BUILDING_ACCELERATION — score 6.202/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JASMY-EUR — BUILDING_ACCELERATION — score 5.802/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — BUILDING_ACCELERATION — score 5.653/10 — DETECTED_BUT_TOO_LATE
- IKA-EUR — BUILDING_ACCELERATION — score 5.423/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CRO-EUR — BUILDING_ACCELERATION — score 5.199/10 — DETECTED_BUT_TOO_LATE
- VELO-EUR — BUILDING_ACCELERATION — score 5.032/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.103/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- RON-EUR — MEMORY_24H — score mémoire 9.938/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 9.534/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GRASS-EUR — ACTIVE_NOW — score mémoire 9.531/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TAI-EUR — ACTIVE_NOW — score mémoire 9.205/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ZKJ-EUR — MEMORY_24H — score mémoire 9.182/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- THQ-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BTT-EUR — ACTIVE_NOW — score mémoire 8.767/10 — sources ACCELERATION — WATCH_ONLY
- LUMIA-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +125.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +107.31% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZETA-EUR +56.43% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- AIOZ-EUR +39.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +39.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +34.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +32.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SWELL-EUR +25.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +25.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +24.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
