# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T17:17:32.352139+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ALGO-EUR | action ACHETE_MAINTENANT | opportunité 8.040 | entrée 7.150 | trend 8.650 | rang 7.713
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MANA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.694 | entrée 6.200 | trend 8.400 | rang 7.392
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 7.543 | entrée 5.200 | trend 8.650 | rang 7.328
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.537 | entrée 7.300 | trend 9.200 | rang 8.184
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ALGO-EUR — ACHETE_MAINTENANT — rank 7.713 — opportunité 8.040 — entrée 7.150 — trend 8.650

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.184
2. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.062
3. ATH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.764

## Accélération indépendante

- GLMR-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- CAKE-EUR — BUILDING_ACCELERATION — score 5.590/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 5.266/10 — DETECTED_BUT_TOO_LATE
- KITE-EUR — BUILDING_ACCELERATION — score 5.197/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NEAR-EUR — BUILDING_ACCELERATION — score 5.189/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ADX-EUR — BUILDING_ACCELERATION — score 5.054/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RECALL-EUR — BUILDING_ACCELERATION — score 4.949/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AKT-EUR — BUILDING_ACCELERATION — score 4.809/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GLMR-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.184/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 8.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.048/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ATH-EUR — ACTIVE_NOW — score mémoire 7.764/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 7.725/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.718/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- GLMR-EUR +49.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +27.97% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRK-EUR +15.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAND-EUR +14.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +14.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FUN-EUR +13.12% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZAMA-EUR +12.82% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- HFT-EUR +12.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- XDP-EUR +9.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +9.00% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
