# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T13:54:53.093514+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HBAR-EUR | action ACHETE_MAINTENANT | opportunité 8.622 | entrée 7.000 | trend 7.150 | rang 7.298
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.384 | entrée 5.100 | trend 8.700 | rang 7.381
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.381
2. HBAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.298
3. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.214

## Accélération indépendante

- EPIC-EUR — CONFIRMED_ACCELERATION — score 9.093/10 — DETECTED_BUT_TOO_LATE
- HBAR-EUR — BUILDING_ACCELERATION — score 6.090/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- G-EUR — BUILDING_ACCELERATION — score 5.532/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- HBAR-EUR — ACTIVE_NOW — score mémoire 7.298/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EPIC-EUR — ACTIVE_NOW — score mémoire 9.093/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.404/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.879/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.879/10 — sources V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.795/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.760/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- STX-EUR — ACTIVE_NOW — score mémoire 7.726/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- BIGTIME-EUR — MEMORY_24H — score mémoire 7.662/10 — sources V4 — MEMORY_ONLY
- ENSO-EUR — MEMORY_24H — score mémoire 7.642/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CELR-EUR +71.39% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +20.98% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVAX-EUR +14.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZAMA-EUR +13.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +12.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +10.71% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +10.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +8.63% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +8.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SHELL-EUR +7.93% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
