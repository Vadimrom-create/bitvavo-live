# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T10:25:26.432946+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : BNB-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.060 | entrée 6.500 | trend 7.500 | rang 7.768
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.224 | entrée 6.000 | trend 9.200 | rang 7.832
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.832
2. BNB-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.768
3. CAKE-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.521

## Accélération indépendante

- SYRUP-EUR — CONFIRMED_ACCELERATION — score 8.187/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ENSO-EUR — MEMORY_24H — score mémoire 8.974/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 8.295/10 — sources V4 — DETECTED_BUT_TOO_LATE
- SYRUP-EUR — ACTIVE_NOW — score mémoire 8.187/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ENS-EUR — ACTIVE_NOW — score mémoire 8.161/10 — sources V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 8.153/10 — sources V4 — DETECTED_BUT_TOO_LATE
- XVG-EUR — ACTIVE_NOW — score mémoire 8.035/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.897/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.890/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.882/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.870/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +80.34% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +36.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +36.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DRIFT-EUR +33.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +26.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARB-EUR +25.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +25.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +22.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +21.64% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- RAY-EUR +21.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
