# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T20:51:51.695304+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ETC-EUR | action ACHETE_MAINTENANT | opportunité 9.133 | entrée 7.500 | trend 8.100 | rang 8.135
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.765 | entrée 5.950 | trend 8.500 | rang 7.508
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZK-EUR | action LATENT_ACCELERATOR | opportunité 8.531 | entrée 5.750 | trend 8.150 | rang 7.608
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : THE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.206 | entrée 7.100 | trend 8.350 | rang 7.961
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ETC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.135
2. THE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.961
3. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.778

## Accélération indépendante

- LAPTOP-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- BOME-EUR — CONFIRMED_ACCELERATION — score 6.556/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEN-EUR — BUILDING_ACCELERATION — score 6.365/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEUS-EUR — BUILDING_ACCELERATION — score 6.106/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUMP-EUR — BUILDING_ACCELERATION — score 5.617/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DRIFT-EUR — BUILDING_ACCELERATION — score 5.203/10 — DETECTED_BUT_TOO_LATE
- JUP-EUR — BUILDING_ACCELERATION — score 4.985/10 — DETECTED_BUT_TOO_LATE
- AIXBT-EUR — BUILDING_ACCELERATION — score 4.913/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XYO-EUR — BUILDING_ACCELERATION — score 4.759/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 9.440/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- APE-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ETC-EUR — ACTIVE_NOW — score mémoire 8.135/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- THE-EUR — ACTIVE_NOW — score mémoire 7.961/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CHR-EUR — MEMORY_24H — score mémoire 7.801/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TRAC-EUR — MEMORY_24H — score mémoire 7.788/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.778/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- DRIFT-EUR +44.10% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +30.67% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- BCH-EUR +26.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +22.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PENGU-EUR +19.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +17.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KITE-EUR +17.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +17.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +15.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TIA-EUR +15.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
