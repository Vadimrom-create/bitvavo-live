# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T07:01:34.517306+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.165 | entrée 6.050 | trend 9.200 | rang 7.999
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.999
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.332

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- W-EUR — ACTIVE_NOW — score mémoire 8.186/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.040/10 — sources V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.999/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 7.972/10 — sources V4 — DETECTED_BUT_TOO_LATE
- BNB-EUR — ACTIVE_NOW — score mémoire 7.972/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.945/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.915/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.867/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.817/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CVC-EUR +44.15% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- REZ-EUR +34.58% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +29.75% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +23.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CPOOL-EUR +22.26% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +14.63% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IQ-EUR +13.15% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- MOVR-EUR +12.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LIGHTER-EUR +11.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +10.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
