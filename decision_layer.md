# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T08:22:48.438526+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.862 | entrée 6.800 | trend 8.650 | rang 7.787
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.787
2. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.786
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.401

## Accélération indépendante

- ARK-EUR — CONFIRMED_ACCELERATION — score 7.058/10 — DETECTED_BUT_TOO_LATE
- CVC-EUR — BUILDING_ACCELERATION — score 5.829/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LSK-EUR — MEMORY_24H — score mémoire 8.317/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.216/10 — sources V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.930/10 — sources V4 — WATCH_ONLY
- TAO-EUR — ACTIVE_NOW — score mémoire 7.924/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.826/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.787/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.786/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAVA-EUR — ACTIVE_NOW — score mémoire 7.730/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.670/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CVC-EUR +56.54% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FIL-EUR +26.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +25.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CPOOL-EUR +25.34% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- REZ-EUR +21.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IQ-EUR +17.41% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- MTL-EUR +14.09% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +12.67% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LIGHTER-EUR +11.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BABY-EUR +10.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
