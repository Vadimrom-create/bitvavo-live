# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-06T20:54:32.318265+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AKT-EUR | action ACHETE_MAINTENANT | opportunité 9.217 | entrée 6.900 | trend 8.400 | rang 8.262
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : API3-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.802 | entrée 5.800 | trend 8.950 | rang 7.658
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ESP-EUR | action LATENT_ACCELERATOR | opportunité 7.718 | entrée 5.300 | trend 9.000 | rang 7.666
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RENDER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.137 | entrée 7.400 | trend 9.200 | rang 8.183
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AKT-EUR — ACHETE_MAINTENANT — rank 8.262 — opportunité 9.217 — entrée 6.900 — trend 8.400
2. APT-EUR — ACHETE_MAINTENANT — rank 7.151 — opportunité 8.052 — entrée 6.850 — trend 7.350

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AKT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.262
2. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.183
3. ADA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.799

## Accélération indépendante

- SWEAT-EUR — CONFIRMED_ACCELERATION — score 7.851/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEUS-EUR — CONFIRMED_ACCELERATION — score 7.447/10 — DETECTED_BUT_TOO_LATE
- IKA-EUR — BUILDING_ACCELERATION — score 5.794/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PROM-EUR — BUILDING_ACCELERATION — score 5.685/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAGA-EUR — BUILDING_ACCELERATION — score 5.464/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — BUILDING_ACCELERATION — score 5.152/10 — DETECTED_BUT_TOO_LATE
- XYO-EUR — BUILDING_ACCELERATION — score 4.924/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 4.921/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WELL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UMA-EUR — MEMORY_24H — score mémoire 9.443/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AKT-EUR — ACTIVE_NOW — score mémoire 8.262/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.183/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 7.931/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICP-EUR — MEMORY_24H — score mémoire 7.875/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWEAT-EUR — ACTIVE_NOW — score mémoire 7.851/10 — sources ACCELERATION, V4 — WATCH_ONLY
- ADA-EUR — ACTIVE_NOW — score mémoire 7.799/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ESP-EUR — ACTIVE_NOW — score mémoire 7.666/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZEUS-EUR +62.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ORCA-EUR +38.85% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NMR-EUR +30.38% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +19.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RLC-EUR +16.55% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- EDU-EUR +13.86% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MET-EUR +12.69% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRB-EUR +12.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NPC-EUR +11.47% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- VTHO-EUR +8.79% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
