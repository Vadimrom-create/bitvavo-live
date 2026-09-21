# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T18:06:10.138704+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : ONDO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.579 | entrée 6.700 | trend 8.100 | rang 7.446
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : WAL-EUR | action LATENT_ACCELERATOR | opportunité 8.254 | entrée 5.650 | trend 9.200 | rang 7.965
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LPT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.293 | entrée 7.050 | trend 8.750 | rang 7.877
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WAL-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.965
2. LPT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.877
3. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.843

## Accélération indépendante

- PUFFER-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- U-EUR — CONFIRMED_ACCELERATION — score 9.648/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — CONFIRMED_ACCELERATION — score 7.211/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XMN-EUR — BUILDING_ACCELERATION — score 6.436/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAGA-EUR — BUILDING_ACCELERATION — score 5.885/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — BUILDING_ACCELERATION — score 5.689/10 — DETECTED_BUT_TOO_LATE
- ARX-EUR — BUILDING_ACCELERATION — score 4.850/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PUFFER-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- RON-EUR — MEMORY_24H — score mémoire 9.938/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CPOOL-EUR — MEMORY_24H — score mémoire 9.834/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — ACTIVE_NOW — score mémoire 9.648/10 — sources ACCELERATION, V4 — WATCH_ONLY
- THQ-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 9.053/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LUMIA-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION — MEMORY_ONLY
- TRAC-EUR — MEMORY_24H — score mémoire 8.588/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +176.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +126.11% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZETA-EUR +55.96% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- FORM-EUR +40.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +38.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUFFER-EUR +29.55% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- SWELL-EUR +24.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEPE-EUR +23.19% — DETECTED_EARLY — couche NONE — action NONE
- AIOZ-EUR +22.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOS-EUR +18.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
