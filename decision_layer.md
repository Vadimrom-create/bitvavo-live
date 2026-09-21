# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T02:12:47.057941+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XPL-EUR | action ACHETE_MAINTENANT | opportunité 7.869 | entrée 7.200 | trend 4.500 | rang 5.995
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MERL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.124 | entrée 6.050 | trend 8.650 | rang 7.817
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARX-EUR | action LATENT_ACCELERATOR | opportunité 7.531 | entrée 5.000 | trend 8.900 | rang 7.479
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : APT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.048 | entrée 6.550 | trend 8.400 | rang 8.212
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. APT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.212
2. XTZ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.064
3. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.977

## Accélération indépendante

- PTB-EUR — CONFIRMED_ACCELERATION — score 8.661/10 — DETECTED_BUT_TOO_LATE
- WIN-EUR — CONFIRMED_ACCELERATION — score 7.815/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- C-EUR — BUILDING_ACCELERATION — score 6.211/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XPL-EUR — ACTIVE_NOW — score mémoire 5.995/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- PTB-EUR — ACTIVE_NOW — score mémoire 8.661/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LSK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.376/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- APT-EUR — ACTIVE_NOW — score mémoire 8.212/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.113/10 — sources ACCELERATION — MEMORY_ONLY
- XTZ-EUR — ACTIVE_NOW — score mémoire 8.064/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.977/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PTB-EUR +75.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +35.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +27.27% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +23.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +23.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +19.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VVV-EUR +17.17% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- NEAR-EUR +15.42% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- S-EUR +14.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +14.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
