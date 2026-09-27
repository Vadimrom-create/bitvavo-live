# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T21:01:42.145064+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SEI-EUR | action ACHETE_MAINTENANT | opportunité 8.933 | entrée 7.650 | trend 8.850 | rang 8.192
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : AXS-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.475 | entrée 5.850 | trend 8.700 | rang 7.973
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BABY-EUR | action LATENT_ACCELERATOR | opportunité 9.168 | entrée 5.200 | trend 8.100 | rang 7.997
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : OP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.364 | entrée 6.250 | trend 8.950 | rang 8.519
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. OP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.519
2. BIGTIME-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.322
3. SNX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.232

## Accélération indépendante

- CSPR-EUR — BUILDING_ACCELERATION — score 6.370/10 — DETECTED_BUT_TOO_LATE
- HFT-EUR — BUILDING_ACCELERATION — score 5.533/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AGI-EUR — BUILDING_ACCELERATION — score 5.347/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CELR-EUR — BUILDING_ACCELERATION — score 5.188/10 — DETECTED_BUT_TOO_LATE
- NOS-EUR — BUILDING_ACCELERATION — score 5.067/10 — DETECTED_BUT_TOO_LATE
- THQ-EUR — BUILDING_ACCELERATION — score 4.768/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SKY-EUR — MEMORY_24H — score mémoire 9.054/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OP-EUR — ACTIVE_NOW — score mémoire 8.519/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- POND-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- APE-EUR — MEMORY_24H — score mémoire 8.344/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BIGTIME-EUR — ACTIVE_NOW — score mémoire 8.322/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SNX-EUR — ACTIVE_NOW — score mémoire 8.232/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SEI-EUR — ACTIVE_NOW — score mémoire 8.192/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +62.44% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +43.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INX-EUR +30.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- W-EUR +22.80% — DETECTED_EARLY — couche NONE — action NONE
- TREAD-EUR +21.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRT-EUR +17.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AUDIO-EUR +15.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUMP-EUR +15.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +15.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +14.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
