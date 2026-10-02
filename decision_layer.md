# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T02:30:42.125349+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.256 | entrée 7.600 | trend 8.700 | rang 7.970
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : HUMA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.854 | entrée 5.950 | trend 8.850 | rang 7.589
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DYDX-EUR | action LATENT_ACCELERATOR | opportunité 7.857 | entrée 5.600 | trend 8.700 | rang 7.623
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MON-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.364 | entrée 7.150 | trend 8.550 | rang 8.237
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 7.970 — opportunité 8.256 — entrée 7.600 — trend 8.700
2. SOL-EUR — ACHETE_MAINTENANT — rank 7.136 — opportunité 8.684 — entrée 7.400 — trend 5.800
3. ONDO-EUR — ACHETE_MAINTENANT — rank 7.106 — opportunité 8.695 — entrée 7.400 — trend 5.900
4. FET-EUR — ACHETE_MAINTENANT — rank 7.095 — opportunité 8.252 — entrée 7.000 — trend 6.550
5. LINK-EUR — ACHETE_MAINTENANT — rank 6.918 — opportunité 8.077 — entrée 7.600 — trend 6.050
6. ETH-EUR — ACHETE_MAINTENANT — rank 6.417 — opportunité 7.607 — entrée 7.450 — trend 5.350
7. BTC-EUR — ACHETE_MAINTENANT — rank 6.360 — opportunité 7.536 — entrée 7.950 — trend 5.100

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. MON-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.237
2. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.970
3. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.870

## Accélération indépendante

- CVX-EUR — CONFIRMED_ACCELERATION — score 9.041/10 — DETECTED_BUT_TOO_LATE
- DEEP-EUR — CONFIRMED_ACCELERATION — score 7.366/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PTB-EUR — CONFIRMED_ACCELERATION — score 6.678/10 — DETECTED_BUT_TOO_LATE
- CAP-EUR — CONFIRMED_ACCELERATION — score 6.569/10 — DETECTED_BUT_TOO_LATE
- AVA-EUR — BUILDING_ACCELERATION — score 6.274/10 — DETECTED_BUT_TOO_LATE
- RLC-EUR — BUILDING_ACCELERATION — score 5.596/10 — DETECTED_BUT_TOO_LATE
- CT-EUR — BUILDING_ACCELERATION — score 4.938/10 — DETECTED_BUT_TOO_LATE
- PIXEL-EUR — BUILDING_ACCELERATION — score 4.900/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CVX-EUR — ACTIVE_NOW — score mémoire 9.041/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — MEMORY_24H — score mémoire 8.847/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 8.294/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MON-EUR — ACTIVE_NOW — score mémoire 8.237/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AGI-EUR — MEMORY_24H — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.002/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.970/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +138.80% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GTC-EUR +79.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVR-EUR +25.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SCR-EUR +25.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MEGA-EUR +23.45% — DETECTED_EARLY — couche NONE — action NONE
- SYN-EUR +19.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CT-EUR +19.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +18.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +17.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALICE-EUR +17.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
