# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T09:35:55.293261+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PYTH-EUR | action ACHETE_MAINTENANT | opportunité 8.352 | entrée 6.900 | trend 8.300 | rang 7.814
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MEME-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.282 | entrée 6.150 | trend 8.700 | rang 7.715
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : EDEN-EUR | action LATENT_ACCELERATOR | opportunité 7.922 | entrée 5.400 | trend 8.600 | rang 7.621
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LTC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.167 | entrée 6.950 | trend 9.000 | rang 8.071
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.071
2. ZK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.986
3. MOVR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.938

## Accélération indépendante

- TRIA-EUR — CONFIRMED_ACCELERATION — score 9.219/10 — DETECTED_BUT_TOO_LATE
- BOB-EUR — CONFIRMED_ACCELERATION — score 8.429/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — CONFIRMED_ACCELERATION — score 7.460/10 — DETECTED_BUT_TOO_LATE
- MET-EUR — BUILDING_ACCELERATION — score 6.335/10 — DETECTED_BUT_TOO_LATE
- A-EUR — BUILDING_ACCELERATION — score 5.435/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 0G-EUR — BUILDING_ACCELERATION — score 5.243/10 — DETECTED_BUT_TOO_LATE
- CAP-EUR — BUILDING_ACCELERATION — score 5.230/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FIDA-EUR — BUILDING_ACCELERATION — score 5.220/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- COTI-EUR — BUILDING_ACCELERATION — score 4.980/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 4.925/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ICX-EUR — MEMORY_24H — score mémoire 9.359/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SLX-EUR — MEMORY_24H — score mémoire 9.336/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TRIA-EUR — ACTIVE_NOW — score mémoire 9.219/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- CPOOL-EUR — MEMORY_24H — score mémoire 8.975/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ALLO-EUR — MEMORY_24H — score mémoire 8.962/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CETUS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SUPER-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BOB-EUR — ACTIVE_NOW — score mémoire 8.429/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- FTT-EUR — MEMORY_24H — score mémoire 8.118/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- MET-EUR +39.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CPOOL-EUR +38.85% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +34.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +29.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +28.86% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ALLO-EUR +25.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +24.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TIA-EUR +21.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PENGU-EUR +21.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SENT-EUR +19.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
