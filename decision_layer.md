# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T07:28:16.162529+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 8.327 | entrée 8.600 | trend 8.750 | rang 8.212
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : TURBO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.082 | entrée 6.500 | trend 7.550 | rang 7.783
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IOST-EUR | action LATENT_ACCELERATOR | opportunité 9.045 | entrée 5.250 | trend 7.650 | rang 7.660
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AXS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.603 | entrée 7.100 | trend 8.700 | rang 8.088
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.212
2. AXS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.088
3. A-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.060

## Accélération indépendante

- CPOOL-EUR — CONFIRMED_ACCELERATION — score 9.530/10 — DETECTED_BUT_TOO_LATE
- MLN-EUR — CONFIRMED_ACCELERATION — score 8.132/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 0G-EUR — BUILDING_ACCELERATION — score 6.069/10 — DETECTED_BUT_TOO_LATE
- SUPER-EUR — BUILDING_ACCELERATION — score 5.586/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — BUILDING_ACCELERATION — score 5.561/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AIOZ-EUR — BUILDING_ACCELERATION — score 5.351/10 — DETECTED_BUT_TOO_LATE
- GROVE-EUR — BUILDING_ACCELERATION — score 5.296/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WELL-EUR — BUILDING_ACCELERATION — score 5.200/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — BUILDING_ACCELERATION — score 4.999/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- IKA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CPOOL-EUR — ACTIVE_NOW — score mémoire 9.530/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SLX-EUR — MEMORY_24H — score mémoire 9.336/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- CETUS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.212/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MLN-EUR — ACTIVE_NOW — score mémoire 8.132/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.118/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AXS-EUR — ACTIVE_NOW — score mémoire 8.088/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +49.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +38.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +35.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +33.10% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +29.03% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SUPER-EUR +27.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +23.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SENT-EUR +19.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PENGU-EUR +19.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALLO-EUR +19.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
