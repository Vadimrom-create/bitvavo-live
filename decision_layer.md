# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T01:06:24.398529+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 8.683 | entrée 5.650 | trend 9.200 | rang 7.316
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : aucun candidat matériel

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.316

## Accélération indépendante

- LAPTOP-EUR — CONFIRMED_ACCELERATION — score 8.167/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LAPTOP-EUR — ACTIVE_NOW — score mémoire 8.167/10 — sources ACCELERATION, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.151/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.952/10 — sources V4 — WATCH_ONLY
- ZRX-EUR — ACTIVE_NOW — score mémoire 7.912/10 — sources V4 — WATCH_ONLY
- S-EUR — ACTIVE_NOW — score mémoire 7.843/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.843/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.838/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.747/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.738/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LIGHTER-EUR — ACTIVE_NOW — score mémoire 7.733/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +54.14% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CVC-EUR +28.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +20.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZKJ-EUR +18.78% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SOLV-EUR +18.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +16.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IQ-EUR +15.08% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- PUNDIX-EUR +11.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +9.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +8.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
