# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T04:08:30.789693+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SUI-EUR | action ACHETE_MAINTENANT | opportunité 8.639 | entrée 7.800 | trend 6.700 | rang 7.360
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : HYPE-EUR | action LATENT_ACCELERATOR | opportunité 7.489 | entrée 4.500 | trend 8.250 | rang 7.119
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : aucun candidat matériel

## Top cross-sectionnel

1. SUI-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.360
2. HYPE-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.119

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- PEPE-EUR — MEMORY_24H — score mémoire 8.255/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.110/10 — sources ACCELERATION, V4 — WATCH_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 8.057/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 8.056/10 — sources V4 — DETECTED_BUT_TOO_LATE
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.936/10 — sources V4 — WATCH_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 7.858/10 — sources V4 — WATCH_ONLY
- ACH-EUR — ACTIVE_NOW — score mémoire 7.851/10 — sources V4 — WATCH_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 7.796/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.781/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.765/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- G-EUR +69.51% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +43.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +35.39% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +30.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +23.60% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QKC-EUR +20.34% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +19.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +19.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +17.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MORPHO-EUR +16.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
