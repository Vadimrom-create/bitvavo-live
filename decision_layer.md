# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T06:57:52.858371+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.426 | entrée 7.500 | trend 7.650 | rang 7.653
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.653
2. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.586
3. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.119

## Accélération indépendante

- SYN-EUR — BUILDING_ACCELERATION — score 5.596/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.717/10 — sources V4 — WATCH_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.374/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ENS-EUR — ACTIVE_NOW — score mémoire 8.212/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.080/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SIGN-EUR — ACTIVE_NOW — score mémoire 8.078/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.064/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.064/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 8.025/10 — sources V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 7.900/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.846/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- G-EUR +58.91% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- DRIFT-EUR +37.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +29.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +28.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +28.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +28.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +27.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +25.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +20.65% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- AGI-EUR +20.65% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
