# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T00:56:29.340309+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : PHA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.880 | entrée 6.550 | trend 8.250 | rang 7.066
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PHA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.066
2. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.444

## Accélération indépendante

- DRIFT-EUR — CONFIRMED_ACCELERATION — score 7.782/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 9.527/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.341/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.319/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.207/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.184/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.177/10 — sources V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.973/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.881/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.849/10 — sources V4 — WATCH_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 7.838/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +67.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DRIFT-EUR +59.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +46.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +38.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +37.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +31.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +18.73% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +17.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +16.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +16.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
