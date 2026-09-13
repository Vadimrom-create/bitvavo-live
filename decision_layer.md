# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T20:21:41.268911+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.861 | entrée 7.350 | trend 7.650 | rang 7.431
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.431
2. ZIL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.591

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.330/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.252/10 — sources V4 — WATCH_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 8.049/10 — sources V4 — WATCH_ONLY
- KAVA-EUR — ACTIVE_NOW — score mémoire 7.912/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.791/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.758/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.757/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.680/10 — sources V4 — WATCH_ONLY
- KSM-EUR — ACTIVE_NOW — score mémoire 7.635/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.630/10 — sources ACCELERATION, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +303.48% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVC-EUR +57.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +22.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +20.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +20.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +16.92% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +16.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +14.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POWR-EUR +13.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOLV-EUR +12.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
