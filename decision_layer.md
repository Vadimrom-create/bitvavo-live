# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T18:51:40.248456+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : LSK-EUR | action LATENT_ACCELERATOR | opportunité 7.401 | entrée 4.550 | trend 8.400 | rang -2.326
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.007 | entrée 7.050 | trend 8.100 | rang 7.314
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.314
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.292
3. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.654

## Accélération indépendante

- LSK-EUR — BUILDING_ACCELERATION — score 5.008/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- W-EUR — ACTIVE_NOW — score mémoire 8.058/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.950/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.880/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.876/10 — sources V4 — WATCH_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 7.868/10 — sources V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.867/10 — sources V4 — WATCH_ONLY
- SPX-EUR — ACTIVE_NOW — score mémoire 7.785/10 — sources V4 — WATCH_ONLY
- YGG-EUR — ACTIVE_NOW — score mémoire 7.698/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.607/10 — sources V4 — WATCH_ONLY
- QKC-EUR — MEMORY_24H — score mémoire 7.588/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- LSK-EUR +260.02% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVC-EUR +54.44% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +23.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +22.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- REZ-EUR +19.98% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +17.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +16.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POWR-EUR +14.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +12.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRAX-EUR +11.62% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
