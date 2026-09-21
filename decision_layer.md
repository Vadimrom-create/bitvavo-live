# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T03:02:16.574217+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAO-EUR | action ACHETE_MAINTENANT | opportunité 9.007 | entrée 7.850 | trend 7.950 | rang 8.041
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : GRT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.531 | entrée 6.050 | trend 8.700 | rang 7.785
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COW-EUR | action LATENT_ACCELERATOR | opportunité 7.402 | entrée 5.100 | trend 8.650 | rang 7.371
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.001 | entrée 6.250 | trend 8.900 | rang 7.785
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.041
2. GRT-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.785
3. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.785

## Accélération indépendante

- FTT-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- CELR-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- XPL-EUR — CONFIRMED_ACCELERATION — score 6.792/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AEVO-EUR — BUILDING_ACCELERATION — score 6.054/10 — DETECTED_BUT_TOO_LATE
- WOO-EUR — BUILDING_ACCELERATION — score 5.833/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOLV-EUR — BUILDING_ACCELERATION — score 5.153/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INX-EUR — BUILDING_ACCELERATION — score 4.879/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — BUILDING_ACCELERATION — score 4.835/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- FET-EUR — ACTIVE_NOW — score mémoire 6.972/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- FTT-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- CELR-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LSK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.376/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.113/10 — sources ACCELERATION — MEMORY_ONLY
- TAO-EUR — ACTIVE_NOW — score mémoire 8.041/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 7.815/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- PTB-EUR +80.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +43.65% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +38.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +26.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VVV-EUR +25.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +24.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +22.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NEAR-EUR +21.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- S-EUR +19.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +18.88% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
