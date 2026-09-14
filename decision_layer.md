# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T08:42:40.997169+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.016 | entrée 7.450 | trend 8.650 | rang 7.915
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.915
2. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.808
3. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.391

## Accélération indépendante

- LSK-EUR — BUILDING_ACCELERATION — score 6.321/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- YB-EUR — ACTIVE_NOW — score mémoire 8.050/10 — sources V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XTZ-EUR — ACTIVE_NOW — score mémoire 8.010/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.947/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.943/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.915/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.857/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.808/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 7.710/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.673/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CVC-EUR +51.67% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FIL-EUR +27.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CPOOL-EUR +26.90% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LSK-EUR +26.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +25.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IQ-EUR +17.04% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- MTL-EUR +13.34% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- LIGHTER-EUR +12.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BABY-EUR +11.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- T-EUR +11.21% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
