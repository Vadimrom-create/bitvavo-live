# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T14:59:16.988471+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.980 | entrée 6.850 | trend 8.100 | rang 7.240
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.240

## Accélération indépendante

- G-EUR — BUILDING_ACCELERATION — score 6.273/10 — DETECTED_BUT_TOO_LATE
- INJ-EUR — BUILDING_ACCELERATION — score 5.155/10 — DETECTED_BUT_TOO_LATE
- NEAR-EUR — BUILDING_ACCELERATION — score 5.000/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.277/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.234/10 — sources V4 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 8.059/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.045/10 — sources V4 — WATCH_ONLY
- XPL-EUR — ACTIVE_NOW — score mémoire 7.994/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.881/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LPT-EUR — MEMORY_24H — score mémoire 7.863/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.734/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.730/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- G-EUR +127.35% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +39.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +31.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARB-EUR +28.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +26.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +22.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DRIFT-EUR +20.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LPT-EUR +20.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +19.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ETHFI-EUR +19.86% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
