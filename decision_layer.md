# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T12:38:34.314520+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.693 | entrée 4.300 | trend 9.200 | rang 6.381
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.662 | entrée 7.100 | trend 8.100 | rang 7.262
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.262
2. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.381

## Accélération indépendante

- USELESS-EUR — CONFIRMED_ACCELERATION — score 7.788/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XVG-EUR — ACTIVE_NOW — score mémoire 8.458/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.206/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 8.015/10 — sources V4 — DETECTED_BUT_TOO_LATE
- XTZ-EUR — ACTIVE_NOW — score mémoire 7.970/10 — sources V4 — WATCH_ONLY
- COTI-EUR — ACTIVE_NOW — score mémoire 7.961/10 — sources V4 — DETECTED_BUT_TOO_LATE
- METIS-EUR — ACTIVE_NOW — score mémoire 7.918/10 — sources V4 — DETECTED_BUT_TOO_LATE
- YGG-EUR — ACTIVE_NOW — score mémoire 7.847/10 — sources V4 — WATCH_ONLY
- USELESS-EUR — ACTIVE_NOW — score mémoire 7.788/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.766/10 — sources V4 — WATCH_ONLY
- ZRX-EUR — ACTIVE_NOW — score mémoire 7.759/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +405.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVC-EUR +65.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +51.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUNDIX-EUR +29.34% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- POWR-EUR +28.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FLOCK-EUR +27.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +23.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- REZ-EUR +20.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MTL-EUR +18.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVA-EUR +16.87% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
