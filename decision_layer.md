# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T13:38:58.817765+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ENA-EUR | action ACHETE_MAINTENANT | opportunité 9.214 | entrée 7.650 | trend 7.900 | rang 8.044
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ALICE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.306 | entrée 5.850 | trend 8.650 | rang 7.600
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MIOTA-EUR | action LATENT_ACCELERATOR | opportunité 7.767 | entrée 5.200 | trend 8.900 | rang 7.641
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LINK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.335 | entrée 6.500 | trend 9.200 | rang 8.166
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ENA-EUR — ACHETE_MAINTENANT — rank 8.044 — opportunité 9.214 — entrée 7.650 — trend 7.900
2. CFG-EUR — ACHETE_MAINTENANT — rank 7.495 — opportunité 7.557 — entrée 7.200 — trend 8.150
3. SOL-EUR — ACHETE_MAINTENANT — rank 6.911 — opportunité 7.829 — entrée 7.600 — trend 6.250
4. XRP-EUR — ACHETE_MAINTENANT — rank 6.106 — opportunité 7.428 — entrée 7.150 — trend 4.850

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. LINK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.166
2. XDC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.101
3. GALA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.093

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- NOS-EUR — CONFIRMED_ACCELERATION — score 8.272/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XDP-EUR — CONFIRMED_ACCELERATION — score 7.948/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MLN-EUR — CONFIRMED_ACCELERATION — score 7.913/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDGE-EUR — BUILDING_ACCELERATION — score 5.803/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — BUILDING_ACCELERATION — score 5.038/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- TREAD-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.836/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 8.690/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY
- BONK-EUR — MEMORY_24H — score mémoire 8.619/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.582/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOS-EUR — ACTIVE_NOW — score mémoire 8.272/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- 0G-EUR +36.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- POND-EUR +32.69% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZBCN-EUR +21.74% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CELO-EUR +20.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CRV-EUR +20.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CVX-EUR +18.38% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SYRUP-EUR +17.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +15.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AAVE-EUR +15.46% — DETECTED_EARLY — couche NONE — action NONE
- EDEN-EUR +13.62% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
