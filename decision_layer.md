# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T16:07:00.127297+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.874 | entrée 5.700 | trend 9.200 | rang 8.166
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.166
2. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.582
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.319

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 7.715/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- HEI-EUR — MEMORY_24H — score mémoire 9.941/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.252/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.166/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SYN-EUR — MEMORY_24H — score mémoire 7.850/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.836/10 — sources V4 — WATCH_ONLY
- LIGHTER-EUR — ACTIVE_NOW — score mémoire 7.793/10 — sources V4 — WATCH_ONLY
- LSK-EUR — ACTIVE_NOW — score mémoire 7.715/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- XVG-EUR — ACTIVE_NOW — score mémoire 7.618/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.614/10 — sources V4 — WATCH_ONLY
- ALGO-EUR — MEMORY_24H — score mémoire 7.613/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SYN-EUR +141.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +76.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HEI-EUR +26.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FOLD-EUR +15.74% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +12.27% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SOSO-EUR +12.06% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- USELESS-EUR +11.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IOST-EUR +8.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +7.78% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZKJ-EUR +7.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
