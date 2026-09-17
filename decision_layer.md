# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T23:12:35.947958+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.323 | entrée 7.200 | trend 7.650 | rang 7.550
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.550
2. PHA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.195
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.751

## Accélération indépendante

- TREAD-EUR — BUILDING_ACCELERATION — score 5.500/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 9.527/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DRIFT-EUR — MEMORY_24H — score mémoire 8.695/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 8.009/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.961/10 — sources V4 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.960/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.958/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.923/10 — sources V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.911/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.899/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.865/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +66.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +52.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +45.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +44.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +35.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +26.55% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- DRIFT-EUR +24.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +20.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- UNI-EUR +19.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +18.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
