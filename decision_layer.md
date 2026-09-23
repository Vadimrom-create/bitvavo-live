# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T17:29:28.856830+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : LPT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.573 | entrée 6.300 | trend 8.400 | rang 7.384
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : GRT-EUR | action LATENT_ACCELERATOR | opportunité 7.949 | entrée 5.750 | trend 8.850 | rang 7.483
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SENT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.021 | entrée 7.150 | trend 8.600 | rang 7.947
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SENT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.947
2. BAT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.882
3. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.609

## Accélération indépendante

- DBR-EUR — CONFIRMED_ACCELERATION — score 8.077/10 — DETECTED_BUT_TOO_LATE
- ZRO-EUR — CONFIRMED_ACCELERATION — score 7.185/10 — DETECTED_BUT_TOO_LATE
- ALLO-EUR — BUILDING_ACCELERATION — score 6.461/10 — DETECTED_BUT_TOO_LATE
- SENT-EUR — BUILDING_ACCELERATION — score 6.047/10 — DETECTED_BUT_TOO_LATE
- CFG-EUR — BUILDING_ACCELERATION — score 5.844/10 — DETECTED_BUT_TOO_LATE
- FTT-EUR — BUILDING_ACCELERATION — score 5.827/10 — DETECTED_BUT_TOO_LATE
- DOGS-EUR — BUILDING_ACCELERATION — score 5.431/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GALA-EUR — BUILDING_ACCELERATION — score 5.191/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LMWR-EUR — BUILDING_ACCELERATION — score 5.043/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUFFER-EUR — BUILDING_ACCELERATION — score 4.893/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SOSO-EUR — MEMORY_24H — score mémoire 9.254/10 — sources ACCELERATION — MEMORY_ONLY
- TRIA-EUR — MEMORY_24H — score mémoire 9.219/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DBR-EUR — ACTIVE_NOW — score mémoire 8.077/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LINK-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.003/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 7.969/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.947/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- BAT-EUR — ACTIVE_NOW — score mémoire 7.882/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +34.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +32.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DBR-EUR +26.99% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- NIL-EUR +19.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +15.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +14.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +13.72% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LIGHTER-EUR +11.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALLO-EUR +10.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SENT-EUR +10.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
