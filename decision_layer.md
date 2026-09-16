# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T02:11:41.073849+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.688 | entrée 4.850 | trend 9.200 | rang 6.648
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : aucun candidat matériel

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.648

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- USELESS-EUR — ACTIVE_NOW — score mémoire 7.973/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SIGN-EUR — ACTIVE_NOW — score mémoire 7.824/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.792/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.710/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.691/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.672/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.600/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — MEMORY_24H — score mémoire 7.598/10 — sources V4 — MEMORY_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.595/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.571/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PUFFER-EUR +32.02% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CROSS-EUR +31.64% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ALIGN-EUR +31.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LAPTOP-EUR +26.99% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- VTHO-EUR +20.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +18.39% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +17.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +12.59% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +12.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +9.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
