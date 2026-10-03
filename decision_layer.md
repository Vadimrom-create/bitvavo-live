# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T01:48:54.291763+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 8.305 | entrée 7.150 | trend 8.700 | rang 7.497
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : IMX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.292 | entrée 5.850 | trend 8.700 | rang 7.660
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : FLUID-EUR | action LATENT_ACCELERATOR | opportunité 8.053 | entrée 5.750 | trend 9.000 | rang 7.833
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : DYDX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.340 | entrée 6.200 | trend 8.750 | rang 8.190
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. WLD-EUR — ACHETE_MAINTENANT — rank 7.497 — opportunité 8.305 — entrée 7.150 — trend 8.700
2. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.489 — opportunité 7.879 — entrée 7.150 — trend 8.150
3. SOL-EUR — ACHETE_MAINTENANT — rank 6.839 — opportunité 8.041 — entrée 7.450 — trend 6.050

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DYDX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.190
2. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.963
3. FLUID-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.833

## Accélération indépendante

- BTT-EUR — BUILDING_ACCELERATION — score 6.354/10 — DETECTED_BUT_TOO_LATE
- SOON-EUR — BUILDING_ACCELERATION — score 6.134/10 — DETECTED_BUT_TOO_LATE
- SCR-EUR — BUILDING_ACCELERATION — score 5.651/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- UP-EUR — BUILDING_ACCELERATION — score 5.623/10 — DETECTED_BUT_TOO_LATE
- INJ-EUR — BUILDING_ACCELERATION — score 5.128/10 — DETECTED_BUT_TOO_LATE
- ZBCN-EUR — BUILDING_ACCELERATION — score 4.890/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 4.781/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FOLD-EUR — MEMORY_24H — score mémoire 9.866/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — ACTIVE_NOW — score mémoire 8.190/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.963/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 7.833/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +52.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ATH-EUR +15.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GALA-EUR +15.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENJ-EUR +14.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CT-EUR +13.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WLD-EUR +11.72% — DETECTED_EARLY — couche NONE — action NONE
- MANA-EUR +11.10% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NOS-EUR +9.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- APE-EUR +9.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SPK-EUR +8.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
