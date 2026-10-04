# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-04T13:26:22.215527+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : STX-EUR | action ACHETE_MAINTENANT | opportunité 8.035 | entrée 7.050 | trend 7.700 | rang 7.386
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ATH-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.664 | entrée 6.200 | trend 8.700 | rang 7.617
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : GALA-EUR | action LATENT_ACCELERATOR | opportunité 8.078 | entrée 4.950 | trend 8.700 | rang 7.682
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MANA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.217 | entrée 6.750 | trend 8.400 | rang 8.289
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. STX-EUR — ACHETE_MAINTENANT — rank 7.386 — opportunité 8.035 — entrée 7.050 — trend 7.700

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. MANA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.289
2. ILV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.137
3. HUMA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.923

## Accélération indépendante

- POND-EUR — CONFIRMED_ACCELERATION — score 9.527/10 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — CONFIRMED_ACCELERATION — score 8.157/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MANA-EUR — CONFIRMED_ACCELERATION — score 7.754/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAND-EUR — CONFIRMED_ACCELERATION — score 7.669/10 — DETECTED_BUT_TOO_LATE
- MAGIC-EUR — CONFIRMED_ACCELERATION — score 6.896/10 — DETECTED_BUT_TOO_LATE
- PIXEL-EUR — BUILDING_ACCELERATION — score 6.133/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLMR-EUR — BUILDING_ACCELERATION — score 5.305/10 — DETECTED_BUT_TOO_LATE
- ILV-EUR — BUILDING_ACCELERATION — score 4.790/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- POND-EUR — ACTIVE_NOW — score mémoire 9.527/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- FIDA-EUR — MEMORY_24H — score mémoire 9.160/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MANA-EUR — ACTIVE_NOW — score mémoire 8.289/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SWELL-EUR — ACTIVE_NOW — score mémoire 8.157/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ILV-EUR — ACTIVE_NOW — score mémoire 8.137/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HUMA-EUR — ACTIVE_NOW — score mémoire 7.923/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KSM-EUR — ACTIVE_NOW — score mémoire 7.842/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 7.791/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PUMP-EUR — ACTIVE_NOW — score mémoire 7.782/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- BEAM-EUR +29.29% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +29.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRK-EUR +24.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +24.66% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOS-EUR +16.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AKT-EUR +14.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AXS-EUR +14.00% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FUN-EUR +13.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOM-EUR +13.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BAT-EUR +12.71% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
