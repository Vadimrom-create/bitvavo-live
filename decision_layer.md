# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T01:53:04.247517+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.892 | entrée 7.750 | trend 8.700 | rang 8.265
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : TLM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.676 | entrée 6.250 | trend 7.300 | rang 6.707
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DYDX-EUR | action LATENT_ACCELERATOR | opportunité 8.147 | entrée 5.600 | trend 8.700 | rang 7.792
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : C-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.767 | entrée 6.300 | trend 8.500 | rang 7.606
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.265 — opportunité 8.892 — entrée 7.750 — trend 8.700
2. ZRO-EUR — ACHETE_MAINTENANT — rank 7.999 — opportunité 8.526 — entrée 7.100 — trend 8.550
3. OP-EUR — ACHETE_MAINTENANT — rank 6.856 — opportunité 8.093 — entrée 7.250 — trend 5.950

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.265
2. ZRO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.999
3. DYDX-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.792

## Accélération indépendante

- TOWNS-EUR — CONFIRMED_ACCELERATION — score 8.818/10 — DETECTED_BUT_TOO_LATE
- SWEAT-EUR — CONFIRMED_ACCELERATION — score 8.294/10 — DETECTED_BUT_TOO_LATE
- SCR-EUR — CONFIRMED_ACCELERATION — score 7.856/10 — DETECTED_BUT_TOO_LATE
- TLM-EUR — CONFIRMED_ACCELERATION — score 7.030/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — BUILDING_ACCELERATION — score 6.293/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GTC-EUR — BUILDING_ACCELERATION — score 5.687/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 5.670/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ACT-EUR — BUILDING_ACCELERATION — score 5.307/10 — DETECTED_BUT_TOO_LATE
- SXT-EUR — BUILDING_ACCELERATION — score 4.759/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.847/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TOWNS-EUR — ACTIVE_NOW — score mémoire 8.818/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- SWEAT-EUR — ACTIVE_NOW — score mémoire 8.294/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.265/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.002/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 7.999/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +124.34% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GTC-EUR +87.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SCR-EUR +34.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MOVR-EUR +33.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MEGA-EUR +24.28% — DETECTED_EARLY — couche NONE — action NONE
- SYN-EUR +19.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +18.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOM-EUR +17.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +15.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +12.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
