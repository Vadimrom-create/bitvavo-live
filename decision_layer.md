# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T08:44:35.947136+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : INJ-EUR | action ACHETE_MAINTENANT | opportunité 9.188 | entrée 7.350 | trend 8.650 | rang 8.420
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.206 | entrée 6.150 | trend 8.350 | rang 8.181
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ACH-EUR | action LATENT_ACCELERATOR | opportunité 9.211 | entrée 5.450 | trend 8.450 | rang 8.159
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COW-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.326 | entrée 6.300 | trend 8.950 | rang 8.508
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.508
2. INJ-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.420
3. LDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.305

## Accélération indépendante

- MOCA-EUR — CONFIRMED_ACCELERATION — score 8.589/10 — DETECTED_BUT_TOO_LATE
- PYTH-EUR — CONFIRMED_ACCELERATION — score 7.544/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KMNO-EUR — CONFIRMED_ACCELERATION — score 7.532/10 — DETECTED_BUT_TOO_LATE
- DEEP-EUR — CONFIRMED_ACCELERATION — score 7.516/10 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — CONFIRMED_ACCELERATION — score 7.361/10 — DETECTED_BUT_TOO_LATE
- ENS-EUR — CONFIRMED_ACCELERATION — score 6.976/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOVE-EUR — CONFIRMED_ACCELERATION — score 6.664/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEPE-EUR — BUILDING_ACCELERATION — score 6.496/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FARTCOIN-EUR — BUILDING_ACCELERATION — score 6.474/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FET-EUR — BUILDING_ACCELERATION — score 6.405/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- STX-EUR — ACTIVE_NOW — score mémoire 8.215/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- SOL-EUR — ACTIVE_NOW — score mémoire 7.965/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CTC-EUR — MEMORY_24H — score mémoire 9.245/10 — sources ACCELERATION — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.049/10 — sources ACCELERATION — MEMORY_ONLY
- BOME-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MOCA-EUR — ACTIVE_NOW — score mémoire 8.589/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- COW-EUR — ACTIVE_NOW — score mémoire 8.508/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.457/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 8.420/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +70.23% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PTB-EUR +59.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +38.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +36.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +33.45% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- KMNO-EUR +29.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +27.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +23.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- VVV-EUR +23.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +22.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
