# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T11:14:29.269026+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : PUMP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.461 | entrée 6.400 | trend 7.500 | rang 7.423
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.187 | entrée 6.700 | trend 9.200 | rang 7.767
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.767
2. SYRUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.574
3. PUMP-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.423

## Accélération indépendante

- ENSO-EUR — BUILDING_ACCELERATION — score 5.194/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- NPC-EUR — ACTIVE_NOW — score mémoire 8.118/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.964/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.932/10 — sources V4 — WATCH_ONLY
- KAS-EUR — MEMORY_24H — score mémoire 7.927/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.816/10 — sources V4 — WATCH_ONLY
- ZRX-EUR — ACTIVE_NOW — score mémoire 7.816/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.767/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.756/10 — sources V4 — WATCH_ONLY
- ARB-EUR — MEMORY_24H — score mémoire 7.749/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PROM-EUR — ACTIVE_NOW — score mémoire 7.734/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +94.15% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +39.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +26.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +25.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DRIFT-EUR +24.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +23.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +23.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +22.04% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +21.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +18.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
