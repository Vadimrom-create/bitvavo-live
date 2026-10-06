# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-06T21:02:40.276553+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AKT-EUR | action ACHETE_MAINTENANT | opportunité 8.251 | entrée 6.900 | trend 8.400 | rang 7.824
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : LPT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.481 | entrée 6.450 | trend 8.250 | rang 7.425
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ESP-EUR | action LATENT_ACCELERATOR | opportunité 7.719 | entrée 5.300 | trend 9.000 | rang 7.667
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RENDER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.174 | entrée 7.400 | trend 9.200 | rang 8.200
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AKT-EUR — ACHETE_MAINTENANT — rank 7.824 — opportunité 8.251 — entrée 6.900 — trend 8.400
2. APT-EUR — ACHETE_MAINTENANT — rank 7.197 — opportunité 7.991 — entrée 6.850 — trend 7.350

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.200
2. API3-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.919
3. ADA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.861

## Accélération indépendante

- EDU-EUR — CONFIRMED_ACCELERATION — score 6.779/10 — DETECTED_BUT_TOO_LATE
- INJ-EUR — BUILDING_ACCELERATION — score 6.061/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ORCA-EUR — BUILDING_ACCELERATION — score 5.880/10 — DETECTED_BUT_TOO_LATE
- WELL-EUR — BUILDING_ACCELERATION — score 5.153/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- UMA-EUR — MEMORY_24H — score mémoire 9.443/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.200/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 7.931/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- API3-EUR — ACTIVE_NOW — score mémoire 7.919/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — MEMORY_24H — score mémoire 7.875/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ADA-EUR — ACTIVE_NOW — score mémoire 7.861/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 7.851/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AKT-EUR — ACTIVE_NOW — score mémoire 7.824/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 7.804/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZEUS-EUR +61.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ORCA-EUR +38.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NMR-EUR +29.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +19.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RLC-EUR +17.90% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MET-EUR +13.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NPC-EUR +12.43% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- EDU-EUR +12.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRB-EUR +11.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- API3-EUR +9.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
