# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T09:51:15.060593+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 7.714 | entrée 7.150 | trend 7.000 | rang 6.979
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ENA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.497 | entrée 6.650 | trend 8.500 | rang 7.399
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.495 | entrée 6.900 | trend 8.300 | rang 7.509
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.509
2. ENA-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.399
3. AVAX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.268

## Accélération indépendante

- CELR-EUR — CONFIRMED_ACCELERATION — score 6.564/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PROVE-EUR — ACTIVE_NOW — score mémoire 8.265/10 — sources V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 8.254/10 — sources V4 — WATCH_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 8.089/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.997/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.976/10 — sources V4 — WATCH_ONLY
- COTI-EUR — MEMORY_24H — score mémoire 7.904/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.832/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.761/10 — sources V4 — WATCH_ONLY
- XTZ-EUR — ACTIVE_NOW — score mémoire 7.692/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- BIGTIME-EUR — MEMORY_24H — score mémoire 7.662/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CELR-EUR +84.06% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +22.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +18.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKL-EUR +14.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- JTO-EUR +12.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOLV-EUR +11.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +11.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +11.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- T-EUR +10.42% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVAX-EUR +9.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
