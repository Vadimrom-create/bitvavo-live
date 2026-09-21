# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T07:50:39.377965+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : APT-EUR | action ACHETE_MAINTENANT | opportunité 7.968 | entrée 7.050 | trend 8.150 | rang 7.432
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PENDLE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.733 | entrée 6.100 | trend 8.650 | rang 7.643
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : INJ-EUR | action LATENT_ACCELERATOR | opportunité 7.789 | entrée 5.500 | trend 8.650 | rang 7.597
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : STX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.312 | entrée 6.150 | trend 8.650 | rang 8.376
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.376
2. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.066
3. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.043

## Accélération indépendante

- DYM-EUR — BUILDING_ACCELERATION — score 6.149/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 5.614/10 — DETECTED_BUT_TOO_LATE
- VERONA-EUR — BUILDING_ACCELERATION — score 5.314/10 — DETECTED_BUT_TOO_LATE
- NOM-EUR — BUILDING_ACCELERATION — score 5.064/10 — DETECTED_BUT_TOO_LATE
- POPCAT-EUR — BUILDING_ACCELERATION — score 4.936/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — BUILDING_ACCELERATION — score 4.910/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- APT-EUR — ACTIVE_NOW — score mémoire 7.432/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CTC-EUR — MEMORY_24H — score mémoire 9.245/10 — sources ACCELERATION — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.049/10 — sources ACCELERATION — MEMORY_ONLY
- FORM-EUR — MEMORY_24H — score mémoire 8.879/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BOME-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HOME-EUR — MEMORY_24H — score mémoire 8.582/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- USELESS-EUR — MEMORY_24H — score mémoire 8.481/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +65.32% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PTB-EUR +51.36% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +36.61% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +35.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +30.42% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EPIC-EUR +27.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NEAR-EUR +24.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +24.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VVV-EUR +22.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +19.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
