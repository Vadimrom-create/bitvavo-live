# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T19:27:34.061083+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : GMT-EUR | action ACHETE_MAINTENANT | opportunité 9.159 | entrée 6.900 | trend 9.000 | rang 8.422
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SKY-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.552 | entrée 6.550 | trend 7.750 | rang 7.116
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : GRT-EUR | action LATENT_ACCELERATOR | opportunité 7.959 | entrée 5.550 | trend 8.550 | rang 7.585
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : BEAM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.655 | entrée 5.800 | trend 9.200 | rang 8.167
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. GMT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.422
2. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.167
3. A-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.164

## Accélération indépendante

- WMTX-EUR — CONFIRMED_ACCELERATION — score 9.982/10 — DETECTED_BUT_TOO_LATE
- LSK-EUR — CONFIRMED_ACCELERATION — score 7.674/10 — DETECTED_BUT_TOO_LATE
- PENDLE-EUR — CONFIRMED_ACCELERATION — score 7.512/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — CONFIRMED_ACCELERATION — score 6.889/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QNT-EUR — BUILDING_ACCELERATION — score 6.153/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — BUILDING_ACCELERATION — score 6.016/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QKC-EUR — BUILDING_ACCELERATION — score 5.727/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 2Z-EUR — BUILDING_ACCELERATION — score 5.533/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — BUILDING_ACCELERATION — score 5.447/10 — DETECTED_BUT_TOO_LATE
- PTB-EUR — BUILDING_ACCELERATION — score 5.087/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VVV-EUR — ACTIVE_NOW — score mémoire 7.609/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- WMTX-EUR — ACTIVE_NOW — score mémoire 9.982/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.429/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GMT-EUR — ACTIVE_NOW — score mémoire 8.422/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 8.167/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- A-EUR — ACTIVE_NOW — score mémoire 8.164/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- XAI-EUR +46.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +34.92% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- NOM-EUR +29.44% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ONDO-EUR +24.95% — DETECTED_EARLY — couche NONE — action NONE
- QNT-EUR +21.80% — DETECTED_EARLY — couche NONE — action NONE
- PLUME-EUR +21.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +19.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XPL-EUR +18.22% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TREAD-EUR +17.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LTC-EUR +16.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
