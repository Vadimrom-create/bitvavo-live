# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T07:07:55.658849+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 8.378 | entrée 7.950 | trend 8.750 | rang 8.076
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AUCTION-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.276 | entrée 6.050 | trend 8.500 | rang 7.741
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RED-EUR | action LATENT_ACCELERATOR | opportunité 7.840 | entrée 5.650 | trend 8.650 | rang 7.588
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.330 | entrée 8.500 | trend 8.350 | rang 8.251
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.251
2. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.076
3. TAIKO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.002

## Accélération indépendante

- CETUS-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- PTB-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- CROSS-EUR — CONFIRMED_ACCELERATION — score 8.473/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BEL-EUR — CONFIRMED_ACCELERATION — score 6.509/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DRIFT-EUR — BUILDING_ACCELERATION — score 6.229/10 — DETECTED_BUT_TOO_LATE
- MET-EUR — BUILDING_ACCELERATION — score 5.707/10 — DETECTED_BUT_TOO_LATE
- ONG-EUR — BUILDING_ACCELERATION — score 5.453/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RPL-EUR — BUILDING_ACCELERATION — score 5.416/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZK-EUR — BUILDING_ACCELERATION — score 4.945/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — BUILDING_ACCELERATION — score 4.789/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- IKA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SLX-EUR — MEMORY_24H — score mémoire 9.336/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- CETUS-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PTB-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CROSS-EUR — ACTIVE_NOW — score mémoire 8.473/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.251/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- FTT-EUR — MEMORY_24H — score mémoire 8.118/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +35.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +34.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +33.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +33.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +29.04% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SUPER-EUR +25.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +22.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PENGU-EUR +20.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +20.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DRIFT-EUR +19.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
