# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T21:21:33.777782+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DOT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.396 | entrée 6.950 | trend 8.300 | rang 7.622
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.622

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.104/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 8.088/10 — sources V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 7.939/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.883/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.864/10 — sources V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.838/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.837/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ORCA-EUR — MEMORY_24H — score mémoire 7.810/10 — sources V4 — MEMORY_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.801/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.795/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- STRK-EUR +51.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +51.11% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +41.35% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +29.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +26.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +25.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +22.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CHIP-EUR +22.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +22.09% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +22.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
