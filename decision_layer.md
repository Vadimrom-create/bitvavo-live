# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T08:59:08.367797+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.287 | entrée 6.200 | trend 9.200 | rang 8.108
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.108
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.552
3. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.368

## Accélération indépendante

- POWR-EUR — BUILDING_ACCELERATION — score 5.487/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- BABY-EUR — BUILDING_ACCELERATION — score 5.474/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- YB-EUR — ACTIVE_NOW — score mémoire 8.332/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.108/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.990/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.956/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.858/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.843/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.790/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.774/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 7.704/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- CVC-EUR +49.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- REZ-EUR +28.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CPOOL-EUR +27.22% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +26.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +23.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MTL-EUR +14.34% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- IQ-EUR +13.91% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +12.49% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LIGHTER-EUR +12.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BABY-EUR +11.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
