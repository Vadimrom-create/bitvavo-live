# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T05:26:02.490496+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : VTHO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.420 | entrée 6.050 | trend 9.200 | rang 8.120
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.399 | entrée 6.900 | trend 7.650 | rang 7.184
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.120
2. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.184

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LSK-EUR — MEMORY_24H — score mémoire 9.125/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.310/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.164/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.139/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.120/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 8.116/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 8.060/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.833/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.792/10 — sources V4 — WATCH_ONLY
- CVC-EUR — ACTIVE_NOW — score mémoire 7.734/10 — sources ACCELERATION, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +35.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +28.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +22.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALIGN-EUR +15.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +13.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +12.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LAPTOP-EUR +11.03% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IOST-EUR +9.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +8.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +8.14% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
