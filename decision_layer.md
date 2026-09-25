# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T22:19:32.121819+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : DATAIP-EUR | action ACHETE_MAINTENANT | opportunité 9.013 | entrée 7.450 | trend 8.200 | rang 8.161
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CAKE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.865 | entrée 6.150 | trend 8.950 | rang 7.818
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZK-EUR | action LATENT_ACCELERATOR | opportunité 8.291 | entrée 5.050 | trend 8.950 | rang 7.876
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PYTH-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.220 | entrée 7.600 | trend 9.200 | rang 8.542
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.542
2. FLUX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.322
3. DATAIP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.161

## Accélération indépendante

- SENT-EUR — CONFIRMED_ACCELERATION — score 7.375/10 — DETECTED_BUT_TOO_LATE
- DRIFT-EUR — CONFIRMED_ACCELERATION — score 7.108/10 — DETECTED_BUT_TOO_LATE
- CHIP-EUR — BUILDING_ACCELERATION — score 6.443/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SUPER-EUR — BUILDING_ACCELERATION — score 6.076/10 — DETECTED_BUT_TOO_LATE
- PENGU-EUR — BUILDING_ACCELERATION — score 5.231/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FET-EUR — BUILDING_ACCELERATION — score 5.090/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PHA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.667/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.542/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- FLUX-EUR — ACTIVE_NOW — score mémoire 8.322/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DATAIP-EUR — ACTIVE_NOW — score mémoire 8.161/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MANA-EUR — ACTIVE_NOW — score mémoire 8.148/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.111/10 — sources ACCELERATION — MEMORY_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 8.099/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.094/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- PHA-EUR +91.12% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +24.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +22.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +21.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +20.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +19.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUI-EUR +18.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DEEP-EUR +17.95% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- GRASS-EUR +16.54% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- JTO-EUR +16.29% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
