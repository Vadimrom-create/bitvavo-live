# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T01:36:10.763556+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VET-EUR | action LATENT_ACCELERATOR | opportunité 7.457 | entrée 5.750 | trend 8.450 | rang 7.218
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SOL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.202 | entrée 4.500 | trend 7.900 | rang 6.937
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.218
2. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.937
3. INJ-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.535

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.942/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CELR-EUR — MEMORY_24H — score mémoire 7.906/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZIG-EUR — ACTIVE_NOW — score mémoire 7.876/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZK-EUR — ACTIVE_NOW — score mémoire 7.863/10 — sources V4 — WATCH_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.851/10 — sources V4 — WATCH_ONLY
- DOT-EUR — MEMORY_24H — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.817/10 — sources V4 — DETECTED_BUT_TOO_LATE
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.801/10 — sources V4 — WATCH_ONLY
- ETC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources V4 — MEMORY_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.739/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +89.39% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +50.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +31.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +22.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SKL-EUR +20.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +20.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- INJ-EUR +18.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AVAX-EUR +18.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOLV-EUR +16.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +16.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
