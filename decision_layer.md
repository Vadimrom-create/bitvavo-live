# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T18:24:01.276027+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SOL-EUR | action ACHETE_MAINTENANT | opportunité 8.173 | entrée 8.250 | trend 8.750 | rang 8.098
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZEN-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.625 | entrée 6.000 | trend 8.300 | rang 7.305
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BREV-EUR | action LATENT_ACCELERATOR | opportunité 7.530 | entrée 4.500 | trend 8.450 | rang 7.233
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.017 | entrée 8.400 | trend 8.350 | rang 7.884
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.098
2. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.884
3. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.834

## Accélération indépendante

- DRIFT-EUR — CONFIRMED_ACCELERATION — score 7.297/10 — DETECTED_BUT_TOO_LATE
- SXT-EUR — CONFIRMED_ACCELERATION — score 7.044/10 — DETECTED_BUT_TOO_LATE
- XMN-EUR — BUILDING_ACCELERATION — score 5.795/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZIL-EUR — BUILDING_ACCELERATION — score 5.729/10 — DETECTED_BUT_TOO_LATE
- PENGU-EUR — BUILDING_ACCELERATION — score 5.684/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — BUILDING_ACCELERATION — score 5.308/10 — DETECTED_BUT_TOO_LATE
- EDGE-EUR — BUILDING_ACCELERATION — score 5.161/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — BUILDING_ACCELERATION — score 5.148/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RON-EUR — BUILDING_ACCELERATION — score 5.077/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 4.837/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TAI-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- APE-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- HMSTR-EUR — MEMORY_24H — score mémoire 8.203/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SOL-EUR — ACTIVE_NOW — score mémoire 8.098/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.884/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.834/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- 0G-EUR — ACTIVE_NOW — score mémoire 7.821/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CHR-EUR — MEMORY_24H — score mémoire 7.801/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- DRIFT-EUR +45.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +39.87% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NIL-EUR +29.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +28.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +22.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +18.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KITE-EUR +18.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +18.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +15.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +14.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
