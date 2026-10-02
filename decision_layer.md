# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T02:10:42.823194+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ZRO-EUR | action ACHETE_MAINTENANT | opportunité 9.344 | entrée 6.850 | trend 8.550 | rang 8.328
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : DYDX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.119 | entrée 6.050 | trend 8.700 | rang 7.821
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : HUMA-EUR | action LATENT_ACCELERATOR | opportunité 7.854 | entrée 5.750 | trend 8.850 | rang 7.427
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MON-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.667 | entrée 6.450 | trend 8.550 | rang 7.811
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ZRO-EUR — ACHETE_MAINTENANT — rank 8.328 — opportunité 9.344 — entrée 6.850 — trend 8.550
2. AAVE-EUR — ACHETE_MAINTENANT — rank 8.093 — opportunité 8.660 — entrée 7.750 — trend 8.700
3. FET-EUR — ACHETE_MAINTENANT — rank 7.411 — opportunité 8.884 — entrée 7.500 — trend 6.550
4. ICP-EUR — ACHETE_MAINTENANT — rank 7.254 — opportunité 8.798 — entrée 6.800 — trend 6.500
5. ETH-EUR — ACHETE_MAINTENANT — rank 6.800 — opportunité 8.581 — entrée 7.600 — trend 5.350
6. BTC-EUR — ACHETE_MAINTENANT — rank 6.748 — opportunité 8.523 — entrée 7.950 — trend 5.100

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ZRO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.328
2. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.093
3. DYDX-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.821

## Accélération indépendante

- QNT-EUR — CONFIRMED_ACCELERATION — score 9.087/10 — DETECTED_BUT_TOO_LATE
- SUPER-EUR — CONFIRMED_ACCELERATION — score 7.252/10 — DETECTED_BUT_TOO_LATE
- CVX-EUR — CONFIRMED_ACCELERATION — score 6.909/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MON-EUR — BUILDING_ACCELERATION — score 6.306/10 — DETECTED_BUT_TOO_LATE
- CAP-EUR — BUILDING_ACCELERATION — score 6.231/10 — DETECTED_BUT_TOO_LATE
- NOM-EUR — BUILDING_ACCELERATION — score 6.205/10 — DETECTED_BUT_TOO_LATE
- SCR-EUR — BUILDING_ACCELERATION — score 5.983/10 — DETECTED_BUT_TOO_LATE
- BAND-EUR — BUILDING_ACCELERATION — score 5.763/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — BUILDING_ACCELERATION — score 5.681/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 2Z-EUR — BUILDING_ACCELERATION — score 5.558/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QNT-EUR — ACTIVE_NOW — score mémoire 9.087/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — MEMORY_24H — score mémoire 8.847/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 8.328/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 8.294/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.093/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.002/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +157.04% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GTC-EUR +76.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SCR-EUR +36.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MOVR-EUR +24.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MEGA-EUR +23.86% — DETECTED_EARLY — couche NONE — action NONE
- NOM-EUR +22.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +20.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +18.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +16.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +15.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
