# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T20:38:04.030364+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.909 | entrée 7.150 | trend 7.650 | rang 7.393
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.393
2. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.834

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.505/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 8.056/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.042/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 8.016/10 — sources V4 — DETECTED_BUT_TOO_LATE
- PHA-EUR — ACTIVE_NOW — score mémoire 7.843/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.832/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.804/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.800/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.668/10 — sources ACCELERATION, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.594/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +318.18% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVC-EUR +58.31% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +22.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +21.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- REZ-EUR +19.62% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +18.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +15.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +15.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOLV-EUR +12.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POWR-EUR +12.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
