# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T09:47:58.000015+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XLM-EUR | action ACHETE_MAINTENANT | opportunité 8.252 | entrée 7.700 | trend 8.750 | rang 7.816
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : ORCA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.985 | entrée 5.800 | trend 7.500 | rang 7.574
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ALICE-EUR | action LATENT_ACCELERATOR | opportunité 8.018 | entrée 5.500 | trend 8.850 | rang 7.323
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : JASMY-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.167 | entrée 7.700 | trend 8.700 | rang 8.017
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XLM-EUR — ACHETE_MAINTENANT — rank 7.816 — opportunité 8.252 — entrée 7.700 — trend 8.750
2. LINK-EUR — ACHETE_MAINTENANT — rank 7.784 — opportunité 8.519 — entrée 7.250 — trend 9.200
3. EIGEN-EUR — ACHETE_MAINTENANT — rank 7.089 — opportunité 8.022 — entrée 7.150 — trend 7.300

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. JASMY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.017
2. IMX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.978
3. GALA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.913

## Accélération indépendante

- ICX-EUR — CONFIRMED_ACCELERATION — score 9.498/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SYRUP-EUR — CONFIRMED_ACCELERATION — score 8.215/10 — DETECTED_BUT_TOO_LATE
- KITE-EUR — CONFIRMED_ACCELERATION — score 7.643/10 — DETECTED_BUT_TOO_LATE
- SNX-EUR — CONFIRMED_ACCELERATION — score 7.312/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — CONFIRMED_ACCELERATION — score 6.998/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GWEI-EUR — CONFIRMED_ACCELERATION — score 6.688/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CTK-EUR — BUILDING_ACCELERATION — score 6.188/10 — DETECTED_BUT_TOO_LATE
- WAXP-EUR — BUILDING_ACCELERATION — score 6.042/10 — DETECTED_BUT_TOO_LATE
- PUMP-EUR — BUILDING_ACCELERATION — score 6.023/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ONG-EUR — BUILDING_ACCELERATION — score 5.782/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- ICX-EUR — ACTIVE_NOW — score mémoire 9.498/10 — sources ACCELERATION, V4 — WATCH_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 9.052/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.836/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 8.690/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.582/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 8.215/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- POND-EUR +46.42% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NMR-EUR +28.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +23.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CRV-EUR +23.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +23.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYRUP-EUR +21.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CVX-EUR +18.32% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- INIT-EUR +18.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 0G-EUR +16.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +15.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
