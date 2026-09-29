# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T00:54:31.731933+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XDC-EUR | action ACHETE_MAINTENANT | opportunité 8.923 | entrée 7.350 | trend 9.000 | rang 8.341
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CRV-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.792 | entrée 6.500 | trend 8.450 | rang 7.459
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CRO-EUR | action LATENT_ACCELERATOR | opportunité 7.846 | entrée 5.750 | trend 8.450 | rang 7.581
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : C-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.170 | entrée 6.650 | trend 8.450 | rang 8.239
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XDC-EUR — ACHETE_MAINTENANT — rank 8.341 — opportunité 8.923 — entrée 7.350 — trend 9.000
2. LINK-EUR — ACHETE_MAINTENANT — rank 8.049 — opportunité 8.873 — entrée 7.400 — trend 8.650
3. XLM-EUR — ACHETE_MAINTENANT — rank 8.001 — opportunité 8.276 — entrée 7.450 — trend 8.800
4. ALGO-EUR — ACHETE_MAINTENANT — rank 7.247 — opportunité 7.952 — entrée 6.950 — trend 8.500

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XDC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.341
2. C-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.239
3. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.049

## Accélération indépendante

- SYRUP-EUR — CONFIRMED_ACCELERATION — score 7.442/10 — DETECTED_BUT_TOO_LATE
- C-EUR — BUILDING_ACCELERATION — score 6.198/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — BUILDING_ACCELERATION — score 6.111/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NMR-EUR — BUILDING_ACCELERATION — score 6.009/10 — DETECTED_BUT_TOO_LATE
- CELO-EUR — BUILDING_ACCELERATION — score 5.753/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SNX-EUR — BUILDING_ACCELERATION — score 5.579/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JUP-EUR — BUILDING_ACCELERATION — score 5.418/10 — DETECTED_BUT_TOO_LATE
- 0G-EUR — BUILDING_ACCELERATION — score 5.069/10 — DETECTED_BUT_TOO_LATE
- GLMR-EUR — BUILDING_ACCELERATION — score 5.065/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HAEDAL-EUR — BUILDING_ACCELERATION — score 5.036/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 8.341/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- C-EUR — ACTIVE_NOW — score mémoire 8.239/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 8.049/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- XLM-EUR — ACTIVE_NOW — score mémoire 8.001/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIXBT-EUR — MEMORY_24H — score mémoire 7.962/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- VIRTUAL-EUR — ACTIVE_NOW — score mémoire 7.775/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.773/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NMR-EUR +34.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +25.07% — DETECTED_EARLY — couche NONE — action NONE
- 0G-EUR +16.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALGO-EUR +13.63% — DETECTED_EARLY — couche NONE — action NONE
- LINK-EUR +10.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IKA-EUR +9.91% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- SYRUP-EUR +9.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NPC-EUR +7.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AZTEC-EUR +7.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CRV-EUR +7.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
