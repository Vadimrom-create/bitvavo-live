# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T10:42:43.731077+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : BNB-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.674 | entrée 6.600 | trend 7.500 | rang 7.662
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.492 | entrée 6.250 | trend 9.200 | rang 7.842
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.842
2. BNB-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.662
3. SYRUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.992

## Accélération indépendante

- SYRUP-EUR — CONFIRMED_ACCELERATION — score 7.683/10 — DETECTED_BUT_TOO_LATE
- AVA-EUR — BUILDING_ACCELERATION — score 4.847/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ENSO-EUR — MEMORY_24H — score mémoire 8.974/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.180/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.177/10 — sources V4 — WATCH_ONLY
- ENS-EUR — ACTIVE_NOW — score mémoire 8.133/10 — sources V4 — DETECTED_BUT_TOO_LATE
- GRT-EUR — ACTIVE_NOW — score mémoire 8.049/10 — sources V4 — DETECTED_BUT_TOO_LATE
- SOMI-EUR — ACTIVE_NOW — score mémoire 8.024/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.018/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.842/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.802/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.798/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +79.32% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +36.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +34.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DRIFT-EUR +31.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +28.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +27.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +26.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STRK-EUR +23.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +22.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +21.35% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
