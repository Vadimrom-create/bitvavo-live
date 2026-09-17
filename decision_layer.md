# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T17:45:38.277899+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.947 | entrée 7.200 | trend 7.650 | rang 7.047
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.047
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.465

## Accélération indépendante

- SYN-EUR — CONFIRMED_ACCELERATION — score 7.031/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 5.420/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 9.527/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.239/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.211/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.130/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.086/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.985/10 — sources V4 — WATCH_ONLY
- ENS-EUR — ACTIVE_NOW — score mémoire 7.970/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.961/10 — sources V4 — WATCH_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 7.862/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.855/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +94.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +40.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +34.19% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- KSM-EUR +28.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +25.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +24.99% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NEAR-EUR +23.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +21.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +19.40% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- GALA-EUR +16.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
