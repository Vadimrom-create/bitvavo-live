# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T22:28:25.284464+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DOT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.350 | entrée 5.950 | trend 8.300 | rang 7.312
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.312
2. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.162

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 9.527/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.992/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.924/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.905/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.832/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.734/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.706/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.690/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.673/10 — sources V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.626/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +80.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +47.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +44.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +43.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +37.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +26.70% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- UNI-EUR +18.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DRIFT-EUR +17.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +16.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +16.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
