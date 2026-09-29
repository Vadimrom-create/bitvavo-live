# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T21:01:51.685586+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 8.351 | entrée 7.150 | trend 8.700 | rang 8.049
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SKY-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.197 | entrée 5.800 | trend 9.000 | rang 7.902
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : C-EUR | action LATENT_ACCELERATOR | opportunité 7.547 | entrée 5.350 | trend 8.250 | rang 7.324
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ROSE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.298 | entrée 6.900 | trend 8.750 | rang 8.276
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. LINK-EUR — ACHETE_MAINTENANT — rank 8.049 — opportunité 8.351 — entrée 7.150 — trend 8.700
2. ICP-EUR — ACHETE_MAINTENANT — rank 7.710 — opportunité 8.700 — entrée 7.400 — trend 8.900
3. RENDER-EUR — ACHETE_MAINTENANT — rank 7.681 — opportunité 8.230 — entrée 7.700 — trend 7.850
4. AVAX-EUR — ACHETE_MAINTENANT — rank 7.573 — opportunité 8.091 — entrée 7.350 — trend 8.000
5. POL-EUR — ACHETE_MAINTENANT — rank 7.545 — opportunité 8.019 — entrée 7.200 — trend 7.750

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ROSE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.276
2. MIOTA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.138
3. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.049

## Accélération indépendante

- TRAC-EUR — CONFIRMED_ACCELERATION — score 9.019/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOVR-EUR — CONFIRMED_ACCELERATION — score 8.020/10 — DETECTED_BUT_TOO_LATE
- TRB-EUR — CONFIRMED_ACCELERATION — score 6.650/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ROSE-EUR — BUILDING_ACCELERATION — score 5.737/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBCN-EUR — BUILDING_ACCELERATION — score 5.246/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 9.160/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TRAC-EUR — ACTIVE_NOW — score mémoire 9.019/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.866/10 — sources ACCELERATION — MEMORY_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 8.276/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.145/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 8.138/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 8.049/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +30.78% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRASS-EUR +27.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVR-EUR +26.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZBCN-EUR +22.37% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- 0G-EUR +20.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +18.04% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +15.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICP-EUR +13.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INIT-EUR +13.06% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AAVE-EUR +12.41% — DETECTED_EARLY — couche NONE — action NONE

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
