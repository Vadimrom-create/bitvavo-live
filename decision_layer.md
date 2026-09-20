# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T09:04:03.612164+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.162 | entrée 5.900 | trend 8.300 | rang 7.415
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.415
2. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.415
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.209

## Accélération indépendante

- CNPY-EUR — BUILDING_ACCELERATION — score 5.142/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- STRK-EUR — BUILDING_ACCELERATION — score 4.762/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XTZ-EUR — ACTIVE_NOW — score mémoire 8.095/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.024/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.980/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- APT-EUR — ACTIVE_NOW — score mémoire 7.888/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 7.751/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- BIGTIME-EUR — ACTIVE_NOW — score mémoire 7.730/10 — sources V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.723/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.701/10 — sources V4 — WATCH_ONLY
- PROVE-EUR — MEMORY_24H — score mémoire 7.609/10 — sources V4 — MEMORY_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.602/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +69.98% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +22.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +17.80% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKL-EUR +16.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +10.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- JTO-EUR +10.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STX-EUR +10.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOLV-EUR +10.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +9.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZAMA-EUR +9.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
