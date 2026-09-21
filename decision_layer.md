# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T22:10:01.323581+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 8.321 | entrée 7.400 | trend 8.700 | rang 7.966
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BIGTIME-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.667 | entrée 6.350 | trend 8.450 | rang 7.548
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MERL-EUR | action LATENT_ACCELERATOR | opportunité 8.021 | entrée 5.750 | trend 8.900 | rang 7.819
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.359 | entrée 6.300 | trend 9.200 | rang 8.142
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.142
2. THE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.047
3. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.967

## Accélération indépendante

- AIOZ-EUR — CONFIRMED_ACCELERATION — score 9.833/10 — DETECTED_BUT_TOO_LATE
- DGB-EUR — CONFIRMED_ACCELERATION — score 8.732/10 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — BUILDING_ACCELERATION — score 6.494/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — BUILDING_ACCELERATION — score 6.449/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — BUILDING_ACCELERATION — score 6.340/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 5.074/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AIOZ-EUR — ACTIVE_NOW — score mémoire 9.833/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — MEMORY_24H — score mémoire 9.738/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 8.767/10 — sources ACCELERATION — MEMORY_ONLY
- DGB-EUR — ACTIVE_NOW — score mémoire 8.732/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- LUMIA-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SFP-EUR — MEMORY_24H — score mémoire 8.323/10 — sources ACCELERATION — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.142/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- THE-EUR — ACTIVE_NOW — score mémoire 8.047/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.967/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +92.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +84.57% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZETA-EUR +51.51% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- AIOZ-EUR +47.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +39.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +34.78% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +34.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SWELL-EUR +32.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUFFER-EUR +23.79% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PEPE-EUR +22.49% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
