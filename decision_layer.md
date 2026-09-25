# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T13:25:59.256703+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ADA-EUR | action ACHETE_MAINTENANT | opportunité 7.928 | entrée 8.000 | trend 8.500 | rang 7.833
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MANTRA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.157 | entrée 5.950 | trend 8.050 | rang 8.018
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : LTC-EUR | action LATENT_ACCELERATOR | opportunité 7.716 | entrée 4.500 | trend 8.650 | rang 7.443
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SENT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.489 | entrée 6.600 | trend 8.900 | rang 8.082
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SENT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.082
2. ATH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.068
3. ENS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.059

## Accélération indépendante

- BIO-EUR — CONFIRMED_ACCELERATION — score 8.143/10 — DETECTED_BUT_TOO_LATE
- TOWNS-EUR — CONFIRMED_ACCELERATION — score 6.576/10 — DETECTED_BUT_TOO_LATE
- PIXEL-EUR — BUILDING_ACCELERATION — score 5.357/10 — DETECTED_BUT_TOO_LATE
- CHIP-EUR — BUILDING_ACCELERATION — score 5.309/10 — DETECTED_BUT_TOO_LATE
- NPC-EUR — BUILDING_ACCELERATION — score 5.073/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FORM-EUR — BUILDING_ACCELERATION — score 5.061/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — BUILDING_ACCELERATION — score 4.937/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALLO-EUR — BUILDING_ACCELERATION — score 4.828/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- HUMA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SCR-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GLMR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 8.218/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BIO-EUR — ACTIVE_NOW — score mémoire 8.143/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SENT-EUR — ACTIVE_NOW — score mémoire 8.082/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ATH-EUR — ACTIVE_NOW — score mémoire 8.068/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ENS-EUR — ACTIVE_NOW — score mémoire 8.059/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SNX-EUR — ACTIVE_NOW — score mémoire 8.019/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PHA-EUR +42.87% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- TREAD-EUR +33.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +32.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +25.67% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +25.11% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PIXEL-EUR +21.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CHIP-EUR +19.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DBR-EUR +18.85% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +18.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FET-EUR +16.33% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
