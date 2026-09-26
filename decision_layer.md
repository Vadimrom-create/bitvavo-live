# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T10:01:51.969392+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 8.623 | entrée 7.250 | trend 8.850 | rang 8.129
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.768 | entrée 6.000 | trend 9.000 | rang 8.108
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZK-EUR | action LATENT_ACCELERATOR | opportunité 8.006 | entrée 5.700 | trend 8.950 | rang 7.828
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.383 | entrée 6.950 | trend 8.850 | rang 8.116
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.129
2. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.116
3. BEAM-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.108

## Accélération indépendante

- RARE-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- QNT-EUR — CONFIRMED_ACCELERATION — score 7.976/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OGN-EUR — CONFIRMED_ACCELERATION — score 7.558/10 — DETECTED_BUT_TOO_LATE
- SLP-EUR — BUILDING_ACCELERATION — score 6.150/10 — DETECTED_BUT_TOO_LATE
- ALT-EUR — BUILDING_ACCELERATION — score 6.003/10 — DETECTED_BUT_TOO_LATE
- DYM-EUR — BUILDING_ACCELERATION — score 5.499/10 — DETECTED_BUT_TOO_LATE
- ADX-EUR — BUILDING_ACCELERATION — score 5.079/10 — DETECTED_BUT_TOO_LATE
- AUDIO-EUR — BUILDING_ACCELERATION — score 4.837/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NEAR-EUR — BUILDING_ACCELERATION — score 4.810/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XPL-EUR — ACTIVE_NOW — score mémoire 7.604/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZRC-EUR — MEMORY_24H — score mémoire 9.830/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.063/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RARE-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- IMU-EUR — MEMORY_24H — score mémoire 8.394/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +163.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +76.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 2Z-EUR +37.40% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PHA-EUR +30.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +25.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +25.07% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +17.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TNSR-EUR +16.86% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- EDGE-EUR +16.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PROM-EUR +14.72% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
