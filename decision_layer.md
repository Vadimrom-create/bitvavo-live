# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T17:26:45.335405+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : WLD-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.624 | entrée 6.500 | trend 8.150 | rang 7.204
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DOT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.610 | entrée 6.550 | trend 8.300 | rang 7.447
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.447
2. WLD-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.204
3. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.096

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.611/10 — sources V4 — WATCH_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.008/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.981/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.918/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.888/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- BAT-EUR — ACTIVE_NOW — score mémoire 7.882/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.854/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.780/10 — sources V4 — DETECTED_BUT_TOO_LATE
- NPC-EUR — ACTIVE_NOW — score mémoire 7.759/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +94.67% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +57.42% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +48.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +33.02% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +30.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +28.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +25.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +25.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- A-EUR +24.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +18.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
