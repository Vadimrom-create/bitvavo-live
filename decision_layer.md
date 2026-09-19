# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T00:36:49.425527+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : FET-EUR | action ACHETE_MAINTENANT | opportunité 8.566 | entrée 7.500 | trend 8.650 | rang 8.142
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : SOL-EUR | action LATENT_ACCELERATOR | opportunité 7.479 | entrée 4.500 | trend 7.950 | rang 6.600
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.026 | entrée 8.250 | trend 8.400 | rang 7.860
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.142
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.860
3. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.800

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- AAVE-EUR — ACTIVE_NOW — score mémoire 8.442/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- SYN-EUR — MEMORY_24H — score mémoire 8.311/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 8.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.142/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZRX-EUR — ACTIVE_NOW — score mémoire 8.068/10 — sources V4 — WATCH_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.031/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 8.030/10 — sources V4 — WATCH_ONLY
- YB-EUR — MEMORY_24H — score mémoire 7.953/10 — sources V4 — MEMORY_ONLY
- GALA-EUR — ACTIVE_NOW — score mémoire 7.950/10 — sources V4 — WATCH_ONLY
- PEPE-EUR — ACTIVE_NOW — score mémoire 7.941/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- F-EUR +56.21% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +55.45% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +49.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +23.26% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- APT-EUR +23.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +23.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +22.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +22.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +20.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +20.13% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
