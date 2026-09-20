# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T04:38:52.483242+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : SKL-EUR | action LATENT_ACCELERATOR | opportunité 8.546 | entrée 4.650 | trend 8.200 | rang 6.873
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.384 | entrée 6.300 | trend 7.950 | rang 7.255
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.255
2. RAY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.178
3. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.950

## Accélération indépendante

- CELR-EUR — CONFIRMED_ACCELERATION — score 7.615/10 — DETECTED_BUT_TOO_LATE
- SKL-EUR — CONFIRMED_ACCELERATION — score 7.553/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- C-EUR — MEMORY_24H — score mémoire 8.029/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.951/10 — sources V4 — WATCH_ONLY
- ZAMA-EUR — MEMORY_24H — score mémoire 7.949/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DOT-EUR — MEMORY_24H — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- ETC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources V4 — MEMORY_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 7.732/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.719/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 7.700/10 — sources V4 — MEMORY_ONLY
- AAVE-EUR — MEMORY_24H — score mémoire 7.654/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PROVE-EUR — MEMORY_24H — score mémoire 7.637/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CELR-EUR +101.93% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +50.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +35.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +25.77% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +23.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +19.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HEI-EUR +17.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKL-EUR +16.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +16.38% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STX-EUR +14.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
