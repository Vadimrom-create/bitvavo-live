# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T09:52:06.908484+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.402 | entrée 7.100 | trend 8.000 | rang 7.809
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MANTA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.785 | entrée 5.850 | trend 8.350 | rang 7.516
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : PEAQ-EUR | action LATENT_ACCELERATOR | opportunité 9.208 | entrée 5.700 | trend 8.100 | rang 7.808
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LTC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.239 | entrée 7.050 | trend 9.000 | rang 8.116
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.116
2. MOVR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.114
3. ZK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.896

## Accélération indépendante

- AVA-EUR — CONFIRMED_ACCELERATION — score 7.913/10 — DETECTED_BUT_TOO_LATE
- HFT-EUR — CONFIRMED_ACCELERATION — score 6.806/10 — DETECTED_BUT_TOO_LATE
- COTI-EUR — CONFIRMED_ACCELERATION — score 6.762/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — DETECTED_BUT_TOO_LATE
- NOM-EUR — BUILDING_ACCELERATION — score 6.111/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CPOOL-EUR — BUILDING_ACCELERATION — score 5.994/10 — DETECTED_BUT_TOO_LATE
- ACE-EUR — BUILDING_ACCELERATION — score 5.470/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RE-EUR — BUILDING_ACCELERATION — score 5.157/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SLX-EUR — MEMORY_24H — score mémoire 9.336/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TRIA-EUR — MEMORY_24H — score mémoire 9.219/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ALLO-EUR — MEMORY_24H — score mémoire 8.962/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CETUS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.118/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.116/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MOVR-EUR — ACTIVE_NOW — score mémoire 8.114/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LINK-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +47.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +34.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +33.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +30.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +27.34% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ALLO-EUR +25.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +23.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TIA-EUR +22.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PENGU-EUR +21.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +20.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
