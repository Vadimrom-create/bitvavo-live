# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T00:32:38.505542+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.373 | entrée 5.750 | trend 9.200 | rang 8.094
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.094

## Accélération indépendante

- VTHO-EUR — BUILDING_ACCELERATION — score 6.330/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 8.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.094/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.933/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.758/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.720/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.648/10 — sources V4 — WATCH_ONLY
- COTI-EUR — ACTIVE_NOW — score mémoire 7.626/10 — sources V4 — DETECTED_BUT_TOO_LATE
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.607/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.533/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WIF-EUR — MEMORY_24H — score mémoire 7.528/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CAP-EUR +36.67% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +33.30% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +29.41% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +23.86% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- T-EUR +18.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PENDLE-EUR +12.86% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- STRAX-EUR +10.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUFFER-EUR +10.72% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- QKC-EUR +9.67% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SENT-EUR +9.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
