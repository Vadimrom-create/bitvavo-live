# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T04:03:45.163105+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAIKO-EUR | action ACHETE_MAINTENANT | opportunité 9.141 | entrée 7.100 | trend 8.700 | rang 8.374
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SOL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.589 | entrée 6.000 | trend 8.500 | rang 7.511
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 7.523 | entrée 5.550 | trend 8.500 | rang 7.427
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.280 | entrée 6.550 | trend 8.950 | rang 7.979
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAIKO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.374
2. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.979
3. HBAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.976

## Accélération indépendante

- NEIRO-EUR — CONFIRMED_ACCELERATION — score 6.777/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEPE-EUR — BUILDING_ACCELERATION — score 6.365/10 — DETECTED_BUT_TOO_LATE
- IKA-EUR — BUILDING_ACCELERATION — score 6.179/10 — DETECTED_BUT_TOO_LATE
- PUFFER-EUR — BUILDING_ACCELERATION — score 6.128/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DOGE-EUR — BUILDING_ACCELERATION — score 5.941/10 — DETECTED_BUT_TOO_LATE
- KITE-EUR — BUILDING_ACCELERATION — score 5.921/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WIF-EUR — BUILDING_ACCELERATION — score 5.862/10 — DETECTED_BUT_TOO_LATE
- BONK-EUR — BUILDING_ACCELERATION — score 5.438/10 — DETECTED_BUT_TOO_LATE
- PROMPT-EUR — BUILDING_ACCELERATION — score 5.000/10 — DETECTED_BUT_TOO_LATE
- ZIL-EUR — BUILDING_ACCELERATION — score 4.985/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- HBAR-EUR — ACTIVE_NOW — score mémoire 7.976/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- GIGA-EUR — MEMORY_24H — score mémoire 9.738/10 — sources ACCELERATION — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 9.177/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.781/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.732/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.438/10 — sources ACCELERATION — MEMORY_ONLY
- TAIKO-EUR — ACTIVE_NOW — score mémoire 8.374/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ICX-EUR +87.63% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +71.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KERNEL-EUR +47.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +41.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +40.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +31.31% — DETECTED_EARLY — couche NONE — action NONE
- WIF-EUR +24.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +20.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CARV-EUR +19.73% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- FARTCOIN-EUR +18.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
