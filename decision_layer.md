# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T08:14:19.095665+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PENDLE-EUR | action ACHETE_MAINTENANT | opportunité 9.295 | entrée 7.400 | trend 8.650 | rang 8.518
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ACH-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.625 | entrée 6.150 | trend 8.450 | rang 7.512
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CELO-EUR | action LATENT_ACCELERATOR | opportunité 7.831 | entrée 5.000 | trend 8.450 | rang 7.386
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.409 | entrée 6.700 | trend 8.900 | rang 8.479
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PENDLE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.518
2. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.479
3. TAO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.221

## Accélération indépendante

- ICX-EUR — CONFIRMED_ACCELERATION — score 8.310/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEAQ-EUR — BUILDING_ACCELERATION — score 5.753/10 — DETECTED_BUT_TOO_LATE
- FORM-EUR — BUILDING_ACCELERATION — score 5.552/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MORPHO-EUR — BUILDING_ACCELERATION — score 5.511/10 — DETECTED_BUT_TOO_LATE
- TRUMP-EUR — BUILDING_ACCELERATION — score 5.451/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VVV-EUR — BUILDING_ACCELERATION — score 5.124/10 — DETECTED_BUT_TOO_LATE
- GWEI-EUR — BUILDING_ACCELERATION — score 5.068/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GTC-EUR — BUILDING_ACCELERATION — score 5.046/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ACE-EUR — BUILDING_ACCELERATION — score 4.936/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MET-EUR — BUILDING_ACCELERATION — score 4.851/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CTC-EUR — MEMORY_24H — score mémoire 9.245/10 — sources ACCELERATION — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.049/10 — sources ACCELERATION — MEMORY_ONLY
- BOME-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HOME-EUR — MEMORY_24H — score mémoire 8.582/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.518/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 8.479/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICX-EUR — ACTIVE_NOW — score mémoire 8.310/10 — sources ACCELERATION, V4 — WATCH_ONLY
- BLUR-EUR — MEMORY_24H — score mémoire 8.302/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +68.74% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PTB-EUR +55.26% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +36.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FTT-EUR +35.34% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +32.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +24.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VVV-EUR +24.78% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EPIC-EUR +23.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NEAR-EUR +20.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +18.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
