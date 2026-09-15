# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T13:47:44.797124+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : UNI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.893 | entrée 6.750 | trend 7.750 | rang 7.931
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.931

## Accélération indépendante

- CNPY-EUR — BUILDING_ACCELERATION — score 5.784/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.995/10 — sources V4 — WATCH_ONLY
- UNI-EUR — ACTIVE_NOW — score mémoire 7.931/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.907/10 — sources V4 — WATCH_ONLY
- BNB-EUR — ACTIVE_NOW — score mémoire 7.888/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.883/10 — sources V4 — WATCH_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.741/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.731/10 — sources V4 — WATCH_ONLY
- TIA-EUR — ACTIVE_NOW — score mémoire 7.702/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.586/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CNPY-EUR +34.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ALIGN-EUR +33.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUFFER-EUR +20.13% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- GLMR-EUR +17.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ASTR-EUR +14.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +12.99% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +12.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CROSS-EUR +12.47% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +9.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INIT-EUR +6.52% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
