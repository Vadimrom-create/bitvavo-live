# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T08:23:19.073695+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : NPC-EUR | action ACHETE_MAINTENANT | opportunité 9.008 | entrée 7.150 | trend 7.700 | rang 7.875
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MANTA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.875 | entrée 5.900 | trend 8.350 | rang 7.577
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RED-EUR | action LATENT_ACCELERATOR | opportunité 8.068 | entrée 5.700 | trend 8.650 | rang 7.697
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LTC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.392 | entrée 7.000 | trend 9.000 | rang 8.176
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.176
2. KMNO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.118
3. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.077

## Accélération indépendante

- ARPA-EUR — CONFIRMED_ACCELERATION — score 8.448/10 — DETECTED_BUT_TOO_LATE
- PORTAL-EUR — CONFIRMED_ACCELERATION — score 7.969/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EPIC-EUR — CONFIRMED_ACCELERATION — score 7.878/10 — DETECTED_BUT_TOO_LATE
- 0G-EUR — CONFIRMED_ACCELERATION — score 7.613/10 — DETECTED_BUT_TOO_LATE
- ALLO-EUR — CONFIRMED_ACCELERATION — score 7.584/10 — DETECTED_BUT_TOO_LATE
- TIA-EUR — CONFIRMED_ACCELERATION — score 6.792/10 — DETECTED_BUT_TOO_LATE
- VIRTUAL-EUR — BUILDING_ACCELERATION — score 6.009/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOON-EUR — BUILDING_ACCELERATION — score 5.797/10 — DETECTED_BUT_TOO_LATE
- KAIA-EUR — BUILDING_ACCELERATION — score 5.691/10 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — BUILDING_ACCELERATION — score 5.411/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- NPC-EUR — ACTIVE_NOW — score mémoire 7.875/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- IKA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CPOOL-EUR — MEMORY_24H — score mémoire 9.530/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SLX-EUR — MEMORY_24H — score mémoire 9.336/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CETUS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARPA-EUR — ACTIVE_NOW — score mémoire 8.448/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- BTT-EUR — MEMORY_24H — score mémoire 8.284/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.176/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 8.118/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- CPOOL-EUR +39.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +35.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +34.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +33.25% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +25.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +24.50% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SENT-EUR +21.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +21.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALLO-EUR +21.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PENGU-EUR +20.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
