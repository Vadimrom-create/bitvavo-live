# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T19:17:31.217762+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TRX-EUR | action ACHETE_MAINTENANT | opportunité 6.686 | entrée 7.150 | trend 4.950 | rang 5.812
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PLUME-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.476 | entrée 6.300 | trend 7.450 | rang 7.397
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : FLUX-EUR | action LATENT_ACCELERATOR | opportunité 8.103 | entrée 5.750 | trend 8.850 | rang 7.399
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LTC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.345 | entrée 6.750 | trend 8.700 | rang 7.952
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.952
2. DATAIP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.821
3. AERO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.746

## Accélération indépendante

- GRASS-EUR — CONFIRMED_ACCELERATION — score 9.229/10 — DETECTED_BUT_TOO_LATE
- HFT-EUR — CONFIRMED_ACCELERATION — score 9.146/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBCN-EUR — CONFIRMED_ACCELERATION — score 8.056/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARX-EUR — CONFIRMED_ACCELERATION — score 7.393/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — CONFIRMED_ACCELERATION — score 7.224/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LIGHTER-EUR — BUILDING_ACCELERATION — score 6.019/10 — DETECTED_BUT_TOO_LATE
- BOB-EUR — BUILDING_ACCELERATION — score 5.247/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AIOZ-EUR — BUILDING_ACCELERATION — score 5.071/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SOSO-EUR — MEMORY_24H — score mémoire 9.254/10 — sources ACCELERATION — MEMORY_ONLY
- GRASS-EUR — ACTIVE_NOW — score mémoire 9.229/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TRIA-EUR — MEMORY_24H — score mémoire 9.219/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HFT-EUR — ACTIVE_NOW — score mémoire 9.146/10 — sources ACCELERATION — WATCH_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.369/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LINK-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZBCN-EUR — ACTIVE_NOW — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 7.969/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +38.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CPOOL-EUR +26.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +23.92% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- NIL-EUR +23.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +18.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +15.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LIGHTER-EUR +13.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +11.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +11.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ACE-EUR +10.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
