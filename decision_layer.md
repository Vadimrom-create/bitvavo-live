# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T17:58:38.456761+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.724 | entrée 6.500 | trend 8.100 | rang 6.650
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.650
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.263

## Accélération indépendante

- ARB-EUR — CONFIRMED_ACCELERATION — score 8.911/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — CONFIRMED_ACCELERATION — score 8.175/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 9.527/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARB-EUR — ACTIVE_NOW — score mémoire 8.911/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- YB-EUR — ACTIVE_NOW — score mémoire 8.225/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.210/10 — sources V4 — WATCH_ONLY
- TREAD-EUR — ACTIVE_NOW — score mémoire 8.175/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 8.146/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.109/10 — sources V4 — WATCH_ONLY
- TAO-EUR — ACTIVE_NOW — score mémoire 8.054/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.994/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.946/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +92.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +40.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +31.29% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- KSM-EUR +26.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +25.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +25.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +23.94% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FOLD-EUR +21.70% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PEAQ-EUR +20.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +18.19% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
