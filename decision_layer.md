# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T19:46:19.185140+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DOT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.360 | entrée 7.300 | trend 8.300 | rang 7.775
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.775
2. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.645

## Accélération indépendante

- POL-EUR — BUILDING_ACCELERATION — score 6.455/10 — DETECTED_BUT_TOO_LATE
- ZEN-EUR — BUILDING_ACCELERATION — score 6.061/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- KAS-EUR — ACTIVE_NOW — score mémoire 8.205/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ICP-EUR — ACTIVE_NOW — score mémoire 8.121/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.049/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.005/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.888/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.823/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.801/10 — sources V4 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.799/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- METIS-EUR — ACTIVE_NOW — score mémoire 7.795/10 — sources V4 — DETECTED_BUT_TOO_LATE
- DOT-EUR — ACTIVE_NOW — score mémoire 7.775/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- G-EUR +57.41% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +45.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +38.59% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +25.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +24.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +23.19% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIG-EUR +23.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +22.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZAMA-EUR +21.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +21.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
