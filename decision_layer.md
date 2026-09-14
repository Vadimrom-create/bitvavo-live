# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T11:50:59.964065+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.078 | entrée 5.800 | trend 9.200 | rang 7.964
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.964
2. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.610
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.566

## Accélération indépendante

- CPOOL-EUR — BUILDING_ACCELERATION — score 5.700/10 — DETECTED_BUT_TOO_LATE
- LAPTOP-EUR — BUILDING_ACCELERATION — score 5.073/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- REZ-EUR — BUILDING_ACCELERATION — score 4.786/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AERO-EUR — ACTIVE_NOW — score mémoire 8.207/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.964/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.885/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.787/10 — sources V4 — WATCH_ONLY
- NEO-EUR — MEMORY_24H — score mémoire 7.738/10 — sources V4 — MEMORY_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.725/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.699/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.689/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.631/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.610/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +63.01% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- T-EUR +30.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CVC-EUR +29.90% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FIL-EUR +22.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +22.12% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- REZ-EUR +20.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QKC-EUR +14.38% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- WAXP-EUR +11.88% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NPC-EUR +11.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IQ-EUR +11.12% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
