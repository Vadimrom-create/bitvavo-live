# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T13:15:29.214734+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : CFG-EUR | action ACHETE_MAINTENANT | opportunité 9.210 | entrée 7.500 | trend 8.150 | rang 8.098
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SUPER-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.010 | entrée 6.650 | trend 7.500 | rang 7.756
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ALICE-EUR | action LATENT_ACCELERATOR | opportunité 8.380 | entrée 5.650 | trend 8.650 | rang 7.547
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RUNE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.292 | entrée 7.100 | trend 8.650 | rang 8.452
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. CFG-EUR — ACHETE_MAINTENANT — rank 8.098 — opportunité 9.210 — entrée 7.500 — trend 8.150
2. ICP-EUR — ACHETE_MAINTENANT — rank 7.769 — opportunité 8.353 — entrée 7.200 — trend 9.000
3. SOL-EUR — ACHETE_MAINTENANT — rank 7.062 — opportunité 8.141 — entrée 7.600 — trend 6.250
4. SHIB-EUR — ACHETE_MAINTENANT — rank 6.880 — opportunité 8.648 — entrée 7.300 — trend 5.450
5. XRP-EUR — ACHETE_MAINTENANT — rank 6.590 — opportunité 8.525 — entrée 7.600 — trend 4.850

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.452
2. C-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.243
3. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.127

## Accélération indépendante

- BONK-EUR — CONFIRMED_ACCELERATION — score 8.619/10 — DETECTED_BUT_TOO_LATE
- SOON-EUR — CONFIRMED_ACCELERATION — score 8.246/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — CONFIRMED_ACCELERATION — score 8.179/10 — DETECTED_BUT_TOO_LATE
- EDEN-EUR — CONFIRMED_ACCELERATION — score 7.441/10 — DETECTED_BUT_TOO_LATE
- PHA-EUR — CONFIRMED_ACCELERATION — score 7.322/10 — DETECTED_BUT_TOO_LATE
- NEIRO-EUR — CONFIRMED_ACCELERATION — score 7.197/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CELR-EUR — CONFIRMED_ACCELERATION — score 6.544/10 — DETECTED_BUT_TOO_LATE
- IKA-EUR — BUILDING_ACCELERATION — score 5.866/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HFT-EUR — BUILDING_ACCELERATION — score 5.431/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOVE-EUR — BUILDING_ACCELERATION — score 5.226/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.836/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 8.690/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY
- BONK-EUR — ACTIVE_NOW — score mémoire 8.619/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- U-EUR — MEMORY_24H — score mémoire 8.582/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RUNE-EUR — ACTIVE_NOW — score mémoire 8.452/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +45.09% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- 0G-EUR +38.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZBCN-EUR +23.87% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CELO-EUR +22.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CRV-EUR +19.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYRUP-EUR +17.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CVX-EUR +17.82% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- GRASS-EUR +17.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AAVE-EUR +16.62% — DETECTED_EARLY — couche NONE — action NONE
- EDEN-EUR +14.41% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Gestion des positions détenues

Policy : STAGED_10_20_RUNNER_V1
- +10% : prise partielle 35%.
- +20% : seconde prise 35%.
- Runner conservé : 30%.
- Revue coût d'opportunité après 72 h ; sortie seulement avant la première partielle, proche/sous le PRU et avec momentum 15m affaibli.
- Pas de stop serré mécaniquement après une petite hausse ; le stop reste lié à l'invalidation structurelle.

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
