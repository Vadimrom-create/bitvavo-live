# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T20:52:04.596796+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.537 | entrée 6.900 | trend 8.100 | rang 6.699
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.699

## Accélération indépendante

- DRIFT-EUR — CONFIRMED_ACCELERATION — score 8.926/10 — DETECTED_BUT_TOO_LATE
- AVA-EUR — BUILDING_ACCELERATION — score 5.981/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 9.527/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DRIFT-EUR — ACTIVE_NOW — score mémoire 8.926/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 8.375/10 — sources V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.259/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 8.182/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.931/10 — sources V4 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.917/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.907/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.895/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.890/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +86.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +42.18% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CROSS-EUR +40.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +33.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +32.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +29.21% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- UNI-EUR +18.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +18.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DRIFT-EUR +17.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QUID-EUR +17.48% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
