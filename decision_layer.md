# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T14:00:15.423284+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SOL-EUR | action ACHETE_MAINTENANT | opportunité 8.849 | entrée 7.950 | trend 7.950 | rang 8.006
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : WAL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.742 | entrée 6.650 | trend 8.650 | rang 7.308
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COW-EUR | action LATENT_ACCELERATOR | opportunité 8.652 | entrée 5.400 | trend 9.200 | rang 8.180
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GRASS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.306 | entrée 7.150 | trend 8.450 | rang 8.350
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. GRASS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.350
2. COW-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 8.180
3. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.018

## Accélération indépendante

- FET-EUR — CONFIRMED_ACCELERATION — score 8.768/10 — DETECTED_BUT_TOO_LATE
- WIF-EUR — CONFIRMED_ACCELERATION — score 7.257/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — CONFIRMED_ACCELERATION — score 7.080/10 — DETECTED_BUT_TOO_LATE
- CELR-EUR — CONFIRMED_ACCELERATION — score 6.750/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VERONA-EUR — CONFIRMED_ACCELERATION — score 6.742/10 — DETECTED_BUT_TOO_LATE
- AGLD-EUR — BUILDING_ACCELERATION — score 6.267/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MLN-EUR — BUILDING_ACCELERATION — score 5.690/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INJ-EUR — BUILDING_ACCELERATION — score 5.548/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ASTER-EUR — BUILDING_ACCELERATION — score 5.247/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MET-EUR — BUILDING_ACCELERATION — score 5.141/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- EDGE-EUR — MEMORY_24H — score mémoire 9.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.488/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 9.465/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 9.053/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.768/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ARB-EUR — MEMORY_24H — score mémoire 8.746/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.457/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +64.93% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +61.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +45.75% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AIOZ-EUR +39.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +30.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +29.94% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SEI-EUR +28.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PROVE-EUR +28.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +27.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUI-EUR +26.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
