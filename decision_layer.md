# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T15:19:59.522388+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.866 | entrée 7.050 | trend 8.100 | rang 7.193
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.193

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- VTHO-EUR — ACTIVE_NOW — score mémoire 8.173/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.079/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.928/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.868/10 — sources V4 — WATCH_ONLY
- LPT-EUR — MEMORY_24H — score mémoire 7.863/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.843/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZORA-EUR — ACTIVE_NOW — score mémoire 7.805/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.804/10 — sources V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 7.795/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LINEA-EUR — ACTIVE_NOW — score mémoire 7.753/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +103.52% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +50.92% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CNPY-EUR +41.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +32.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARB-EUR +27.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +26.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +20.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +20.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +20.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SKY-EUR +18.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
