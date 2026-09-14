# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T20:34:04.539892+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.907 | entrée 7.250 | trend 8.150 | rang 7.508
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.508
2. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.481
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.303

## Accélération indépendante

- USELESS-EUR — BUILDING_ACCELERATION — score 5.845/10 — DETECTED_BUT_TOO_LATE
- ETH-EUR — BUILDING_ACCELERATION — score 5.711/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- NPC-EUR — BUILDING_ACCELERATION — score 5.312/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- ENA-EUR — BUILDING_ACCELERATION — score 5.122/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 8.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.123/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.013/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.968/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.966/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.830/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.810/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.803/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.753/10 — sources V4 — WATCH_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 7.696/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CNPY-EUR +52.77% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +42.45% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +24.42% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +17.43% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +15.46% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +12.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RED-EUR +10.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +10.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PENDLE-EUR +10.23% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- T-EUR +9.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
