# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T12:54:06.462417+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XLM-EUR | action ACHETE_MAINTENANT | opportunité 8.327 | entrée 7.800 | trend 9.000 | rang 8.154
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ALICE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.114 | entrée 5.850 | trend 8.650 | rang 7.658
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DIA-EUR | action LATENT_ACCELERATOR | opportunité 7.428 | entrée 4.500 | trend 8.300 | rang 7.169
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LINK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.101 | entrée 6.450 | trend 9.200 | rang 8.053
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XLM-EUR — ACHETE_MAINTENANT — rank 8.154 — opportunité 8.327 — entrée 7.800 — trend 9.000
2. AVAX-EUR — ACHETE_MAINTENANT — rank 7.384 — opportunité 7.801 — entrée 7.800 — trend 8.100
3. EIGEN-EUR — ACHETE_MAINTENANT — rank 7.348 — opportunité 7.633 — entrée 7.100 — trend 7.850
4. SOL-EUR — ACHETE_MAINTENANT — rank 7.255 — opportunité 8.603 — entrée 7.850 — trend 6.250
5. SHIB-EUR — ACHETE_MAINTENANT — rank 6.661 — opportunité 8.315 — entrée 7.300 — trend 5.450
6. XRP-EUR — ACHETE_MAINTENANT — rank 6.268 — opportunité 8.466 — entrée 7.850 — trend 4.850

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.154
2. LINK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.053
3. GALA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.002

## Accélération indépendante

- ARX-EUR — CONFIRMED_ACCELERATION — score 8.740/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CROSS-EUR — CONFIRMED_ACCELERATION — score 7.030/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XRP-EUR — CONFIRMED_ACCELERATION — score 6.706/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BONK-EUR — BUILDING_ACCELERATION — score 5.684/10 — DETECTED_BUT_TOO_LATE
- 0G-EUR — BUILDING_ACCELERATION — score 5.267/10 — DETECTED_BUT_TOO_LATE
- CSPR-EUR — BUILDING_ACCELERATION — score 5.173/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BAT-EUR — BUILDING_ACCELERATION — score 4.804/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.836/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARX-EUR — ACTIVE_NOW — score mémoire 8.740/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 8.690/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.582/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.185/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +42.26% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- 0G-EUR +40.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZBCN-EUR +24.97% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CELO-EUR +22.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYRUP-EUR +18.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CRV-EUR +18.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NMR-EUR +16.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +16.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVX-EUR +15.51% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- AAVE-EUR +15.19% — DETECTED_EARLY — couche NONE — action NONE

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
