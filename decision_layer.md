# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T20:51:17.074347+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.546 | entrée 7.350 | trend 7.650 | rang 7.283
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.283

## Accélération indépendante

- CVC-EUR — CONFIRMED_ACCELERATION — score 6.973/10 — DETECTED_BUT_TOO_LATE
- REZ-EUR — BUILDING_ACCELERATION — score 4.783/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.539/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.241/10 — sources V4 — WATCH_ONLY
- BLUR-EUR — ACTIVE_NOW — score mémoire 7.949/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.901/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.757/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.728/10 — sources V4 — WATCH_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 7.726/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.715/10 — sources V4 — WATCH_ONLY
- USELESS-EUR — ACTIVE_NOW — score mémoire 7.589/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- QKC-EUR — MEMORY_24H — score mémoire 7.588/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- LSK-EUR +315.80% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVC-EUR +64.33% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +22.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FIL-EUR +22.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +20.56% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +17.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +14.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +14.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOLV-EUR +14.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POWR-EUR +12.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
