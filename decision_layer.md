# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T14:01:17.590164+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NPC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.768 | entrée 6.400 | trend 7.750 | rang 7.191
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NPC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.191
2. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.177

## Accélération indépendante

- SAGA-EUR — BUILDING_ACCELERATION — score 4.801/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UNI-EUR — MEMORY_24H — score mémoire 7.931/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.916/10 — sources V4 — WATCH_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.890/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.875/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.710/10 — sources V4 — WATCH_ONLY
- PROM-EUR — ACTIVE_NOW — score mémoire 7.708/10 — sources V4 — WATCH_ONLY
- TIA-EUR — MEMORY_24H — score mémoire 7.702/10 — sources V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.683/10 — sources V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.635/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CNPY-EUR +33.71% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ALIGN-EUR +29.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUFFER-EUR +22.20% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +16.79% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- GLMR-EUR +15.77% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ASTR-EUR +14.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +12.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CROSS-EUR +11.72% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +7.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INIT-EUR +6.52% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
