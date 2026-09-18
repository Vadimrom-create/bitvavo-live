# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T11:46:22.004864+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : INJ-EUR | action LATENT_ACCELERATOR | opportunité 7.467 | entrée 5.150 | trend 8.300 | rang 6.299
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LSK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.370 | entrée 6.750 | trend 8.400 | rang 7.160
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.160
2. SYRUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.851
3. INJ-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.299

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 8.412/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- CNPY-EUR — BUILDING_ACCELERATION — score 4.752/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LSK-EUR — ACTIVE_NOW — score mémoire 8.412/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CATI-EUR — ACTIVE_NOW — score mémoire 8.176/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.027/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 8.016/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.971/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.967/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 7.912/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.782/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.782/10 — sources V4 — WATCH_ONLY
- ARB-EUR — MEMORY_24H — score mémoire 7.749/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- G-EUR +103.02% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +41.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +29.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DRIFT-EUR +25.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +24.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +24.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STRK-EUR +19.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +19.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RAY-EUR +18.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +17.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
