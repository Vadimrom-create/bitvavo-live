# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T13:50:02.989835+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 9.199 | entrée 7.500 | trend 7.900 | rang 8.063
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : EIGEN-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.798 | entrée 6.250 | trend 7.300 | rang 6.832
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 7.643 | entrée 4.500 | trend 8.950 | rang 7.518
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LTC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.745 | entrée 7.450 | trend 9.200 | rang 8.219
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.219
2. VET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.063
3. BONK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.915

## Accélération indépendante

- LAPTOP-EUR — CONFIRMED_ACCELERATION — score 8.780/10 — DETECTED_BUT_TOO_LATE
- REQ-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QNT-EUR — CONFIRMED_ACCELERATION — score 8.209/10 — DETECTED_BUT_TOO_LATE
- NOM-EUR — CONFIRMED_ACCELERATION — score 8.023/10 — DETECTED_BUT_TOO_LATE
- ACT-EUR — CONFIRMED_ACCELERATION — score 7.986/10 — DETECTED_BUT_TOO_LATE
- LSK-EUR — CONFIRMED_ACCELERATION — score 7.665/10 — DETECTED_BUT_TOO_LATE
- ID-EUR — CONFIRMED_ACCELERATION — score 6.719/10 — DETECTED_BUT_TOO_LATE
- DIA-EUR — BUILDING_ACCELERATION — score 6.318/10 — DETECTED_BUT_TOO_LATE
- MEME-EUR — BUILDING_ACCELERATION — score 6.237/10 — DETECTED_BUT_TOO_LATE
- AZTEC-EUR — BUILDING_ACCELERATION — score 6.214/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- OP-EUR — ACTIVE_NOW — score mémoire 7.705/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- APT-EUR — ACTIVE_NOW — score mémoire 7.358/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.456/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 9.446/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LUNA2-EUR — MEMORY_24H — score mémoire 8.989/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LAPTOP-EUR — ACTIVE_NOW — score mémoire 8.780/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- REZ-EUR — MEMORY_24H — score mémoire 8.510/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NOM-EUR +43.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +32.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +25.67% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARX-EUR +14.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ONDO-EUR +13.20% — DETECTED_EARLY — couche NONE — action NONE
- MORPHO-EUR +12.20% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- INIT-EUR +10.93% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- LTC-EUR +10.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +7.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOSO-EUR +7.47% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
