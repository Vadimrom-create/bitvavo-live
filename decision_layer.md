# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T06:57:20.732234+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.312 | entrée 6.850 | trend 8.950 | rang 8.082
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : APT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.468 | entrée 6.300 | trend 8.450 | rang 7.327
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.122 | entrée 7.150 | trend 8.500 | rang 7.845
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.082
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.845
3. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.434

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 8.067/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AAVE-EUR — ACTIVE_NOW — score mémoire 8.082/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LSK-EUR — ACTIVE_NOW — score mémoire 8.067/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SENT-EUR — ACTIVE_NOW — score mémoire 8.033/10 — sources V4 — WATCH_ONLY
- ARX-EUR — ACTIVE_NOW — score mémoire 7.978/10 — sources V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.946/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.910/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.891/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.891/10 — sources V4 — WATCH_ONLY
- SSV-EUR — MEMORY_24H — score mémoire 7.845/10 — sources V4 — MEMORY_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.845/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- EDGE-EUR +57.46% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +35.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +30.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +25.69% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- INJ-EUR +23.78% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +22.36% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +22.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +21.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +21.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MORPHO-EUR +17.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
