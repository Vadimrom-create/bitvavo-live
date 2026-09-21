# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T17:45:09.613071+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : IMX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.213 | entrée 5.850 | trend 8.450 | rang 8.198
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : INIT-EUR | action LATENT_ACCELERATOR | opportunité 8.021 | entrée 5.350 | trend 8.750 | rang 7.315
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COW-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.332 | entrée 5.850 | trend 8.900 | rang 7.979
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. IMX-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.198
2. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.979
3. LPT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.931

## Accélération indépendante

- ACE-EUR — CONFIRMED_ACCELERATION — score 7.646/10 — DETECTED_BUT_TOO_LATE
- PUFFER-EUR — CONFIRMED_ACCELERATION — score 7.389/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — CONFIRMED_ACCELERATION — score 6.688/10 — DETECTED_BUT_TOO_LATE
- RPL-EUR — CONFIRMED_ACCELERATION — score 6.527/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INJ-EUR — BUILDING_ACCELERATION — score 6.331/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VTHO-EUR — BUILDING_ACCELERATION — score 5.688/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOG-EUR — BUILDING_ACCELERATION — score 5.487/10 — DETECTED_BUT_TOO_LATE
- ALIGN-EUR — BUILDING_ACCELERATION — score 5.193/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HOME-EUR — BUILDING_ACCELERATION — score 4.817/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- RON-EUR — MEMORY_24H — score mémoire 9.938/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CPOOL-EUR — MEMORY_24H — score mémoire 9.834/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SYN-EUR — MEMORY_24H — score mémoire 9.518/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- THQ-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 9.053/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LUMIA-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION — MEMORY_ONLY
- TRAC-EUR — MEMORY_24H — score mémoire 8.588/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +212.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +137.53% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZETA-EUR +52.77% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- FORM-EUR +41.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +35.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SWELL-EUR +29.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEPE-EUR +23.96% — DETECTED_EARLY — couche NONE — action NONE
- PTB-EUR +22.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +22.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOS-EUR +21.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
