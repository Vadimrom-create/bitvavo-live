# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T01:25:18.941605+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 8.241 | entrée 5.650 | trend 9.200 | rang 7.170
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : aucun candidat matériel

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.170

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 7.300/10 — DETECTED_BUT_TOO_LATE
- FIL-EUR — BUILDING_ACCELERATION — score 5.634/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LAPTOP-EUR — MEMORY_24H — score mémoire 8.167/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.078/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.028/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.947/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.888/10 — sources V4 — WATCH_ONLY
- APT-EUR — MEMORY_24H — score mémoire 7.715/10 — sources V4 — MEMORY_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.619/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ZIG-EUR — MEMORY_24H — score mémoire 7.576/10 — sources V4 — MEMORY_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.571/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.564/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +34.47% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CVC-EUR +27.44% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +21.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IQ-EUR +17.72% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- VTHO-EUR +17.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZKJ-EUR +15.71% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +14.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOLV-EUR +14.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUNDIX-EUR +10.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +8.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
