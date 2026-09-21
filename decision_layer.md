# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T12:35:52.787997+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAIKO-EUR | action ACHETE_MAINTENANT | opportunité 8.417 | entrée 7.100 | trend 8.150 | rang 7.705
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PENDLE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.274 | entrée 6.100 | trend 8.950 | rang 7.967
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ACH-EUR | action LATENT_ACCELERATOR | opportunité 7.612 | entrée 4.500 | trend 9.000 | rang 7.479
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AERO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.727 | entrée 6.850 | trend 8.450 | rang 8.024
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AERO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.024
2. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.018
3. PENDLE-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.967

## Accélération indépendante

- ARB-EUR — CONFIRMED_ACCELERATION — score 9.412/10 — DETECTED_BUT_TOO_LATE
- ACU-EUR — CONFIRMED_ACCELERATION — score 9.053/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZAMA-EUR — CONFIRMED_ACCELERATION — score 7.530/10 — DETECTED_BUT_TOO_LATE
- RENDER-EUR — CONFIRMED_ACCELERATION — score 7.372/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — CONFIRMED_ACCELERATION — score 7.321/10 — DETECTED_BUT_TOO_LATE
- LTC-EUR — CONFIRMED_ACCELERATION — score 7.227/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PTB-EUR — CONFIRMED_ACCELERATION — score 6.794/10 — DETECTED_BUT_TOO_LATE
- ARX-EUR — CONFIRMED_ACCELERATION — score 6.501/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XMN-EUR — BUILDING_ACCELERATION — score 6.467/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GALA-EUR — BUILDING_ACCELERATION — score 6.397/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 9.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.488/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 9.465/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARB-EUR — ACTIVE_NOW — score mémoire 9.412/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AIOZ-EUR — MEMORY_24H — score mémoire 9.407/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMX-EUR — MEMORY_24H — score mémoire 9.317/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACU-EUR — ACTIVE_NOW — score mémoire 9.053/10 — sources ACCELERATION, V4 — WATCH_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.457/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SFP-EUR — MEMORY_24H — score mémoire 8.323/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +72.55% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +65.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +38.05% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +31.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +30.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +29.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +26.51% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AIOZ-EUR +26.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUI-EUR +25.78% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CETUS-EUR +24.05% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
