# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T04:26:49.108039+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.615 | entrée 7.550 | trend 8.250 | rang 7.535
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.535
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.185
3. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.127

## Accélération indépendante

- G-EUR — CONFIRMED_ACCELERATION — score 6.999/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AERO-EUR — ACTIVE_NOW — score mémoire 8.364/10 — sources V4 — WATCH_ONLY
- RAY-EUR — ACTIVE_NOW — score mémoire 8.199/10 — sources ACCELERATION, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.135/10 — sources V4 — WATCH_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 8.100/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.000/10 — sources ACCELERATION, V4 — WATCH_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 7.868/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- BEAM-EUR — ACTIVE_NOW — score mémoire 7.856/10 — sources V4 — WATCH_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 7.741/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.712/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ACH-EUR — ACTIVE_NOW — score mémoire 7.704/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +77.41% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +38.44% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +34.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +28.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +21.17% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIG-EUR +19.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +17.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MORPHO-EUR +17.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QKC-EUR +17.44% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +17.22% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
