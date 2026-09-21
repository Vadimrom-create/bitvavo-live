# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T17:51:49.444235+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : SUPER-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.078 | entrée 5.800 | trend 8.950 | rang 7.696
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COW-EUR | action LATENT_ACCELERATOR | opportunité 7.958 | entrée 5.350 | trend 8.900 | rang 7.747
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LPT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.553 | entrée 7.150 | trend 8.750 | rang 8.056
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LPT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.056
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.814
3. JUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.810

## Accélération indépendante

- ACE-EUR — CONFIRMED_ACCELERATION — score 6.950/10 — DETECTED_BUT_TOO_LATE
- INJ-EUR — CONFIRMED_ACCELERATION — score 6.825/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUFFER-EUR — BUILDING_ACCELERATION — score 5.998/10 — DETECTED_BUT_TOO_LATE
- O-EUR — BUILDING_ACCELERATION — score 5.619/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAGA-EUR — BUILDING_ACCELERATION — score 5.617/10 — DETECTED_BUT_TOO_LATE
- RPL-EUR — BUILDING_ACCELERATION — score 4.932/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HOME-EUR — BUILDING_ACCELERATION — score 4.905/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- RON-EUR — MEMORY_24H — score mémoire 9.938/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CPOOL-EUR — MEMORY_24H — score mémoire 9.834/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- THQ-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 9.053/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LUMIA-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION — MEMORY_ONLY
- TRAC-EUR — MEMORY_24H — score mémoire 8.588/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FARTCOIN-EUR — MEMORY_24H — score mémoire 8.408/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +197.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +123.01% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZETA-EUR +52.39% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- FORM-EUR +38.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +35.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SWELL-EUR +27.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +22.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +22.25% — DETECTED_EARLY — couche NONE — action NONE
- NOS-EUR +21.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PONKE-EUR +17.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
