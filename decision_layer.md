# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T06:39:19.611427+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.338 | entrée 6.300 | trend 7.950 | rang 7.223
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.223
2. AVAX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.008
3. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.898

## Accélération indépendante

- C-EUR — CONFIRMED_ACCELERATION — score 8.092/10 — DETECTED_BUT_TOO_LATE
- G-EUR — CONFIRMED_ACCELERATION — score 7.182/10 — DETECTED_BUT_TOO_LATE
- CELR-EUR — BUILDING_ACCELERATION — score 5.711/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- C-EUR — ACTIVE_NOW — score mémoire 8.092/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- PROVE-EUR — ACTIVE_NOW — score mémoire 8.000/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.985/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.969/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — MEMORY_24H — score mémoire 7.960/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.937/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NPC-EUR — MEMORY_24H — score mémoire 7.903/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DOT-EUR — MEMORY_24H — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- ETC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources V4 — MEMORY_ONLY
- APT-EUR — ACTIVE_NOW — score mémoire 7.745/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +109.69% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +94.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +37.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +31.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKL-EUR +26.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +23.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +19.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +15.98% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SOLV-EUR +15.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ONG-EUR +14.64% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
