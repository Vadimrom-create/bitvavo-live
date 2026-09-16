# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T15:34:56.151177+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.605 | entrée 6.100 | trend 8.650 | rang 7.584
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.584
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.824

## Accélération indépendante

- HEI-EUR — CONFIRMED_ACCELERATION — score 9.941/10 — DETECTED_BUT_TOO_LATE
- SYN-EUR — CONFIRMED_ACCELERATION — score 7.850/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- HEI-EUR — ACTIVE_NOW — score mémoire 9.941/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- SIGN-EUR — MEMORY_24H — score mémoire 8.099/10 — sources V4 — MEMORY_ONLY
- ETHFI-EUR — MEMORY_24H — score mémoire 7.895/10 — sources V4 — MEMORY_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.853/10 — sources V4 — WATCH_ONLY
- SYN-EUR — ACTIVE_NOW — score mémoire 7.850/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.821/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZORA-EUR — MEMORY_24H — score mémoire 7.801/10 — sources V4 — MEMORY_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.798/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.765/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.699/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- SYN-EUR +134.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +56.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HEI-EUR +28.84% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FOLD-EUR +16.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IOST-EUR +11.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +11.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +11.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +10.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOSO-EUR +9.60% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SOMI-EUR +6.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
