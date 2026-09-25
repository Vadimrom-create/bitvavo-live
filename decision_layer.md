# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T12:49:08.739239+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ADA-EUR | action ACHETE_MAINTENANT | opportunité 8.324 | entrée 7.600 | trend 8.500 | rang 7.934
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RUNE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.797 | entrée 6.450 | trend 8.700 | rang 7.665
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : LTC-EUR | action LATENT_ACCELERATOR | opportunité 7.542 | entrée 4.500 | trend 8.650 | rang 7.345
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : CAKE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.944 | entrée 6.600 | trend 8.950 | rang 8.180
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.180
2. COMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.083
3. ADA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.934

## Accélération indépendante

- HUMA-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- KITE-EUR — CONFIRMED_ACCELERATION — score 7.195/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POL-EUR — CONFIRMED_ACCELERATION — score 7.022/10 — DETECTED_BUT_TOO_LATE
- MEW-EUR — CONFIRMED_ACCELERATION — score 6.932/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RARE-EUR — CONFIRMED_ACCELERATION — score 6.835/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PNUT-EUR — CONFIRMED_ACCELERATION — score 6.823/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MET-EUR — CONFIRMED_ACCELERATION — score 6.545/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OP-EUR — BUILDING_ACCELERATION — score 6.482/10 — DETECTED_BUT_TOO_LATE
- AIXBT-EUR — BUILDING_ACCELERATION — score 6.440/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BONK-EUR — BUILDING_ACCELERATION — score 6.391/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CAKE-EUR — ACTIVE_NOW — score mémoire 8.180/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- INJ-EUR — ACTIVE_NOW — score mémoire 7.883/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- XRP-EUR — ACTIVE_NOW — score mémoire 7.312/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- HUMA-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- SCR-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GLMR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 8.374/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 8.218/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- PHA-EUR +35.78% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- TREAD-EUR +34.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +33.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +27.92% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +25.95% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +21.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FET-EUR +21.55% — DETECTED_EARLY — couche NONE — action NONE
- PIXEL-EUR +21.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HUMA-EUR +21.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DEEP-EUR +19.88% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
