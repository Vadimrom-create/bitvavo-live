# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T21:53:24.771332+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : ORCA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.691 | entrée 6.650 | trend 9.000 | rang 7.816
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MOVR-EUR | action LATENT_ACCELERATOR | opportunité 8.716 | entrée 5.750 | trend 8.950 | rang 8.076
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PYTH-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.749 | entrée 7.050 | trend 9.200 | rang 8.281
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.281
2. TAIKO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.254
3. MOVR-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 8.076

## Accélération indépendante

- C-EUR — BUILDING_ACCELERATION — score 4.945/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLMR-EUR — BUILDING_ACCELERATION — score 4.868/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.667/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.281/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TAIKO-EUR — ACTIVE_NOW — score mémoire 8.254/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.111/10 — sources ACCELERATION — MEMORY_ONLY
- MOVR-EUR — ACTIVE_NOW — score mémoire 8.076/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TIA-EUR — ACTIVE_NOW — score mémoire 8.033/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 7.981/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MANA-EUR — ACTIVE_NOW — score mémoire 7.968/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 7.948/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PHA-EUR +74.26% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +26.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +21.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AERO-EUR +20.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +16.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +16.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +16.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +15.69% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DEEP-EUR +15.50% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- WIN-EUR +14.87% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
