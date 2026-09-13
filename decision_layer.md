# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T12:26:19.812485+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.793 | entrée 4.750 | trend 9.200 | rang 6.412
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.366 | entrée 7.400 | trend 7.650 | rang 7.221
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.221
2. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.412

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 7.360/10 — DETECTED_BUT_TOO_LATE
- NPC-EUR — BUILDING_ACCELERATION — score 6.352/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- REZ-EUR — BUILDING_ACCELERATION — score 5.427/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- NPC-EUR — ACTIVE_NOW — score mémoire 8.134/10 — sources ACCELERATION, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.991/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.923/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.807/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.784/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.774/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.686/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.657/10 — sources V4 — DETECTED_BUT_TOO_LATE
- METIS-EUR — ACTIVE_NOW — score mémoire 7.580/10 — sources V4 — WATCH_ONLY
- YGG-EUR — ACTIVE_NOW — score mémoire 7.566/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +392.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVC-EUR +58.21% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +55.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FLOCK-EUR +29.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POWR-EUR +29.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUNDIX-EUR +26.30% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +24.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MTL-EUR +21.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +20.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVA-EUR +17.18% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
