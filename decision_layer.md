# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T11:19:51.175225+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ALGO-EUR | action ACHETE_MAINTENANT | opportunité 8.035 | entrée 6.950 | trend 8.650 | rang 7.844
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AZTEC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.701 | entrée 6.650 | trend 8.150 | rang 7.480
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DYDX-EUR | action LATENT_ACCELERATOR | opportunité 8.000 | entrée 5.550 | trend 8.950 | rang 7.736
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : NOM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.537 | entrée 6.300 | trend 8.650 | rang 7.927
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ALGO-EUR — ACHETE_MAINTENANT — rank 7.844 — opportunité 8.035 — entrée 6.950 — trend 8.650
2. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.822 — opportunité 8.895 — entrée 6.950 — trend 7.650
3. PUMP-EUR — ACHETE_MAINTENANT — rank 7.220 — opportunité 8.110 — entrée 7.050 — trend 7.800
4. ORCA-EUR — ACHETE_MAINTENANT — rank 7.145 — opportunité 8.251 — entrée 6.900 — trend 7.150

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. NOM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.927
2. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.886
3. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.844

## Accélération indépendante

- U-EUR — CONFIRMED_ACCELERATION — score 8.740/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — CONFIRMED_ACCELERATION — score 6.914/10 — DETECTED_BUT_TOO_LATE
- QNT-EUR — BUILDING_ACCELERATION — score 6.092/10 — DETECTED_BUT_TOO_LATE
- UP-EUR — BUILDING_ACCELERATION — score 5.761/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KITE-EUR — BUILDING_ACCELERATION — score 5.186/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NPC-EUR — BUILDING_ACCELERATION — score 5.023/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CT-EUR — BUILDING_ACCELERATION — score 4.961/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.258/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OPEN-EUR — MEMORY_24H — score mémoire 9.112/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — ACTIVE_NOW — score mémoire 8.740/10 — sources ACCELERATION, V4 — WATCH_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.257/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 7.987/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOM-EUR — ACTIVE_NOW — score mémoire 7.927/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +52.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +33.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SWEAT-EUR +29.89% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CT-EUR +23.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SCR-EUR +18.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +18.20% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MAGIC-EUR +16.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZK-EUR +15.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKY-EUR +14.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AAVE-EUR +13.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
