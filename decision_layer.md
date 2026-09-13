# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T19:48:25.361949+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.795 | entrée 6.150 | trend 9.200 | rang 6.919
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.919
2. ZIL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.424

## Accélération indépendante

- CVC-EUR — CONFIRMED_ACCELERATION — score 6.846/10 — DETECTED_BUT_TOO_LATE
- LSK-EUR — BUILDING_ACCELERATION — score 5.304/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ATOM-EUR — ACTIVE_NOW — score mémoire 8.264/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.070/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.984/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.804/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.795/10 — sources V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.740/10 — sources V4 — WATCH_ONLY
- YGG-EUR — ACTIVE_NOW — score mémoire 7.656/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.629/10 — sources V4 — WATCH_ONLY
- QKC-EUR — MEMORY_24H — score mémoire 7.588/10 — sources V4 — MEMORY_ONLY
- KSM-EUR — ACTIVE_NOW — score mémoire 7.585/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +284.13% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVC-EUR +58.64% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- REZ-EUR +26.41% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +22.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +19.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZIL-EUR +18.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +17.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOLV-EUR +13.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +12.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POWR-EUR +11.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
