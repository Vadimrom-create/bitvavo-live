# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T11:31:03.814722+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : PUMP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.494 | entrée 6.350 | trend 7.500 | rang 7.010
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.238 | entrée 5.550 | trend 9.200 | rang 7.535
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.535
2. SYRUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.198
3. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.122

## Accélération indépendante

- VTHO-EUR — CONFIRMED_ACCELERATION — score 6.966/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.155/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- KAS-EUR — ACTIVE_NOW — score mémoire 7.943/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.910/10 — sources V4 — WATCH_ONLY
- NEO-EUR — ACTIVE_NOW — score mémoire 7.759/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.755/10 — sources V4 — WATCH_ONLY
- ARB-EUR — MEMORY_24H — score mémoire 7.749/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.729/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.716/10 — sources V4 — WATCH_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.697/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +92.97% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +40.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +27.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARB-EUR +24.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DRIFT-EUR +23.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +22.25% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STRK-EUR +21.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +20.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +18.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +17.79% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
