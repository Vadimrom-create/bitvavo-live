# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T08:21:16.231287+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AVAX-EUR | action ACHETE_MAINTENANT | opportunité 8.134 | entrée 7.600 | trend 8.450 | rang 7.786
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : ONDO-EUR | action LATENT_ACCELERATOR | opportunité 7.441 | entrée 4.500 | trend 7.650 | rang 6.957
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.891 | entrée 7.950 | trend 8.500 | rang 7.873
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.873
2. AVAX-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.786
3. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.512

## Accélération indépendante

- ENA-EUR — CONFIRMED_ACCELERATION — score 6.909/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- STRK-EUR — BUILDING_ACCELERATION — score 5.347/10 — DETECTED_BUT_TOO_LATE
- INJ-EUR — BUILDING_ACCELERATION — score 4.778/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AVAX-EUR — ACTIVE_NOW — score mémoire 7.786/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ACH-EUR — ACTIVE_NOW — score mémoire 8.316/10 — sources V4 — DETECTED_BUT_TOO_LATE
- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.282/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.180/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.174/10 — sources V4 — DETECTED_BUT_TOO_LATE
- LSK-EUR — MEMORY_24H — score mémoire 8.067/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.008/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.983/10 — sources V4 — WATCH_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 7.934/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.920/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- EDGE-EUR +50.88% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HEI-EUR +40.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +36.84% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +29.78% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +29.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +25.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +24.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZAMA-EUR +23.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +23.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +18.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
