# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T16:47:47.753129+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XDC-EUR | action ACHETE_MAINTENANT | opportunité 8.321 | entrée 7.550 | trend 9.000 | rang 8.181
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PEAQ-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.020 | entrée 6.500 | trend 7.550 | rang 7.110
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 7.661 | entrée 5.150 | trend 8.450 | rang 7.295
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PYTH-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.457 | entrée 6.000 | trend 8.650 | rang 7.929
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XDC-EUR — ACHETE_MAINTENANT — rank 8.181 — opportunité 8.321 — entrée 7.550 — trend 9.000

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XDC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.181
2. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.929
3. LINK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.781

## Accélération indépendante

- ICX-EUR — BUILDING_ACCELERATION — score 5.948/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDGE-EUR — BUILDING_ACCELERATION — score 5.912/10 — DETECTED_BUT_TOO_LATE
- PARTI-EUR — BUILDING_ACCELERATION — score 5.879/10 — DETECTED_BUT_TOO_LATE
- ACT-EUR — BUILDING_ACCELERATION — score 5.829/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NMR-EUR — BUILDING_ACCELERATION — score 5.814/10 — DETECTED_BUT_TOO_LATE
- LUMIA-EUR — BUILDING_ACCELERATION — score 5.762/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XTZ-EUR — BUILDING_ACCELERATION — score 5.276/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SUSHI-EUR — BUILDING_ACCELERATION — score 5.076/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KSM-EUR — BUILDING_ACCELERATION — score 4.974/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FOLD-EUR — BUILDING_ACCELERATION — score 4.877/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- IMU-EUR — MEMORY_24H — score mémoire 9.209/10 — sources ACCELERATION — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.779/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PUMP-EUR — MEMORY_24H — score mémoire 8.750/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 8.582/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RECALL-EUR — MEMORY_24H — score mémoire 8.403/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 8.181/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 7.933/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.929/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- HBAR-EUR +36.29% — DETECTED_EARLY — couche NONE — action NONE
- QNT-EUR +25.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IKA-EUR +19.18% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- NMR-EUR +15.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALGO-EUR +15.00% — DETECTED_EARLY — couche NONE — action NONE
- MON-EUR +11.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AZTEC-EUR +9.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MIOTA-EUR +9.38% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRT-EUR +8.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +8.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
