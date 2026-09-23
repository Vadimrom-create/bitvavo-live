# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T22:48:13.194917+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SOL-EUR | action ACHETE_MAINTENANT | opportunité 8.316 | entrée 7.350 | trend 8.100 | rang 7.833
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SLX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.036 | entrée 5.900 | trend 7.350 | rang 7.663
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : FLUX-EUR | action LATENT_ACCELERATOR | opportunité 8.303 | entrée 5.550 | trend 8.850 | rang 7.827
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : DATAIP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.877 | entrée 6.700 | trend 7.850 | rang 7.866
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DATAIP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.866
2. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.833
3. FLUX-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.827

## Accélération indépendante

- ZIG-EUR — CONFIRMED_ACCELERATION — score 8.658/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LSK-EUR — CONFIRMED_ACCELERATION — score 6.761/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.545/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZIG-EUR — ACTIVE_NOW — score mémoire 8.658/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZBCN-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DATAIP-EUR — ACTIVE_NOW — score mémoire 7.866/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOL-EUR — ACTIVE_NOW — score mémoire 7.833/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FLUX-EUR — ACTIVE_NOW — score mémoire 7.827/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- NIL-EUR +47.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CPOOL-EUR +26.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +20.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +19.85% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- RAY-EUR +12.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOM-EUR +12.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +11.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +10.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +10.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOSO-EUR +9.01% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
