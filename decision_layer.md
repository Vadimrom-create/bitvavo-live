# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T19:35:16.887766+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.386 | entrée 6.600 | trend 8.100 | rang 7.344
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.344
2. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.828
3. ZIL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.814

## Accélération indépendante

- LSK-EUR — BUILDING_ACCELERATION — score 5.134/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.139/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.872/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.807/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.778/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.768/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.649/10 — sources V4 — WATCH_ONLY
- DOGE-EUR — ACTIVE_NOW — score mémoire 7.637/10 — sources V4 — WATCH_ONLY
- YGG-EUR — ACTIVE_NOW — score mémoire 7.606/10 — sources V4 — WATCH_ONLY
- QKC-EUR — MEMORY_24H — score mémoire 7.588/10 — sources V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.587/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +277.18% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVC-EUR +57.72% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- REZ-EUR +30.53% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +23.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +20.04% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +18.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOLV-EUR +14.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +14.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POWR-EUR +12.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +11.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
